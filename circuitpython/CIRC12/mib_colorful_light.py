from digitalio import *
from pulseio import *
from board import *
import time
import urandom

# works: D4
redLED = PWMOut(D3)
greenLED = PWMOut(D4)
blueLED = PWMOut(D5)

RGBLED = [redLED, greenLED, blueLED]

RED     = [100, 0,   0]   # only red
ORANGE  = [50,  5,   0]
YELLOW  = [100, 100, 0]    # red+green
GREEN   = [0,   100, 0]   # only green
TEAL    = [0,   50,  5]
CYAN    = [0,   100, 100]    # green+blue
BLUE    = [0,   0,   100]   # only blue
MAGENTA = [100, 0,   100]    # red+blue
WHITE   = [100, 100, 100]     # all on
BLACK   = [0,   0,   0]  # all off

colors = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, CYAN, MAGENTA, WHITE, BLACK]

# affine transfer/map with constrained output
def map(x, in_min, in_max, out_min, out_max):
    outrange = float(out_max - out_min)
    inrange = float(in_max - in_min)
    ret = (x - in_min) * (outrange / inrange) + out_min
    if (out_max > out_min):
        return max(min(ret, out_max), out_min)
    else:
        return max(min(ret, out_min), out_max)

def setColor(color):
    print("Setting (%0.2f, %0.2f, %0.2f)" % (color[0], color[1], color[2]))
    RGBLED[0].duty_cycle = int(map(color[0], 0, 100, 65535, 0))
    RGBLED[1].duty_cycle = int(map(color[1], 0, 100, 65535, 0))
    RGBLED[2].duty_cycle = int(map(color[2], 0, 100, 65535, 0))

def randomColor():
    c = urandom.randrange(len(colors))
    setColor(colors[c])

while True:
    #randomColor()
    for color in colors:
        setColor(color)
        time.sleep(0.5)
