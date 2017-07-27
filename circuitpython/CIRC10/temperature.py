# CIRC10 - Temperature
# (Circuit Python)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada and Asher Lieber for Adafruit Industries.

import board
import analogio
import time

sensor = analogio.AnalogIn(board.A0)


# affine transfer/map with constrained output
def map(x, in_min, in_max, out_min, out_max):
    outrange = float(out_max - out_min)
    inrange = float(in_max - in_min)
    ret = (x - in_min) * (outrange / inrange) + out_min
    if (out_max > out_min):
        return max(min(ret, out_max), out_min)
    else:
        return max(min(ret, out_min), out_max)

def getVoltage(p_sensor):
    # map value from photo sensor to voltage
    v = map(p_sensor.value, 0, 65535, 0, 3.3)
    return v

# loop forever
while True:
    temp = getVoltage(sensor)
    print("Voltage =", temp, end="")
    # convert to celsius
    temp = (temp - 0.5) * 100
    print("   Temperature =", temp)
    time.sleep(0.1)
