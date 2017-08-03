# CIRC16 - IR Replay
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries

import time
import board
import pulseio
import digitalio
import array

# 38 for NEC
ir_led = pulseio.PWMOut(board.D9, frequency=1000*38, duty_cycle=0) 
ir_led_send = pulseio.PulseOut(ir_led)

recv = pulseio.PulseIn(board.D3, maxlen=150, idle_state = True)

# creating DigitalInOut objects for a record and play button
but0 = digitalio.DigitalInOut(board.D11) # record
but1 = digitalio.DigitalInOut(board.D10) # playback

# setting up indicator LED
led = digitalio.DigitalInOut(board.D4)
led.switch_to_output()

# waits for IR to be detected, returns
def get_ir():
    ir_f = array.array('H')
    print('waiting for ir')
    recv.clear()
    while len(recv) == 0:
        pass
    # time to collect more ir stuff
    time.sleep(.2) 
    print(len(recv))
    for i in range(len(recv)):
        ir_f.append(recv[i])
    recv.clear()
    time.sleep(.01)
    print('recieved')
    return ir_f

def imitate_u(ir_f):
    # enable_out()
    ir_led.duty_cycle = (2**16)//3 #???
    time.sleep(.4)
    print('sending')
    if ir_f[0] == 65535:
        ir_led_send.send(ir_f[1:])
    else:
        ir_led_send.send(ir_f)
    time.sleep(.5) # give some cooldown time

# so nothing devastating happens if play before record
to_send = array.array('H')
while True:
    # while (but0.value or but1.value):
        # pass
    # record
    if not but0.value:
        led.value = True
        to_send = get_ir()
        if len(to_send) != 72:
            for i in range(2):
                time.sleep(.1)
                led.value = not led.value
        led.value = False
    if not but1.value:
        for i in range(5):
            time.sleep(.05)
            led.value = not led.value
        if len(to_send) != 0:
            imitate_u(to_send)
        led.value = False
