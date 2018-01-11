"""
'eight_leds.py'.

=================================================
lights up 8 leds with different animations
"""
import time
import board
import digitalio

LEDPINS = [digitalio.DigitalInOut(board.D2),
           digitalio.DigitalInOut(board.D3),
           digitalio.DigitalInOut(board.D4),
           digitalio.DigitalInOut(board.D5),
           digitalio.DigitalInOut(board.D6),
           digitalio.DigitalInOut(board.D7),
           digitalio.DigitalInOut(board.D8),
           digitalio.DigitalInOut(board.D9)]

for pin in LEDPINS:
    pin.switch_to_output()

def one_after_another_no_loop():
    """turns one LED on at a time, not looping at the end."""
    delay_time = 0.1
    LEDPINS[0].value = True
    time.sleep(delay_time)
    LEDPINS[1].value = True
    time.sleep(delay_time)
    LEDPINS[2].value = True
    time.sleep(delay_time)
    LEDPINS[3].value = True
    time.sleep(delay_time)
    LEDPINS[4].value = True
    time.sleep(delay_time)
    LEDPINS[5].value = True
    time.sleep(delay_time)
    LEDPINS[6].value = True
    time.sleep(delay_time)
    LEDPINS[7].value = True
    time.sleep(delay_time)

    LEDPINS[7].value = False
    time.sleep(delay_time)
    LEDPINS[6].value = False
    time.sleep(delay_time)
    LEDPINS[5].value = False
    time.sleep(delay_time)
    LEDPINS[4].value = False
    time.sleep(delay_time)
    LEDPINS[3].value = False
    time.sleep(delay_time)
    LEDPINS[2].value = False
    time.sleep(delay_time)
    LEDPINS[1].value = False
    time.sleep(delay_time)
    LEDPINS[0].value = False
    time.sleep(delay_time)


def one_after_another_loop():
    """turns one LED on at a time, looping at the end."""
    delay_time = 0.1
    for led in LEDPINS:
        led.value = True
        time.sleep(delay_time)
    for led in LEDPINS[::-1]:
        led.value = False
        time.sleep(delay_time)


def one_on_at_a_time():
    """turns one LED on at a time, looping at the end."""
    delay_time = 0.1
    led_array_length = len(LEDPINS)
    for i in range(10 * led_array_length):
        j = i % led_array_length
        LEDPINS[j].value = True
        time.sleep(delay_time)
        LEDPINS[j].value = False


def in_and_out():
    """fades the LEDs in and out."""
    delay_time = 0.1
    for i in range(3):
        off_led = i - 1
        if i == 0:
            off_led = 3
        on_led_1 = 3 - i
        on_led_2 = 4 + i
        off_led1 = 3 - off_led
        off_led2 = 4 + off_led
        delay_time = 0.1
        for pin_range in LEDPINS:
            for _ in range(10):
                pin_range.value = True
                time.sleep(delay_time)
                pin_range.value = False
    for i in range(3):
        i = 3 - i
        off_led = i + 1
        if i == 3:
            off_led = 0
        on_led_1 = 3 - i
        on_led_2 = 4 + i
        off_led1 = 3 - off_led
        off_led2 = 4 + off_led
        LEDPINS[on_led_1].value = True
        LEDPINS[on_led_2].value = True
        LEDPINS[off_led1].value = False
        LEDPINS[off_led2].value = False
        time.sleep(delay_time)


while True:
    # one_after_another_no_loop()
    # one_after_another_loop()
    # one_on_at_a_time()
    in_and_out()
