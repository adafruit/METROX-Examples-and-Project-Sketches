import digitalio                                        
import pulseio                                          
from board import *                                     
import time                                             
                                                        
motorPin = D9                                           
motor = pulseio.PWMOut(motorPin, frequency=1000)        
                                                        
def motorOnThenOffwithSpeed():                          
    onSpeed = 0.80  # 80%                               
    onTime = 2.5                                        
    offSpeed = 0.10  # 10%                              
    offTime = 1.0                                       
    motor.duty_cycle = int(onSpeed * 65535)             
    time.sleep(onTime)                                  
    motor.duty_cycle = int(offSpeed * 65535)            
    time.sleep(offTime)                                 
                                                        
def motorAcceleration():                                
    delayTime = 0.05  # seconds between each speed step 
                                                        
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
