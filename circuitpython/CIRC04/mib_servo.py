# CIRC04 - A Single Servo make it better
# (Circuit Python)                                                                                             
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com               
                                                                                                               
# by Limor Fried/Ladyada for Adafruit Industries.                                                              

# import required libraries
import analogio    
import pulseio
import board
import time

servoPin = board.D9
servo = pulseio.PWMOut(servoPin, frequency=50)
servoMin = 0.2
servoMax = 2.25

potPin = board.A0
pot = analogio.AnalogIn(potPin)

def servoAngle(angle):
    # make sure angle isn't above 180 or below 0
    angle = min(180, angle)
    angle = max(0, angle)
    # range is 0 - 20ms
    pulsewidth = servoMin + (angle / 180)*(servoMax-servoMin)
    duty_percent = pulsewidth / 20.0
    servo.duty_cycle = int(duty_percent * 65535)

def servoSweep():
    # iterate from 0-180, setting the servo angle to each number
    for a in range(0,180,1):
        servoAngle(a)
        time.sleep(0.01)
    # iterate from 180-0
    for a in range(180,0,-1):
        servoAngle(a)
        time.sleep(0.01)

def potSweep():
    val = pot.value / 65536
    print("Pot =", val)
    servoAngle(180 * val)
    time.sleep(0.05)

while True:
    #servoSweep()
    potSweep()
