"""
'squeeze.py'.

=================================================
force sensitive resistor (fsr) with circuitpython
"""

import analogio
import board
import pulseio

squeeze = analogio.AnalogIn(board.A2)
led = pulseio.PWMOut(board.D10)

while True:
    led.duty_cycle = squeeze.value
