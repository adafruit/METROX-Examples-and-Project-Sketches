"""
'8_more_leds.py'.

=================================================
LED light show with a 74HC595 shift register
"""

import board
import digitalio
import time

dataPin = board.D2
clockPin = board.D3
latchPin = board.D4

data = digitalio.DigitalInOut(dataPin)
data.switch_to_output()
clock = digitalio.DigitalInOut(clockPin)
clock.switch_to_output()
latch = digitalio.DigitalInOut(latchPin)
latch.switch_to_output()

led_state = 0
bits = [0b00000001, 0b00000010, 0b00000100, 0b00001000,
        0b00010000, 0b00100000, 0b01000000, 0b10000000]
masks = [0b11111110, 0b11111101, 0b11111011, 0b11110111,
         0b11101111, 0b11011111, 0b10111111, 0b01111111]


def updateLEDs(leds):
    latch.value = False
    for bit in range(8):
        if (leds & (1 << bit)):
            data.value = True
        else:
            data.value = False
        clock.value = True
        clock.value = False
    latch.value = True


def updateLEDsLong(value):
    latch.value = False
    val = value
    # repeat once for each bit
    for i in range(8):
        # use bitmask to select only the eightth bit in number
        bit = val & 0b10000000
        # val = val << 1
        val <<= 1

        if bit == 128:
            data.value = True
        else:
            data.value = False
        clock.value = True
        time.sleep(.01)
        clock.value = False
    latch.value = True


def changeLed(led, state):
    global led_state
    led_state = led_state & masks[led]
    if state:
        led_state = led_state | bits[led]
        # print(led_state)
    updateLEDs(led_state)


while True:
    changeLed(3, True)
    for i in range(0, 256, 1):
        updateLEDs(i)
        time.sleep(0.4)
