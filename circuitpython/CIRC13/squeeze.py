import board
import pulseio 
import analogio

squeeze = analogio.AnalogIn(board.A2)
led = pulseio.PWMOut(board.D9)

while True:
    led.duty_cycle = squeeze.value
