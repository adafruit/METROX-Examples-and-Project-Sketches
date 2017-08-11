# CIRC06 - Music with Piezo 
# (Circuit Python)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com 

# by Limor Fried/Ladyada and Asher Lieber for Adafruit Industries.             

# import required libraries
import digitalio
import pulseio
import board
import time
from simpleio import tone

# d9
# a space represents a rest
notes = 'ccdcfeccdcgf ' 
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
# bpm
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
