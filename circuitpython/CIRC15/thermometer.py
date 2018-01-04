"""
'thermometer.py'
=================================================
a little tmp36-based thermometer with a character lcd

requires:
- CircuitPython_CharLCD Module
"""

import time
import analogio
import digitalio
import adafruit_character_lcd
from simpleio import map_range
from board import *

#   Character LCD Config:
#   modify this if you have a different sized charlcd
lcd_columns = 16
lcd_rows = 2

#   Metro Express Pin Config:
lcd_rs = digitalio.DigitalInOut(D7)
lcd_en = digitalio.DigitalInOut(D8)
lcd_d7 = digitalio.DigitalInOut(D12)
lcd_d6 = digitalio.DigitalInOut(D11)
lcd_d5 = digitalio.DigitalInOut(D10)
lcd_d4 = digitalio.DigitalInOut(D9)
lcd_backlight = digitalio.DigitalInOut(D13)

#   Init the lcd class
lcd = adafruit_character_lcd.Character_LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                           lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

therm = analogio.AnalogIn(A0)

# loop forever
while True:
    # get temperature from sensor
    tmp = ((((map_range(therm.value, 0, 65535, 0, 3.3))-.5)*100)*1.8)+32
    lcd.clear()
    lcd.message('temp: ' + str(tmp)[:5] + ' * f')
    time.sleep(.6)
