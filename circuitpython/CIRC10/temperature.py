# CIRC10 - Temperature
# (Circuit Python)

from analogio import *
from board import *
import time

sensor = AnalogIn(A0)


# affine transfer/map with constrained output
def map(x, in_min, in_max, out_min, out_max):
    outrange = float(out_max - out_min)
    inrange = float(in_max - in_min)
    ret = (x - in_min) * (outrange / inrange) + out_min
    if (out_max > out_min):
        return max(min(ret, out_max), out_min)
    else:
        return max(min(ret, out_min), out_max)

def getVoltage(pin):
    v = map(pin.value, 0, 65535, 0, 3.3)
    return v

while True:
    temp = getVoltage(sensor)
    print("Voltage =", temp, end="")
    temp = (temp - 0.5) * 100
    print("   Temperature =", temp)
    time.sleep(0.1)
