# CIRC15 - Thermometer
# (CircuitPython)                                                                               
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com
                                                                                                
# by Asher Lieber for Adafruit Industries.

import time
import digitalio
import adafruit_character_lcd as LCD
import board
import analogio
from simpleio import map_range

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

therm = analogio.AnalogIn(board.A0)

# loop forever
while True:
    # get temperature from sensor
    tmp = ((((map_range(therm.value, 0, 65535, 0, 3.3))-.5)*100)*1.8)+32
    lcd.clear()
    # lcd.message('temp: ' + str(therm.value * .004882814)[:5] + ' * f')
    lcd.message('temp: ' + str(tmp)[:5] + ' * f')
    time.sleep(.6)
