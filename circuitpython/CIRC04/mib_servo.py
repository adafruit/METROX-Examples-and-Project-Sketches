"""
'mib_servo.py'.

=================================================
sweeping a servo with an analog potntiometer
requires:
- Adafruit_CircuitPython_Motor
"""
import time
import analogio
import board
import pulseio
from adafruit_motor import servo


servo = servo.servo(pulseio.PWMOut(board.D9))
pot = analogio.AnalogIn(board.A0)


def servo_sweep():
    """sweeps the servo."""
    for angle_fwd in range(0, 180, 1):
        servo.angle = angle_fwd
        time.sleep(0.01)
    for angle_bkwd in range(180, 0, -1):
        servo.angle = angle_bkwd
        time.sleep(0.01)


def pot_sweep():
    """assigns servo value to an analog potntiometer value."""
    val = pot.value / 65536
    servo.angle = 180 * val
    time.sleep(0.05)


while True:
    servo_sweep()
    # pot_sweep()
