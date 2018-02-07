"""
'squeeze.py'.

=================================================
using a force sensitive resistor (fsr) with CircuitPython
"""

import analogio
import board
import pulseio

fsr = analogio.AnalogIn(board.A2)
led = pulseio.PWMOut(board.D10)

while True:
    led.duty_cycle = fsr.value
