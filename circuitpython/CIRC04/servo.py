# CIRC04 - A Single Servo
# (Circuit Python) 

import digitalio
import pulseio
from board import *
import time

servoPin = D9
servo = pulseio.PWMOut(servoPin, frequency=50)
servoMin = 0.5
servoMax = 2.5

def servoAngle(angle):
    angle = min(180, angle)
    angle = max(0, angle)
    print("Angle =",angle)
    # range is 0 - 20ms
    pulsewidth = servoMin + (angle / 180)*(servoMax-servoMin)
    print("Pulsewidth = ", pulsewidth)
    duty_percent = pulsewidth / 20.0
    print("duty %", duty_percent)
    servo.duty_cycle = int(duty_percent * 65535)


while True:
    servoAngle(0)
    time.sleep(1)
    servoAngle(90)
    time.sleep(1)
    servoAngle(180)
    time.sleep(1)
