"""
'8_more_leds.py'.

=================================================
LED light show with a 74HC595 shift register
"""

import time
import board
import digitalio


DATA = digitalio.DigitalInOut(board.d2)
DATA.switch_to_output()
CLK = digitalio.DigitalInOut(board.d3)
CLK.switch_to_output()
LATCH = digitalio.DigitalInOut(board.d4)
LATCH.switch_to_output()

LED_STATE = 0
BITS = [0b00000001, 0b00000010, 0b00000100, 0b00001000,
        0b00010000, 0b00100000, 0b01000000, 0b10000000]
MASKS = [0b11111110, 0b11111101, 0b11111011, 0b11110111,
         0b11101111, 0b11011111, 0b10111111, 0b01111111]


def update_leds(leds):
    """updates the LED state."""
    LATCH.value = False
    for bit in range(8):
        if leds & (1 << bit):
            DATA.value = True
        else:
            DATA.value = False
        CLK.value = True
        CLK.value = False
    LATCH.value = True


def update_leds_long(value):
    """uses bitmasking to update LEDs."""
    LATCH.value = False
    val = value
    # repeat once for each bit
    for _ in range(8):
        # use bitmask to select only the eighth bit in number
        bit = val & 0b10000000
        val <<= 1
        if bit == 128:
            DATA.value = True
        else:
            DATA.value = False
        CLK.value = True
        time.sleep(.01)
        CLK.value = False
    LATCH.value = True


def change_led(led, state):
    """changes the LED's state."""
    global LED_STATE
    LED_STATE = LED_STATE & MASKS[led]
    if state:
        LED_STATE = LED_STATE | BITS[led]
        # print(LED_STATE)
    update_leds(LED_STATE)


while True:
    change_led(3, True)
    for j in range(0, 256, 1):
        update_leds(j)
        time.sleep(0.4)
