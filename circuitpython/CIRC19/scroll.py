from adafruit_hid import mouse
import analogio
import digitalio
import board
import time

button = digitalio.DigitalInOut(board.D2)
pot = analogio.AnalogIn(board.A0)

m = mouse.Mouse()

def _map(x, in_min, in_max, out_min, out_max):
    outrange = float(out_max - out_min)
    inrange = float(in_max - in_min)
    ret = (x - in_min) * (outrange / inrange) + out_min
    if (out_max > out_min):
        return max(min(ret, out_max), out_min)
    else:
        return max(min(ret, out_min), out_max)

while True:
    if not button.value: # move while button is pressed
    # if button.value: # stop moving when button is pressed
        #maps potentiometer value to mouse scroll value
        # m.move(0, 0, int(_map(pot.value, 50, 65520, -127, 127)))
        m.move(0, 0, int(_map(pot.value, 50, 65520, -5, 5)))
        time.sleep(.08)
