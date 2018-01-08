"""
'servo.py'.

=================================================
controls a servo using simpleio's servo method
requires:
- simpleio library
"""

import time
import simpleio
import board

myServo = simpleio.Servo(board.D9)

while True:
    myServo.angle = 0
    print("Angle: ", myServo.angle)
    time.sleep(2)
    myServo.angle = myServo.microseconds_to_angle(2500)
    print("Angle: ", myServo.angle)
    time.sleep(2)
