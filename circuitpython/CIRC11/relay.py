# CIRC11 - Large Loads With Relays
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import board
import digitalio
import time

# set up the relay as an output
relay = digitalio.DigitalInOut(board.D2)
relay.switch_to_output()

while True:
    # toggle the value of the relay
    relay.value = not relay.value
    time.sleep(1)
