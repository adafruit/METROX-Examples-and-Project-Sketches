"""
'temperature.py'.

=================================================
Writes TMP36 data to the REPL
"""

import time
import analogio
import board
from simpleio import map_range

TEMP_SENSOR = analogio.AnalogIn(board.A0)


def get_voltage(_temp_sensor):
    """gets the TMP36's voltage."""
    voltage_val = map_range(_temp_sensor.value, 0, 65535, 0, 3.3)
    return voltage_val


while True:
    TMP = get_voltage(TEMP_SENSOR)
    print("Voltage =", TMP, end="")
    # convert to celsius
    TMP = (TMP - 0.5) * 100
    print("   Temperature =", TMP)
    time.sleep(1)
