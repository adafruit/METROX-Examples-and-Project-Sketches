"""
'neopixel.py'.

=================================================
control a LED with an IR Remote
"""
import board
import time
import neopixel

# we only have one neopixel on our metro express
neo = neopixel.NeoPixel(board.NEOPIXEL, 1)

# primary colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors = [red, green, blue]

# write red, green, blue into an array
for i in colors:
    neo[0] = i
    neo.write()
    time.sleep(.3)

# shows all colors by trying all combinations of RGB levels
for red_level in range(0, 256, 100):
    for green_level in range(0, 256, 100):
        for blue_level in range(0, 256, 100):
            print("red: ", red_level, "green: ",
                  green_level, "blue: ", blue_level)
            neo[0] = (red_level, green_level, blue_level)
            neo.write()
            # wait 0.2 seconds to give us time to see the colors
            time.sleep(1)
neo[0] = (0, 0, 0)
neo.write()
