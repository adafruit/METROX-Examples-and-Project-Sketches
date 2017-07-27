# PROJ04 - Music Box
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import board
import analogio
import digitalio
import pulseio
import time
import adafruit_character_lcd as LCD

# LCD setup
lcd_columns = 16
lcd_rows = 2
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_d6 = digitalio.DigitalInOut(board.D11)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)
lcd_backlight = digitalio.DigitalInOut(board.D13)
lcd = LCD.cirpyth_char_lcd(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

#making musical note custom characters
note = [0,15,15,9,9,27,27,0]
note2 = [0,7,4,4,4,4,28,28]
lcd.create_char(0, note)
lcd.create_char(1, note2)

piezo = pulseio.PWMOut(board.D6, frequency = 440, duty_cycle = 0, variable_frequency = True)

light = analogio.AnalogIn(board.A0)

tones = {'c': 261.625,
         'd': 293.665,
         'e': 329.63,
         'f': 349.23,
         'g': 391.995,
         'a': 440,
         'b': 493.885,
         'C': 523.25}

tempo = 300   # bpm

notes = "ccdcfeccdcgf "
beats = [ 1, 1, 1, 1,1,2,1,1,1,1,1,2,4]

def playTone(tone, duration):
    piezo.frequency = int(tone)
    #print(" ->", tone)
    # half of max
    piezo.duty_cycle = 65536 // 2 
    time.sleep(duration)
    piezo.duty_cycle = 0

tempodelay = 60/tempo
while True:
    lcd.clear()
    for i in range(8):
        # print custom characters to LCD
        lcd.message('\x00\x01')
    lcd.message('\n')
    # the darkest
    if light.value != 65520:
        lcd.set_backlight(True)
        # play those notes!
        for i in range(len(notes)):
            if light.value == 65520:
                lcd.clear()
                lcd.set_backlight(False)
                break
            note = notes[i]
            beat = beats[i]
            lcd.message(str(note))
            if note == ' ': time.sleep(beat * tempodelay)
            else:
                playTone(tones[note], beat*tempodelay)
            time.sleep(tempodelay/2)
