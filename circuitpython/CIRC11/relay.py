"""
'relay.py'.

=================================================
drives a small relay
"""

import time
import board
import digitalio

relay = digitalio.DigitalInOut(board.D2)
relay.switch_to_output()

while True:
    relay.value = not relay.value
    time.sleep(1)
