"""
'temperature.py'.

=================================================
Writes tmp_value36 data to the REPL
"""

import time
import analogio
import board
from simpleio import map_range

tmp36 = analogio.AnalogIn(board.A0)


def get_voltage(_temp_sensor):
    """gets the tmp_value36's voltage."""
    voltage_val = map_range(_temp_sensor.value, 0, 65535, 0, 3.3)
    return voltage_val


while True:
    tmp_value = get_voltage(tmp36)
    print("Voltage =", tmp_value, end="")
    # convert to celsius
    tmp_value = (tmp_value - 0.5) * 100
    print("   Temperature =", tmp_value)
    time.sleep(1)
