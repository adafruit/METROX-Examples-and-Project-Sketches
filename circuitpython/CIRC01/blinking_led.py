"""
'blinking_led.py'.

=================================================
blinks a led using digitalio
"""
import digitalio
import board
import time

# create a DigitalInOut object
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
