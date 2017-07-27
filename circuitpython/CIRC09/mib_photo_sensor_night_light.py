# CIRC09 - Light make it better night_light
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import analogio
#import pulseio
import digitalio
import board
import time

threshold = 60000

# led = pulseio.PWMOut(board.D9)
led = digitalio.DigitalInOut(board.D9)
led.switch_to_output()
light = analogio.AnalogIn(board.A0)

# affine transfer/_map with constrained output
def _map(x, in_min, in_max, out_min, out_max):
    outrange = float(out_max - out_min)
    inrange = float(in_max - in_min)
    ret = (x - in_min) * (outrange / inrange) + out_min
    if (out_max > out_min):
        return max(min(ret, out_max), out_min)
    else:
        return max(min(ret, out_min), out_max)

while True:
    if light.value > threshold:
        led.value = True
    else:
        led.value = False
