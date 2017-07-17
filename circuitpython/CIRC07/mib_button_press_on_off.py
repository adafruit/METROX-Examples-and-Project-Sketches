import digitalio
from board import *
import time

led = DigitalInOut(D13)                    
led.switch_to_output()
button1 = DigitalInOut(D2)
button1.switch_to_input()
button2 = DigitalInOut(D3)
button2.switch_to_input()

while True:        
    if not button1.value:
        led.value = False
    elif not button2.value:
        led.value = True
