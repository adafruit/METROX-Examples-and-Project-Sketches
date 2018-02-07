"""
'motor.py'.

=================================================
spin a DC motor using digitalio
"""

import time
import board
import digitalio

motor = digitalio.DigitalInOut(board.D9)
motor.switch_to_output()


def motor_on_then_off():
    """toggles the motor."""
    on_time = 2.5
    off_time = 1.0
    motor.value = True
    time.sleep(on_time)
    motor.value = False
    time.sleep(off_time)


while True:
    motor_on_then_off()
