"""
'potentiometer.py'.

=================================================
control a led's brightness using a potentiometer
"""
import time
import digitalio
import analogio
import board

led = digitalio.DigitalInOut(board.D13)
pot = analogio.AnalogIn(board.A0)
led.switch_to_output()

sensor_val = 0

while True:
    # potentiometer value/max potentiometer value
    sensor_val = pot.value / 65536
    print(sensor_val)
    led.value = True
    time.sleep(sensor_val)
    led.value = False
    time.sleep(sensor_val)
