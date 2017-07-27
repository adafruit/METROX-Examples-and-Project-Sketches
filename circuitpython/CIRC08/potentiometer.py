# CIRC08 - Twisting
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Limor Fried/Ladyada for Adafruit Industries.

import digitalio
import analogio
import board
import time

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
pot = analogio.AnalogIn(A0)

sensorval = 0

while True:
    # potentiometer value/max potentiometer value
    sensorval = pot.value / 65536
    print(sensorval)
    led.value = True
    time.sleep(sensorval)
    led.value = False
    time.sleep(sensorval)
