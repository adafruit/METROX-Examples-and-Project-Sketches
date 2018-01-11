"""
'BUTTON_press.py'.

=================================================
push the BUTTON and light up a LED
"""
import digitalio
import board

LED = digitalio.DigitalInOut(board.D13)
LED.switch_to_output()
BUTTON = digitalio.DigitalInOut(board.D2)
BUTTON.switch_to_input()


while True:
    BTN_VAL = BUTTON.value
    LED.value = not BTN_VAL
