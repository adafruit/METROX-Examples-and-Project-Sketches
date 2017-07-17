# CIRC08 - Twisting
# (Circuit Python)

from digitalio import *
from analogio import *
from board import *
from pulseio import *
import time

Direction = DigitalInOut.direction  

led = DigitalInOut(D13)
led.switch_to_output()
pot = AnalogIn(A0)

sensorval = 0

while True:
    sensorval = pot.value / 65536
    print(sensorval)
    led.value = True
    time.sleep(sensorval)
    led.value = False
    time.sleep(sensorval)
