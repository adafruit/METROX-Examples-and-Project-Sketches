# CIRC09 - Light
# (Circuit Python)

from analogio import *
from pulseio import *
from board import *
import time

led = PWMOut(D9)
light = AnalogIn(A0)

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
    mapped = _map(light.value, 20000, 65000, 0, 65535)
    print(mapped)
    led.duty_cycle = int(mapped)
