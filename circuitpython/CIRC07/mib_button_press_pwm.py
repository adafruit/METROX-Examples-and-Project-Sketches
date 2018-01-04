"""
'mib_button_press_pwm.py'.

=================================================
fade a LED in and out using two buttons
"""

import digitalio
import board
import pulseio
import time

led = pulseio.PWMOut(board.D13)
button1 = digitalio.DigitalInOut(board.D3)
button1.switch_to_input()
button2 = digitalio.DigitalInOut(board.D2)
button1.switch_to_input()


while True:
    brightness = led.duty_cycle
    # If button
    if not button1.value:
        brightness += 100
    if not button2.value:
        brightness -= 100
    brightness = max(0, brightness)
    brightness = min(44000, brightness)
    led.duty_cycle = brightness
    time.sleep(0.001)
