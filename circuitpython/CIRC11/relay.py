# CIRC11 - Large Loads With Relays
# (Circuit Python)

from digitalio import *
from board import *
import time

relay = DigitalInOut(D2)
relay.switch_to_output()

while True:
    relay.value = not relay.value
    time.sleep(1)
