"""
'mib_potentiometer_threshold.py'.

=================================================
turns on a LED when the potentiometer is above a half-turn
"""
import analogio
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
pot = analogio.AnalogIn(board.A0)

threshold = 10000

while True:
    if pot.value > threshold:
        led.value = True
    else:
        led.value = False
