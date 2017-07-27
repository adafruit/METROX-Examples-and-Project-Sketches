# CIRC12 - Colorful Light make it better
# (Circuit Python)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries

import digitalio
import pulseio
import board
import time
import urandom

# works: D4
redLED = pulseio.PWMOut(board.D3)
greenLED = pulseio.PWMOut(board.D4)
blueLED = pulseio.PWMOut(board.D5)

RGBLED = [redLED, greenLED, blueLED]

# only red
RED     = [100, 0,   0]
ORANGE  = [50,  5,   0]
# red+green
YELLOW  = [100, 100, 0]
# only green
GREEN   = [0,   100, 0]
TEAL    = [0,   50,  5]
# green+blue
CYAN    = [0,   100, 100]
# only blue
BLUE    = [0,   0,   100]
# red+blue
MAGENTA = [100, 0,   100]
# all on
WHITE   = [100, 100, 100]
# all off
BLACK   = [0,   0,   0]

colors = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, CYAN, MAGENTA, WHITE, BLACK]

# affine transfer/map with constrained output
def _map(x, in_min, in_max, out_min, out_max):
    outrange = float(out_max - out_min)
    inrange = float(in_max - in_min)
    ret = (x - in_min) * (outrange / inrange) + out_min
    if (out_max > out_min):
        return max(min(ret, out_max), out_min)
    else:
        return max(min(ret, out_min), out_max)

def setColor(color):
    print("Setting (%0.2f, %0.2f, %0.2f)" % (color[0], color[1], color[2]))
    RGBLED[0].duty_cycle = int(_map(color[0], 0, 100, 65535, 0))
    RGBLED[1].duty_cycle = int(_map(color[1], 0, 100, 65535, 0))
    RGBLED[2].duty_cycle = int(_map(color[2], 0, 100, 65535, 0))

def randomColor():
    c = urandom.randrange(len(colors))
    setColor(colors[c])

# loop forever
while True:
    #randomColor()
    for color in colors:
        setColor(color)
        time.sleep(0.5)
