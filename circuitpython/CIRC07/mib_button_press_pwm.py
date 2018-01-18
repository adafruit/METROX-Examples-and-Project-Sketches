"""
'mib_button_press_pwm.py'.

=================================================
fade a LED in and out using two buttons
"""
import time
import digitalio
import board
import pulseio


LED = pulseio.PWMOut(board.D13)
BUTTON1 = digitalio.DigitalInOut(board.D3)
BUTTON1.switch_to_input()
BUTTON2 = digitalio.DigitalInOut(board.D2)
BUTTON2.switch_to_input()


while True:
    BRIGHTNESS = LED.duty_cycle
    # If button
    if not BUTTON1.value:
        BRIGHTNESS += 100
    if not BUTTON2.value:
        BRIGHTNESS -= 100
    BRIGHTNESS = max(0, BRIGHTNESS)
    BRIGHTNESS = min(44000, BRIGHTNESS)
    LED.duty_cycle = BRIGHTNESS
    time.sleep(0.001)
