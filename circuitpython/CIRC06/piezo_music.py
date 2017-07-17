# CIRC06 - Music with Piezo 
# (Circuit Python)

import digitalio
import pulseio
from board import *
import time

piezoPin = D9
piezo = pulseio.PWMOut(piezoPin, frequency = 440, duty_cycle = 0, variable_frequency=True)

notes = 'ccdcfeccdcgf ' # a space represents a rest
beats = [ 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 4]
#notes = 'ccggaagffeeddc ' # a space represents a rest
#beats = [ 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 ]
tones = {'c': 261.625,
         'd': 293.665,
         'e': 329.63,
         'f': 349.23,
         'g': 391.995,
         'a': 440,
         'b': 493.885,
         'C': 523.25}
tempo = 300   # bpm


def playTone(tone, duration):
    piezo.frequency = int(tone)
    print(' ->', tone)
    piezo.duty_cycle = 65536 // 2  # half of max
    time.sleep(duration)
    piezo.duty_cycle = 0

for i in range(len(notes)):
    tempodelay = 60 / tempo

    note = notes[i]
    beat = beats[i]
    print(note, end='')
    if note == ' ':
        time.sleep(beat * tempodelay)
    else:
        playTone(tones[note], beat*tempodelay)
    time.sleep(tempodelay/2)
