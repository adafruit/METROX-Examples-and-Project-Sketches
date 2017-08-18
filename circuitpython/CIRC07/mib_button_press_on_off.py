# CIRC07 - Button Pressing make it better on_off
# (Circuit Python)                                                                                  
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com    
                                                                                                    
# by Limor Fried/Ladyada for Adafruit Industries.                                                   

import digitalio
import board
import time

led = digitalio.DigitalInOut(board.D13)                    
led.switch_to_output()
button1 = digitalio.DigitalInOut(board.D2)
button1.switch_to_input()
button2 = digitalio.DigitalInOut(board.D3)
button2.switch_to_input()

while True:        
    if not button1.value:
        led.value = False
    elif not button2.value:
        led.value = True
