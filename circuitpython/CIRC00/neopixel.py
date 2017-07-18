import neopixel
import board
import time

neo = neopixel.NeoPixel(board.NEOPIXEL, 1) # we only have one on our metro express

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors = [red, green, blue]

# red, green, blue
for i in colors:
    neo[0] = i
    neo.write()
    time.sleep(.3)

# shows all colors
for red_level in range(0, 256, 100):
    for green_level in range(0, 256, 100):
        for blue_level in range(0, 256, 100):
            print(red_level, green_level, blue_level)
            neo[0] = (red_level, green_level, blue_level)
            neo.write()
            time.sleep(.2)
for i in range(100):
    neo[0] = (255, 255, 255) # bright white light
    neo.write()
    time.sleep(.05)
    neo[0] = (0, 0, 0) #off
    neo.write()
    time.sleep(.05)
neo[0] = (0,0,0)
neo.write()
