"""
'blinking_LED.py'.

=================================================
blinks a LED using digitalio
"""

import time
import digitalio
import board

# create a DigitalInOut object
LED = digitalio.DigitalInOut(board.D13)
# LED pin should be used as an output
LED.switch_to_output()

while True:
    # turn LED ON
    LED.value = True
    # wait 1 second
    time.sleep(1.0)
    # turn LED off
    LED.value = False
    # wait 1 second
    time.sleep(1.0)
