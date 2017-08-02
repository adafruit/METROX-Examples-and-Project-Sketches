# PROJ06 - Laser Pet Toy
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import board
import pulseio
import digitalio

import IRrecvPCI
import IRLib_P01_NECd
import time

import urandom

# remote codes
ENTER = 0xfd906f
BUTTON_0 = 0xfd30cf
RIGHT_ARROW = 0xfd50af                                 
LEFT_ARROW = 0xfd10ef
BUTTON_9 = 0xfd58a7

# the rest of these are not used in this PROJ 
# if you want to create more functions for the laser pet toy, use these
VOLUME_UP = 0xfd40bf
VOLUME_DOWN = 0xfd00ff
PLAY_PAUSE = 0xfd807f
UP_ARROW = 0xfda05f
DOWN_ARROW = 0xfdb04f
BUTTON_1 = 0xfd08f7
BUTTON_2 = 0xfd8877
BUTTON_3 = 0xfd48b7
BUTTON_4 = 0xfd28d7
BUTTON_5 = 0xfda857
BUTTON_6 = 0xfd6897
BUTTON_7 = 0xfd18e7
BUTTON_8 = 0xfd9867

# servo = pulseio.PWMOut(board.D9, frequency=50)
servo = pulseio.PWMOut(board.D6, frequency=50)
servo_min = .5
servo_max = 2.5

# laser = digitalio.DigitalInOut(board.D13)
# laser = digitalio.DigitalInOut(board.D3)
laser = digitalio.DigitalInOut(board.D2)
laser.switch_to_output()
continuous_laser_mode = True

current_angle = 90

# setting up IR reciever and decoder
# recvr = IRrecvPCI.IRrecvPCI(board.D2)
recvr = IRrecvPCI.IRrecvPCI(board.D10)
recvr.enableIRIn()
dec = IRLib_P01_NECd.IRdecodeNEC()

def servo_angle(angle):
    global current_angle
    current_angle = max(min(angle, 180), 0)
    pulse_width = servo_min + ((max(min(angle, 180), 0))/180)*(servo_max-servo_min)
    # range is 0-20 ms
    servo.duty_cycle = int((pulse_width/20)*65535)
    print('now at angle: ' + str(current_angle))

def get_signal():
    while not recvr.getResults():
        pass
    recvr.enableIRIn()
    dec.decode()
    # print(dec.value)
    return dec.value

def rand_angle():
    servo_angle(urandom.randint(0, 180))
while True:
    print(laser.value)
    if not continuous_laser_mode: laser.value = False
    tmp_signal = get_signal()
    if tmp_signal   == ENTER: continuous_laser_mode = not continuous_laser_mode
    elif tmp_signal == BUTTON_0: 
        laser.value = True
        rand_angle()
    elif tmp_signal == LEFT_ARROW:
        laser.value = True
        servo_angle(current_angle - 10)
    elif tmp_signal == RIGHT_ARROW:
        laser.value = True
        servo_angle(current_angle + 10)
    elif tmp_signal == BUTTON_9:
        laser.value = True
        while True:
            if recvr.getResults():
                break
            time.sleep(1)
            rand_angle()
