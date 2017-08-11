# CIRC14 - Metro Express NeoPixel make it better
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import board
import digitalio
import analogio
import adafruit_character_lcd as LCD
import time

light = analogio.AnalogIn(board.A0)

# set up our lcd object { 
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
# }

while True:
    lcd.clear()
    percent = str(100-((light.value/65535)*100))
    nice = percent[:percent.find('.')]
    lcd.message(nice + "% bright")
    # lcd.message(str(light.value))
    time.sleep(1)
    # increment our elapsed_secs variable each time a second passes
