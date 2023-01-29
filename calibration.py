from machine import ADC, Pin, I2C, Timer
import machine
import utime

soil = ADC(Pin(28)) 
 
while True:
    moisture = soil.read_u16()
    print(moisture)
    utime.sleep(0.5)