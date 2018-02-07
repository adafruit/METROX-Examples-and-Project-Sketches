"""
'piezo_music.py'.

=================================================
Twinkle Twinkle with a piezo!
requires:
- simpleio library
"""
import time
import board
from simpleio import tone

note_array = 'ccdcfeccdcgf '
beat_array = [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 4]
tone_array = {'c': 263,
              'd': 293,
              'e': 329,
              'f': 349,
              'g': 391,
              'a': 440,
              'b': 493,
              'C': 523}
tempo = 300

# play the notes!
for i, item in enumerate(note_array):
    tempodelay = 60 / tempo
    note = note_array[i]
    beat = beat_array[i]

    print(note, end='')
    if note == ' ':
        time.sleep(beat * tempodelay)
    else:
        tone(board.D9, tone_array[note], beat*tempodelay)
    time.sleep(tempodelay/2)
