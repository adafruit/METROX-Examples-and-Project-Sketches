"""
'button_press_on_off.py'.

=================================================
lightswitch-like operation with two buttons and a LED
"""

import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
button1 = digitalio.DigitalInOut(board.D2)
button1.switch_to_input()
button2 = digitalio.DigitalInOut(board.D3)
button2.switch_to_input()


while True:
    if not button1.value:
        led.value = False
    elif not button2.value:
        led.value = True
