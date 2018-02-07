"""
'button_press.py'.

=================================================
push the button and light up a led
"""
import digitalio
import board

led = digitalio.DigitalInOut(board.D13)
button = digitalio.DigitalInOut(board.D2)
led.switch_to_output()
button.switch_to_input()


while True:
    btn_state = button.value
    led.value = not btn_state
