# CIRC09 - Light make it better night_light
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import analogio
import digitalio
import board
import time

threshold = 60000

led = digitalio.DigitalInOut(board.D9)
led.switch_to_output()
light = analogio.AnalogIn(board.A0)


while True:
    if light.value > threshold:
        led.value = True
    else:
        led.value = False
