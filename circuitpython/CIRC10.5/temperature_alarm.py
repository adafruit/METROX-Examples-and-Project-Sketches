import analogio
import pulseio
import board
import time

piezo = pulseio.PWMOut(board.D8, frequency = 440, duty_cycle = 0, variable_f
requency = True)

temp = analogio.AnalogIn(board.A0)

freezing_temp = 0 

boiling_temp = 100 

# affine transformation
def _map(x, in_min, in_max, out_min, out_max):
    outrange = float(out_max - out_min)
    inrange = float(in_max - in_min)
    ret = (x - in_min) * (outrange / inrange) + out_min
    if (out_max > out_min):
        return max(min(ret, out_max), out_min)
    else:
        return max(min(ret, out_min), out_max)

while True:
    temperature = _map(temp.value, 0, 65535, 0, 5)
    # temp to degrees C
    temperature = (temperature - .5) * 100
    print(temperature)

    if temperature < freezing_temp:
        piezo.duty_cycle = 30000
    if temperature > boiling_temp:
        piezo.duty_cycle = 10000
    time.sleep(.5)
