"""
'mib_photo_sensor_night_light.py'.

=================================================
turns off and on a LED using a photo sensor
"""

import analogio
import board
import digitalio

threshold = 60000

led = digitalio.DigitalInOut(board.D9) led.switch_to_output()
light = analogio.AnalogIn(board.A0)


while True:
    if light.value > threshold:
        led.value = True
    else:
        led.value = False
