import board
import analogio 
import pulseio

piezo = pulseio.PWMOut(board.D6)
photo = analogio.AnalogIn(board.A0)

def _map(x, in_min, in_max, out_min, out_max):
    outrange = float(out_max - out_min)
    inrange = float(in_max - in_min)
    ret = (x - in_min) * (outrange / inrange) + out_min
    if (out_max > out_min):
        return max(min(ret, out_max), out_min)
    else:
        return max(min(ret, out_min), out_max)
while True:
    val = int(_map(photo.value, 0, 65520, 1000, 64000))
    piezo.duty_cycle = val 
