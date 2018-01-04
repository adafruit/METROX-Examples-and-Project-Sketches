"""
'photo_sensor.py'.

=================================================
uses light to control a LED
"""
import analogio
import board
import pulseio
from simpleio import map_range

led = pulseio.PWMOut(board.D9)
light = analogio.AnalogIn(board.A0)


while True:
    mapped = map_range(light.value, 20000, 32766, 0, 32766)
    led.duty_cycle = int(mapped)
