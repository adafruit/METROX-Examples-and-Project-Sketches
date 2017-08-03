import board
import time
import digitalio
import adafruit_character_lcd as LCD

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

elapsed_secs = 0
while True:
    lcd.clear()
    lcd.message('hello, world!\n')
    # display the number of elapsed seconds on our LCD
    lcd.message(str(elapsed_secs))
    time.sleep(1)
    # increment our elapsed_secs variable each time a second passes
    elapsed_secs += 1
