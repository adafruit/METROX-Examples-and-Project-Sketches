# CIRC07 - Button Pressing make it better pwm
# (CircuitPython)                                                                                  
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com    
                                                                                                    
# by Limor Fried/Ladyada for Adafruit Industries.                                                   

import digitalio
import board
import pulseio
import time        
                   
led = pulseio.PWMOut(board.D9)   
button1 = digitalio.DigitalInOut(board.D2)                 
button1.switch_to_input()
button2 = digitalio.DigitalInOut(board.D3)                 
button1.switch_to_input()
                   
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
