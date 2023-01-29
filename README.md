# MIST
Moisture Interpreting Sensor Thing

If (for some reason) you feel like using my code you will need:  
- `Raspberry Pi Pico W`
- `Capacitive soil moisture sensor`
- `A pot plant with a nearby wall outlet`
- `Optional but recommended - RCD/GFCI` depending on how much you trust your ability to not spill water
- `Mobile Phone`

Move all the files onto the Pico W  
Edit secrets.py to have your wifi name and password  
Set your Pico W to have a static IP

Calibration:
- Run `calibration.py`
- Put your capaciative moisture sensor in water
- Take the lowest number you see and put it as the min_moisture in `soil.py`
- Put your capaciative moisture sensor in dry soil
- Take the highest number you see and put it as the max_moisture in `soil.py`

*Instructions about shortcuts goes here*
