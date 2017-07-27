# CIRC08 - Twisting make it better pwm 
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries.

import digitalio
import analogio
import board
import pulseio
import time

led = pulseio.PWMOut(board.D9)
pot = analogio.AnalogIn(board.A0)

while True:
    led.duty_cycle = pot.value
