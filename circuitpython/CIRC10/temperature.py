"""
'temperature.py'.

=================================================
Writes TMP36 data to the REPL
"""

import analogio
import board
import time
from simpleio import map_range

sensor = analogio.AnalogIn(board.A0)


def getVoltage(p_sensor):
    v = map_range(p_sensor.value, 0, 65535, 0, 3.3)
    return v


while True:
    temp = getVoltage(sensor)
    print("Voltage =", temp, end="")
    # convert to celsius
    temp = (temp - 0.5) * 100
    print("   Temperature =", temp)
    time.sleep(1)
