# CIRC12 - Colorful Light
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries

import digitalio
import pulseio
import board
import time

redLED = digitalio.DigitalInOut(board.D9)
greenLED = digitalio.DigitalInOut(board.D10)
blueLED = digitalio.DigitalInOut(board.D11)

RGBLED = [redLED, greenLED, blueLED]
# only red
RED     = [True, False, False]
# only green
GREEN   = [False, True, False]
# only blue
BLUE    = [False, False, True]
# red+green
YELLOW  = [True, True, False]
# green+blue
CYAN    = [False, True, True]
# red+blue
MAGENTA = [True, False, True]
# all on
WHITE   = [True, True, True]
# all off
BLACK   = [False, False, False]

colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE, BLACK]

# switch to output
for led in RGBLED:
    led.switch_to_output()

def setColor(color):
    RGBLED[0].value = not color[0]
    RGBLED[1].value = not color[1]
    RGBLED[2].value = not color[2]

setColor(GREEN)
