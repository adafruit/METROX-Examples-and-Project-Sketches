# CIRC03 - Blinking LED make it better
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com 

# by Limor Fried/Ladyada for Adafruit Industries.

# import required libraries
import digitalio                                        
import pulseio                                          
import board
import time                                             
                                                        
motorPin = board.D9                                           
motor = pulseio.PWMOut(motorPin, frequency=1000)
                                                        
def motorOnThenOffwithSpeed():
    # 80%
    onSpeed = 0.80
    onTime = 2.5
    # 10%
    offSpeed = 0.10
    offTime = 1.0
    motor.duty_cycle = int(onSpeed * 65535)
    time.sleep(onTime)
    motor.duty_cycle = int(offSpeed * 65535)
    time.sleep(offTime)

def motorAcceleration():
    # seconds between each speed step
    delayTime = 0.05

    # Accelerates the motor                             
    for speed in range(0, 100, 1):
        motor.duty_cycle = int(speed / 100 * 65535)
        time.sleep(delayTime)         

    # Decelerates the motor                             
    for speed in range(100, 0, -1):
        motor.duty_cycle = int(speed / 100 * 65535)
        time.sleep(delayTime)         
                                                        
while True:
    motorOnThenOffwithSpeed()        
    #motorAcceleration()
