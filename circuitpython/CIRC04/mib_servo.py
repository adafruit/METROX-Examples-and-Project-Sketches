"""
'mib_servo.py'.

=================================================
controls a servo with a potentiometer
requires:
- simpleio library
"""

import analogio
import board
import time
from simpleio import Servo

servo = Servo(board.D9)
potPin = board.A0
pot = analogio.AnalogIn(potPin)


def servoSweep():
    for a in range(0, 180, 1):
        servo.angle = a
        time.sleep(0.01)
    for a in range(180, 0, -1):
        servo.angle = a
        time.sleep(0.01)


def potSweep():
    val = pot.value / 65536
    servo.angle = 180 * val
    time.sleep(0.05)


while True:
    # servoSweep()
    potSweep()
