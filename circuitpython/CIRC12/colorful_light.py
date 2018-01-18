"""
'colorful_light.py'.

=================================================
RGB LED control with circuitpython
"""

import board
import digitalio

RED_LED = digitalio.DigitalInOut(board.D9)
GREEN_LED = digitalio.DigitalInOut(board.D10)
BLUE_LED = digitalio.DigitalInOut(board.D11)

RGBLED = [RED_LED, GREEN_LED, BLUE_LED]
RED = [True, False, False]
GREEN = [False, True, False]
BLUE = [False, False, True]
YELLOW = [True, True, False]
CYAN = [False, True, True]
MAGENTA = [True, False, True]
WHITE = [True, True, True]
BLACK = [False, False, False]
COLOR_ARRAY = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE, BLACK]

for led in RGBLED:
    led.switch_to_output()


def set_color(color):
    """sets the rgb led's cathode value."""
    RGBLED[0].value = not color[0]
    RGBLED[1].value = not color[1]
    RGBLED[2].value = not color[2]


while True:
    set_color(GREEN)
