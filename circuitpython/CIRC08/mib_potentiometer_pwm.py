"""
'mib_potentiometer_pwm.py'.

=================================================
fades a LED using a potentiometer
"""

import analogio
import board
import pulseio

LED = pulseio.PWMOut(board.D9)
POT = analogio.AnalogIn(board.A0)

while True:
    LED.duty_cycle = POT.value
