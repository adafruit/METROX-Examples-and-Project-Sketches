# CIRC04 - A Single Servo
# (Circuit Python) 
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com 

# by Limor Fried/Ladyada for Adafruit Industries.

# import required libraries
import digitalio
import pulseio
import board
import time
from simpleio import Servo

servo = Servo(board.D9)

while True:
    servo.set_angle(0)
    time.sleep(1)
    servo.set_angle(90)
    time.sleep(1)
    servo.set_angle(180)
    time.sleep(1)
