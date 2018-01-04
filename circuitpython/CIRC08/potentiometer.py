"""
'potentiometer.py'.

=================================================
control a LED's brightness using a potentiometer
"""
import digitalio
import analogio
import time
import board

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
pot = analogio.AnalogIn(board.A0)

sensorval = 0

while True:
    # potentiometer value/max potentiometer value
    sensorval = pot.value / 65536
    print(sensorval)
    led.value = True
    time.sleep(sensorval)
    led.value = False
    time.sleep(sensorval)
