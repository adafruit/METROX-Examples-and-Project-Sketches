"""
'mib_potentiometer_light_thresh.py'.

=================================================
turns on a led when the potentiometer is above a half-turn
"""
import analogio
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
pot = analogio.AnalogIn(board.A0)
led.switch_to_output()

light_thresh = 10000

while True:
    if pot.value > light_thresh:
        led.value = True
    else:
        led.value = False
