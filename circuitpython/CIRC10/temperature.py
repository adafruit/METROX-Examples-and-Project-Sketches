# CIRC10 - Temperature
# (Circuit Python)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada and Asher Lieber for Adafruit Industries.

import board
import analogio
import time
from simpleio import map_range

sensor = analogio.AnalogIn(board.A0)

def getVoltage(p_sensor):
    # map value from photo sensor to voltage
    v = map_range(p_sensor.value, 0, 65535, 0, 3.3)
    return v

# loop forever
while True:
    temp = getVoltage(sensor)
    print("Voltage =", temp, end="")
    # convert to celsius
    temp = (temp - 0.5) * 100
    print("   Temperature =", temp)
    time.sleep(0.1)
