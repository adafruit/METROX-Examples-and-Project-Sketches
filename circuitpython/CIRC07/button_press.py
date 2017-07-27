# CIRC07 - Button Pressing
# (Circuit Python)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries.

import digitalio
from board import *
import time

led = digitalio.DigitalInOut(D13)
led.switch_to_output()
button = digitalio.DigitalInOut(D2)
button.switch_to_input()

while True:
    val = button.value
    led.value = not val
