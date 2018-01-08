"""
'rgb_ir_sensor.py'.

=================================================
control a RGB LED with an IR Remote
requires:
- adafruit_irremote library
"""

import board
import digitalio
import pulseio
import adafruit_irremote

RED = [True, False, False]
GREEN = [False, True, False]
BLUE = [False, False, True]
YELLOW = [True, True, False]
CYAN = [False, True, True]
MAGENTA = [True, False, True]
WHITE = [True, True, True]
BLACK = [False, False, False]

LEDs = [digitalio.DigitalInOut(board.D9), digitalio.DigitalInOut(board.D10),
        digitalio.DigitalInOut(board.D11)]

for i in LEDs:
    i.switch_to_output()

pulsein = pulseio.PulseIn(board.D6, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()
# size must match what you are decoding! for NEC use 4
received_code = bytearray(4)
last_code = None


def set_rgbLED_color(color):
    for i in range(len(LEDs)):
        LEDs[i].value = not color[i]


while True:
    try:
        pulses = decoder.read_pulses(pulsein)
    except MemoryError as e:
        print("Memory Error Occured: ", e)
        continue

    try:
        code = decoder.decode_bits(pulses, debug=False)
    except adafruit_irremote.IRNECRepeatException:
        print("NEC Code Repeated, doing last command")
        code = last_code
    except adafruit_irremote.IRDecodeException as e:
        print("Failed to decode: ", e)
    except MemoryError as e:
        print("Memory Error Occured: ", e)

    print(code[2])
    if code[2] == 247:
        set_rgbLED_color(RED)
    elif code[2] == 119:
        set_rgbLED_color(GREEN)
    elif code[2] == 183:
        set_rgbLED_color(BLUE)
    elif code[2] == 215:
        set_rgbLED_color(YELLOW)
    elif code[2] == 87:
        set_rgbLED_color(CYAN)
    elif code[2] == 151:
        set_rgbLED_color(MAGENTA)
    elif code[2] == 231:
        set_rgbLED_color(WHITE)
    elif code[2] == 215:
        set_rgbLED_color(BLACK)
    else:
        set_rgbLED_color(BLACK)

    last_code = code
