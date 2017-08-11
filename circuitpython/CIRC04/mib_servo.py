# CIRC04 - A Single Servo make it better
# (Circuit Python)                                                                                             
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com               
                                                                                                               
# by Limor Fried/Ladyada for Adafruit Industries.                                                              

# import required libraries
import analogio    
import pulseio
import board
import time
from simpleio import Servo

servo = Servo(board.D9)

potPin = board.A0
pot = analogio.AnalogIn(potPin)

def servoSweep():
    # iterate from 0-180, setting the servo angle to each number
    for a in range(0,180,1):
        servo.set_angle(a)
        time.sleep(0.01)
    # iterate from 180-0
    for a in range(180,0,-1):
        servo.set_angle(a)
        time.sleep(0.01)

def potSweep():
    val = pot.value / 65536
    print("Pot =", val)
    servo.set_angle(180 * val)
    time.sleep(0.05)

while True:
    # servoSweep()
    potSweep()
