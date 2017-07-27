# CIRC03 - Spin Motor Spin
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries.

# import required libraries
import digitalio                                            
import pulseio                                              
import board
import time                                                 
                                                            
motorPin = board.D9                                               
                                                            
motor = digitalio.DigitalInOut(motorPin)                    
# switch motor to output mode
motor.switch_to_output()                                    
                                                            
def motorOnThenOff():                                       
    onTime = 2.5                                            
    offTime = 1.0                                           
    motor.value = True                                      
    # wait for onTime seconds
    time.sleep(onTime)                                      
    motor.value = False                                     
    # wait for offTime seconds
    time.sleep(offTime)                                     
                                                            
# run this forever
while True:                                                 
    motorOnThenOff()
