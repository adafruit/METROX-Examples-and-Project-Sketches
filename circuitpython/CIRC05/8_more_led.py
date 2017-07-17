# CIRC05 - More LEDs
# (Circuit Python)

import digitalio
from board import *
import time

dataPin = D2
clockPin = D3
latchPin = D4

data = digitalio.DigitalInOut(dataPin)
data.switch_to_output()
clock = digitalio.DigitalInOut(clockPin)
clock.switch_to_output()
latch = digitalio.DigitalInOut(latchPin)
latch.switch_to_output()

def updateLEDs(leds):
    latch.value = False
    for bit in range(8):
        if (leds & (1<<bit)):
            data.value = True
        else:
            data.value = False
        clock.value = True
        clock.value = False
    latch.value = True

while True:
    for i in range(0,256,1):
        updateLEDs(i)
        time.sleep(0.1)
