"""
'mib_photo_sensor_night_light.py'.

=================================================
turns off and on a LED using a photo sensor
"""

import analogio
import board
import digitalio

THRESHOLD = 60000

LED = digitalio.DigitalInOut(board.D9)
LED.switch_to_output()
LIGHT = analogio.AnalogIn(board.A0)


while True:
    if LIGHT.value > THRESHOLD:
        LED.value = True
    else:
        LED.value = False
