# CIRC09 - Light
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries.

import analogio
import pulseio
import board
import time

led = pulseio.PWMOut(board.D9)
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
    print(light.value)
    # map reasonable light values to our LED brightness
    mapped = _map(light.value, 20000, 65000, 0, 65535)
    print(mapped)
    # change brightness of LED
    led.duty_cycle = int(mapped)
