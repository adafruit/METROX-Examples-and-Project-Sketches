import digitalio   
import analogio    
import pulseio     
from board import *
import time        
                   
servoPin = D9      
servo = pulseio.PWMOut(servoPin, frequency=50)                                             
servoMin = 0.2     
servoMax = 2.25    
                   
potPin = A0        
pot = analogio.AnalogIn(potPin)            
                   
def servoAngle(angle):                     
    angle = min(180, angle)                
    angle = max(0, angle)                  
    # range is 0 - 20ms                    
    pulsewidth = servoMin + (angle / 180)*(servoMax-servoMin)                              
    duty_percent = pulsewidth / 20.0       
    servo.duty_cycle = int(duty_percent * 65535)                                           
                   
def servoSweep():  
    for a in range(0,180,1):               
        servoAngle(a)                      
        time.sleep(0.01)                   
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
