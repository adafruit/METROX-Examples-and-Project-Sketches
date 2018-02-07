"""
'servo.py'.

=================================================
move a hobby servo (towerpro sg92r) w/ 3-wire interface
requires:
- Adafruit_CircuitPython_Motor
"""
import time
import board
import pulseio
from adafruit_motor import servo

servo = servo.Servo(pulseio.PWMOut(board.D9))


while True:
    servo.angle = 0
    time.sleep(2)
    servo.angle = 90
    time.sleep(2)
