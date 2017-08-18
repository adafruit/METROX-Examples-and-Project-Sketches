# PROJ01 - Theremin
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import board
import analogio 
import pulseio
from simpleio import map_range

piezo = pulseio.PWMOut(board.D9)
photo = analogio.AnalogIn(board.A0)

while True:
    # map photo sensor value to hearable sound on piezo
    val = int(map_range(photo.value, 0, 65520, 1000, 64000))
    piezo.duty_cycle = val 
