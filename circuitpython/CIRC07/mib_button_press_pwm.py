"""
'mib_button_press_pwm.py'.

=================================================
fade a led in and out using two buttons
"""
import time
import digitalio
import board
import pulseio


led = pulseio.PWMOut(board.D13)
btn1 = digitalio.DigitalInOut(board.D3)
btn2 = digitalio.DigitalInOut(board.D2)
btn1.switch_to_input()
btn2.switch_to_input()


while True:
    brightness = led.duty_cycle
    # If button
    if not btn1.value:
        brightness += 100
    if not btn2.value:
        brightness -= 100
    brightness = max(0, brightness)
    brightness = min(44000, brightness)
    led.duty_cycle = brightness
    time.sleep(0.001)
