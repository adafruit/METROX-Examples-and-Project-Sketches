# Circuit Python Explorers Guide
# CIRC06 - Music with Piezo

import time
import board
import digitalio
import pulseio
from simpleio import tone

# set note
notes = 'ccdcfeccdcgf '
# set beats
beats = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 4]
# set tones
tones = {'c': 263,
         'd': 293,
         'e': 329,
         'f': 349,
         'g': 391,
         'a': 440,
         'b': 493,
         'C': 523}
# set bpm
tempo = 300

# play the notes!
for i in range(len(notes)):
    tempodelay = 60 / tempo
    note = notes[i]
    beat = beats[i]
    print(note, end='')
    if note == ' ':
        time.sleep(beat * tempodelay)
    else:
        tone(board.D9, tones[note], beat*tempodelay)
    time.sleep(tempodelay/2)
