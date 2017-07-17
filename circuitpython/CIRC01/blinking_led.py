# CIRC01 - Blinking LED
# (Circuit Python)

import digitalio
import board
import time

led = digitalio.DigitalInOut(board.D13)
# LED pin should be used as an output 
led.switch_to_output()

while True:
    # turn LED ON
    led.value = True
    # wait 1 second
    time.sleep(1.0)
    # turn LED off
    led.value = False
    # wait 1 second
    time.sleep(1.0)
