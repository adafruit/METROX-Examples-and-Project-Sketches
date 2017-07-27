# CIRC06 - Music with Piezo 
# (Circuit Python)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com 

# by Limor Fried/Ladyada and Asher Lieber for Adafruit Industries.             

# import required libraries
import digitalio
import pulseio
import board
import time

piezoPin = board.D9
# create a PWMOut object for piezo
piezo = pulseio.PWMOut(piezoPin, frequency = 440, duty_cycle = 0, variable_frequency=True)

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


def playTone(tone, duration):
    piezo.frequency = int(tone)
    print(' ->', tone)
    # half of max
    piezo.duty_cycle = 65536 // 2
    time.sleep(duration)
    piezo.duty_cycle = 0

# play the notes!
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
