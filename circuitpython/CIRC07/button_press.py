"""
'button_press.py'.

=================================================
push the button and light up a LED
"""
import digitalio
import board

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
button = digitalio.DigitalInOut(board.D2)
button.switch_to_input()


while True:
    val = button.value
    led.value = not val
