"""
'mib_photo_sensor_night_light_sensor.py'.

=================================================
turns off and on a led using a photo sensor
"""

import analogio
import board
import digitalio

led = digitalio.DigitalInOut(board.D9)
light_sensor = analogio.AnalogIn(board.A0)
led.switch_to_output()

threshold_value = 60000


while True:
    if light_sensor.value > threshold_value:
        led.value = True
    else:
        led.value = False
