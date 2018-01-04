"""
'colorful_light.py'.

=================================================
RGB LED control with circuitpython
"""

import board
import digitalio

redLED = digitalio.DigitalInOut(board.D9)
greenLED = digitalio.DigitalInOut(board.D10)
blueLED = digitalio.DigitalInOut(board.D11)

RGBLED = [redLED, greenLED, blueLED]
RED = [True, False, False]
GREEN = [False, True, False]
BLUE = [False, False, True]
YELLOW = [True, True, False]
CYAN = [False, True, True]
MAGENTA = [True, False, True]
WHITE = [True, True, True]
BLACK = [False, False, False]
colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE, BLACK]

for led in RGBLED:
    led.switch_to_output()


def setColor(color):
    RGBLED[0].value = not color[0]
    RGBLED[1].value = not color[1]
    RGBLED[2].value = not color[2]


while True:
    setColor(GREEN)
