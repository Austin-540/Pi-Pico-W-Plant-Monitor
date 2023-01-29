from machine import ADC, Pin, I2C, Timer
import machine
import utime
import network
from secrets import *
import socket
html = ""
import math

soil = ADC(Pin(28)) 
 
#Calibraton values
min_moisture=0
max_moisture=5800
 
 
def soil_tick(var):
    global moisture
    # read moisture value and convert to percentage using the calibration range
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")

Timer().init(freq=0.5, mode=Timer.PERIODIC, callback=soil_tick)

led = machine.Pin("LED", machine.Pin.OUT)


secrets_dict = get_secrets()
wifi_name = secrets_dict["network_name"]
wifi_password = secrets_dict["network_password"]


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_name, wifi_password)

max_wait = 10 #seconds

while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("Trying to connect...")
    utime.sleep(1)
    
if wlan.status() !=3:
    print("Connection Failed!")

else:
    print("Connected")
    print("IP = " + wlan.ifconfig()[0])
    led.on()
    utime.sleep(0.3)
    led.off()
    


sta_if = network.WLAN(network.STA_IF)
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    try:
        cl, addr = s.accept()
        print("Client connected from ", addr)
        request = cl.recv(1024)
        print(request)
        
        request = str(request)
        led_on = request.find("/light/on")
        led_off = request.find("/light/off")
        print("led on = " + str(led_on))
        print("led off = " + str(led_off))
        
        if led_on == 6:
            
            print("LED on - line 80")
            led.on()
            stateis = "LED ON"
        
        if led_off == 6:
            print("LED off")
            led.off()
            stateis = "LED OFF"  

        response = html + str(math.ceil(moisture))

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print("Connection closed")


