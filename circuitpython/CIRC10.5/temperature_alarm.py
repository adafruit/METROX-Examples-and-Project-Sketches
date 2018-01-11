"""
'temperature_alarm.py'.

=================================================
sounds an alarm when the temperature crosses a threshold
requires:
- simpleio
"""

import time
import analogio
import pulseio
import board
from simpleio import map_range

piezo = pulseio.PWMOut(board.D8, frequency=440, duty_cycle=0, variable_frequency=True)
TMP_36 = analogio.AnalogIn(board.A0)

freezing_temp = 0
boiling_temp = 100

while True:
    temperature = map_range(TMP_36.value, 0, 65535, 0, 5)
    # temp to degrees C
    temperature = (temperature - .5) * 100
    print(temperature)

    if temperature < freezing_temp:
        piezo.duty_cycle = 30000
    if temperature > boiling_temp:
        piezo.duty_cycle = 10000
    time.sleep(.5)
