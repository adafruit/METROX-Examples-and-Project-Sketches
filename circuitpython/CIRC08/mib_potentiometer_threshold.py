# CIRC08 - Twisting make it better pwm 
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries.

import board
import digitalio
import analogio

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
pot = analogio.AnalogIn(board.A0)

threshold = 10000

while True:
    if pot.value > threshold:
        led.value = True
    else:
        led.value = False
