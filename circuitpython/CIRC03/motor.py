# CIRC03 - Spin Motor Spin
# (Circuit Python)

import digitalio                                            
import pulseio                                              
from board import *                                         
import time                                                 
                                                            
motorPin = D9                                               
                                                            
motor = digitalio.DigitalInOut(motorPin)                    
motor.switch_to_output()                                    
                                                            
def motorOnThenOff():                                       
    onTime = 2.5                                            
    offTime = 1.0                                           
    motor.value = True                                      
    time.sleep(onTime)                                      
    motor.value = False                                     
    time.sleep(offTime)                                     
                                                            
while True:                                                 
    motorOnThenOff()
