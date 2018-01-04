# CIRC10 - Temperature Alarm
# (Circuit Python)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import analogio
import pulseio
import board
import time
from simpleio import map_range

piezo = pulseio.PWMOut(board.D8, frequency = 440, duty_cycle = 0, variable_frequency = True)
temp = analogio.AnalogIn(board.A0)

freezing_temp = 0 
boiling_temp = 100

while True:
    temperature = map_range(temp.value, 0, 65535, 0, 5)
    # temp to degrees C
    temperature = (temperature - .5) * 100
    print(temperature)

    if temperature < freezing_temp:
        piezo.duty_cycle = 30000
    if temperature > boiling_temp:
        piezo.duty_cycle = 10000
    time.sleep(.5)
