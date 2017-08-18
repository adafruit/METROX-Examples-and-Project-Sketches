# CIRC18 - Adding USB Control
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries

from adafruit_hid import mouse
import analogio
import digitalio
import board
import time
from simpleio import map_range

button = digitalio.DigitalInOut(board.D6)
pot = analogio.AnalogIn(board.A0)

m = mouse.Mouse()

while True:
    if not button.value: # move while button is pressed
    # if button.value: # stop moving when button is pressed
        #maps potentiometer value to mouse scroll value
        m.move(0, 0, int(map_range(pot.value, 50, 65520, -5, 5)))
        time.sleep(.08)
