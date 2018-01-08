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

redLED = pulseio.PWMOut(board.D9)
greenLED = pulseio.PWMOut(board.D10)
blueLED = pulseio.PWMOut(board.D11)

RGBLED = [redLED, greenLED, blueLED]

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

colors = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, CYAN, MAGENTA, WHITE, BLACK]


def setColor(color):
    """sets the rgb led's cathodes."""
    print("Setting (%0.2f, %0.2f, %0.2f)" % (color[0], color[1], color[2]))
    RGBLED[0].duty_cycle = int(map_range(color[0], 0, 100, 65535, 0))
    RGBLED[1].duty_cycle = int(map_range(color[1], 0, 100, 65535, 0))
    RGBLED[2].duty_cycle = int(map_range(color[2], 0, 100, 65535, 0))


def randomColor():
    """generates a random color."""
    c = random.randrange(len(colors))
    setColor(colors[c])


setColor(GREEN)
