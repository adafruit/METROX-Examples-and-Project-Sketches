from digitalio import *                    
from board import *
from pulseio import *                      
import time        
                   
Direction = DigitalInOut.direction         
                   
led = PWMOut(D9)   
button1 = DigitalInOut(D2)                 
button1.direction = Direction.IN           
button2 = DigitalInOut(D3)                 
button2.direction = Direction.IN           
                   
while True:        
    brightness = led.duty_cycle            
    if not button1.value:
        brightness += 100                  
    if not button2.value:
        brightness -= 100                  
    print(brightness)                      
    brightness = max(0, brightness)        
    brightness = min(44000, brightness)    
    led.duty_cycle = brightness            
    time.sleep(0.001)
