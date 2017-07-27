# CIRC13 - Squeezing
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries

import board
import pulseio 
import analogio

squeeze = analogio.AnalogIn(board.A2)
led = pulseio.PWMOut(board.D9)

# loop forever
while True:
    # set brightness of LED to value of FSR
    led.duty_cycle = squeeze.value
