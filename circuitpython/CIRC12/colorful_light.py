# CIRC12 - Colorful Light
# (Circuit Python)

from digitalio import *
from pulseio import *
from board import *
import time
Direction = DigitalInOut.direction

redLED = DigitalInOut(D9)
greenLED = DigitalInOut(D10)
blueLED = DigitalInOut(D11)

RGBLED = [redLED, greenLED, blueLED]

RED     = [True, False, False]   # only red
GREEN   = [False, True, False]   # only green
BLUE    = [False, False, True]   # only blue
YELLOW  = [True, True, False]    # red+green
CYAN    = [False, True, True]    # green+blue
MAGENTA = [True, False, True]    # red+blue
WHITE   = [True, True, True]     # all on
BLACK   = [False, False, False]  # all off

colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE, BLACK]

for led in RGBLED:
    led.direction = Direction.OUTPUT


def setColor(color):
    RGBLED[0].value = not color[0]
    RGBLED[1].value = not color[1]
    RGBLED[2].value = not color[2]

setColor(GREEN)
