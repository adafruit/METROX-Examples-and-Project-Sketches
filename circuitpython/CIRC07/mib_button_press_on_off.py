"""
'button_press_on_off.py'.

=================================================
lightswitch-like operation with two buttons and a LED
"""

import board
import digitalio

LED = digitalio.DigitalInOut(board.D13)
LED.switch_to_output()
BUTTON1 = digitalio.DigitalInOut(board.D2)
BUTTON1.switch_to_input()
BUTTON2 = digitalio.DigitalInOut(board.D3)
BUTTON2.switch_to_input()


while True:
    if not BUTTON1.value:
        LED.value = False
    elif not BUTTON2.value:
        LED.value = True
