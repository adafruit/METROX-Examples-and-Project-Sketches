"""
'8_leds.py'.

=================================================
lights up 8 leds with different animations
"""

import board
import digitalio
import time

# create a list of DigitalInOut objects using pins 2-9
ledpins = [digitalio.DigitalInOut(board.D2),
           digitalio.DigitalInOut(board.D3),
           digitalio.DigitalInOut(board.D4),
           digitalio.DigitalInOut(board.D5),
           digitalio.DigitalInOut(board.D6),
           digitalio.DigitalInOut(board.D7),
           digitalio.DigitalInOut(board.D8),
           digitalio.DigitalInOut(board.D9)]

for pin in ledpins:
    pin.switch_to_output()


def oneAfterAnotherNoLoop():
    delayTime = 0.1

    ledpins[0].value = True
    time.sleep(delayTime)
    ledpins[1].value = True
    time.sleep(delayTime)
    ledpins[2].value = True
    time.sleep(delayTime)
    ledpins[3].value = True
    time.sleep(delayTime)
    ledpins[4].value = True
    time.sleep(delayTime)
    ledpins[5].value = True
    time.sleep(delayTime)
    ledpins[6].value = True
    time.sleep(delayTime)
    ledpins[7].value = True
    time.sleep(delayTime)

    ledpins[7].value = False
    time.sleep(delayTime)
    ledpins[6].value = False
    time.sleep(delayTime)
    ledpins[5].value = False
    time.sleep(delayTime)
    ledpins[4].value = False
    time.sleep(delayTime)
    ledpins[3].value = False
    time.sleep(delayTime)
    ledpins[2].value = False
    time.sleep(delayTime)
    ledpins[1].value = False
    time.sleep(delayTime)
    ledpins[0].value = False
    time.sleep(delayTime)


def oneAfterAnotherLoop():
    delayTime = 0.1
    for led in ledpins:
        led.value = True
        time.sleep(delayTime)
    for led in ledpins[::-1]:
        led.value = False
        time.sleep(delayTime)


def oneOnAtATime():
    delayTime = 0.1
    ledArrayLength = len(ledpins)
    for i in range(10 * ledArrayLength):
        j = i % ledArrayLength
        ledpins[j].value = True
        time.sleep(delayTime)
        ledpins[j].value = False


def inAndOut():
    delayTime = 0.1
    for i in range(3):
        offLED = i - 1
        if i == 0:
            offLED = 3
        onLED1 = 3 - i
        onLED2 = 4 + i
        offLED1 = 3 - offLED
        offLED2 = 4 + offLED
        ledpins[onLED1].value = True
        ledpins[onLED2].value = True
        ledpins[offLED1].value = False
        ledpins[offLED2].value = False
        time.sleep(delayTime)
    for i in range(3):
        i = 3 - i
        offLED = i + 1
        if i == 3:
            offLED = 0
        onLED1 = 3 - i
        onLED2 = 4 + i
        offLED1 = 3 - offLED
        offLED2 = 4 + offLED
        ledpins[onLED1].value = True
        ledpins[onLED2].value = True
        ledpins[offLED1].value = False
        ledpins[offLED2].value = False
        time.sleep(delayTime)


while True:
    # oneAfterAnotherNoLoop()
    # oneAfterAnotherLoop()
    # oneOnAtATime()
    inAndOut()
