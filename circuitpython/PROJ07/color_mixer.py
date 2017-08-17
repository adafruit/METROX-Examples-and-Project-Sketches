# PROJ07 - Color Mixer
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.Com

# by Asher Lieber for Adafruit Industries

import adafruit_CircuitPython_RGB_LED as rgb
import board
import analogio
import digitalio
import time
from simpleio import map_range

but = digitalio.DigitalInOut(board.D11)
pot = analogio.AnalogIn(board.A0)

rgb_led = rgb.rgb_led(board.D10, board.D9, board.D8)

# to keep track of the color we're currently adjusting
current_color = 0
# to keep track of the current rgb levels
current_rgb = [0,0,0]
while True:
    # if button pressed
    if not but.value:
        time.sleep(.2)
        current_color += 1
        if current_color == 3:
            current_color = 0
        c_r = current_rgb
        # flash the color we're currently adjusting as an indicator
        current_rgb = [0,0,0]
        current_rgb[current_color] = 255
        rgb_led.set_color(current_rgb[0], current_rgb[1], current_rgb[2])
        # stop showing current color - show user mix
        current_rgb = c_r
        time.sleep(.2)
        print('now adjusting color ' + str(current_color))
        print('current color is:')
        print(current_rgb)
    current_rgb[current_color] = map_range(pot.value, 130, 65400, 0, 255)
    rgb_led.set_color(current_rgb[0], current_rgb[1], current_rgb[2])
