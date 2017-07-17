# CIRC07 - Button Pressing
# (Circuit Python)

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
