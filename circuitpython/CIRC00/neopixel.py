# CIRC00 -  Metro Express NeoPixel
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

# import required libraries
import neopixel
import board
import time

# we only have one neopixel on our metro express
neo = neopixel.NeoPixel(board.NEOPIXEL, 1)

# primary colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors = [red, green, blue]

# red, green, blue
for i in colors:
    neo[0] = i
    neo.write()
    time.sleep(.3)

# shows all colors by trying all combinations of RGB levels
for red_level in range(0, 256, 100):
    for green_level in range(0, 256, 100):
        for blue_level in range(0, 256, 100):
            print(red_level, green_level, blue_level)
            neo[0] = (red_level, green_level, blue_level)
            neo.write()
            # wait 0.2 seconds to give us time to see the colors
            time.sleep(.2)
# flashing white light
for i in range(100):
    # bright white light
    neo[0] = (255, 255, 255) 
    neo.write()
    time.sleep(.05)
    # off
    neo[0] = (0, 0, 0)
    neo.write()
    time.sleep(.05)
neo[0] = (0,0,0)
neo.write()
