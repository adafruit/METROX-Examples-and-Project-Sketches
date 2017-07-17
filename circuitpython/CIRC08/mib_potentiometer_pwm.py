from digitalio import *
from analogio import *
from board import *
from pulseio import *
import time

led = PWMOut(D9)
pot = AnalogIn(A0)

while True:
    led.duty_cycle = pot.value

