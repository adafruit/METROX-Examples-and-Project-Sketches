# CIRC09 - Light
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries.

import analogio
import pulseio
import board
import time
from simpleio import map_range

led = pulseio.PWMOut(board.D9)
light = analogio.AnalogIn(board.A0)

while True:
    print(light.value)
    # map reasonable light values to our LED brightness
    mapped = map_range(light.value, 20000, 65000, 0, 65535)
    print(mapped)
    # change brightness of LED
    led.duty_cycle = int(mapped)
