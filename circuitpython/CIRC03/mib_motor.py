"""
'mib_motor.py'.

=================================================
spins a DC motor using pulseio
"""

import board
import pulseio
import time

motorPin = board.D9
motor = pulseio.PWMOut(motorPin, frequency=1000)


def motorOnThenOffwithSpeed():
    onSpeed = 0.80
    onTime = 2.5
    offSpeed = 0.10
    offTime = 1.0
    motor.duty_cycle = int(onSpeed * 65535)
    time.sleep(onTime)
    motor.duty_cycle = int(offSpeed * 65535)
    time.sleep(offTime)


def motorAcceleration():
    delayTime = 0.05
    for speed in range(0, 100, 1):
        motor.duty_cycle = int(speed / 100 * 65535)
        time.sleep(delayTime)
    for speed in range(100, 0, -1):
        motor.duty_cycle = int(speed / 100 * 65535)
        time.sleep(delayTime)


while True:
    motorOnThenOffwithSpeed()
    # motorAcceleration()
