# PROJ02 - Fidget Spinner Tachometer
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries

import board
import time
import digitalio
import analogio
import adafruit_character_lcd as LCD

# setting up the LCD 
#    {
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
#    }

light = analogio.AnalogIn(board.A0)
led   = digitalio.DigitalInOut(board.D2)
led.switch_to_output()

spinner_arms = 3

sample_depth = 256

target_sample_rate_hz = 150

l_levels = 0

# led.value = True
lcd.message('GET READY!')
for i in range(1000):
    l_levels += light.value
    time.sleep(.001)
threshold = l_levels/1000
print('threshold: ' + str(threshold))

# led.value = False

readings = []
start = time.monotonic()
for i in range(sample_depth):
    readings.append(light.value)
stop = time.monotonic()
print((stop-start)*1000)

target_period = 1/target_sample_rate_hz
actual_period = (stop-start)/sample_depth
delay = 0
if actual_period > target_period:
    #can't sample fast enough
    print('can\'t sample fast enough!')
else:
    delay = target_period - actual_period

led.value = True

# print(str(delay*sample_depth) + ' aaa')
# while True:
# high_score = 0

# adds zeros for prettier output
def add_z(strn, digits):
    if len(strn) == digits: return strn
    else:
        ret = ''
        for i in range(digits-len(strn)):
            ret += '0'
    return ret + strn

def spin():
    vals = []
    high_score = 0
    while True:
        time.sleep(1)

        readings = []
        start = time.monotonic()
        lcd.clear()
        lcd.message('start spinning!')
        time.sleep(1)
        for i in range(sample_depth, 0, -1):
            # lcd.clear()
            if i == sample_depth / 3:
                lcd.clear()
                lcd.message('keep spinning!')
            if i == sample_depth / 2:
                lcd.clear()
                lcd.message('almost there!')
            lcd.message('\n' + add_z(str(i), 3) + ' hs: ' + str(round(high_score)))
            readings.append(light.value)
            time.sleep(delay)
        stop = time.monotonic()
        elapsed = stop - start
        # min and max readings from sample
        min_val = min(readings)
        max_val = max(readings)

        magnitude = max_val - min_val
        if magnitude < threshold:
            continue

        midpoint = min_val + magnitude/2
        crossings = 0
        for i in range(1, sample_depth):
            p0 = readings[i-1]
            p1 = readings[i]
            if p1 == midpoint or p0 < midpoint < p1 or p0 > midpoint > p1:
                    crossings += 1
        # print(crossings)
        period = elapsed/(crossings/2/spinner_arms)
        frequency = 1/period
        rpm = frequency * 60
        lcd.clear()
        lcd.message('\n' + str(round(rpm)) + ' RPM, ' + str(crossings) + 'Xing')
        print(rpm)
        vals.append(rpm)
        if rpm > high_score:
            high_score = rpm
            time.sleep(1)
            lcd.clear()
            lcd.message('you beat the\nhigh score!')
        time.sleep(1)
    return vals
            # time.sleep(1)
spin()
