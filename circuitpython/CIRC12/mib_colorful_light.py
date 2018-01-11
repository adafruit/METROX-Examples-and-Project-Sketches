"""
'mib_colorful_light.py'.

=================================================
RGB LED control with circuitpython
requires:
-simpleio
"""
import random
import board
import pulseio
from simpleio import map_range

RED_LED = pulseio.PWMOut(board.D9)
GREEN_LED = pulseio.PWMOut(board.D10)
BLUE_LED = pulseio.PWMOut(board.D11)

RGB_LED_ARR = [RED_LED, GREEN_LED, BLUE_LED]

RED = [100, 0, 0]
ORANGE = [50, 5, 0]
YELLOW = [100, 100, 0]
GREEN = [0, 100, 0]
TEAL = [0, 50, 5]
CYAN = [0, 100, 100]
BLUE = [0, 0, 100]
MAGENTA = [100, 0, 100]
WHITE = [100, 100, 100]
BLACK = [0, 0, 0]

COLOR_ARR = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, CYAN, MAGENTA, WHITE, BLACK]


def set_color(color):
    """sets the rgb led's cathodes."""
    print("Setting (%0.2f, %0.2f, %0.2f)" % (color[0], color[1], color[2]))
    RGB_LED_ARR[0].duty_cycle = int(map_range(color[0], 0, 100, 65535, 0))
    RGB_LED_ARR[1].duty_cycle = int(map_range(color[1], 0, 100, 65535, 0))
    RGB_LED_ARR[2].duty_cycle = int(map_range(color[2], 0, 100, 65535, 0))


def random_color():
    """generates a random color."""
    rnd_color = random.randrange(len(COLOR_ARR))
    set_color(COLOR_ARR[rnd_color])

while True:
    set_color(GREEN)
