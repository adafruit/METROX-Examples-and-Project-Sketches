# PROJ05 - Metro Media Controller
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries.

import board
from adafruit_hid import keyboard

# required to decode NEC IR signals
import IRrecvPCI
import IRLib_P01_NECd

import digitalio
import time


# set this to True if you're using a mac computer
MAC_COMPUTER = True

# remote codes
ENTER = 0xfd906f
VOLUME_UP = 0xfd40bf                                                   
VOLUME_DOWN = 0xfd00ff                                                   
RIGHT_ARROW = 0xfd50af                                                   
LEFT_ARROW = 0xfd10ef                                                   
PLAY_PAUSE = 0xfd807f                                                   

# these are some extra button codes not used in this PROJ
# if you want to create more functions in VLC or any other app, use these
UP_ARROW = 0xfda05f                                                   
DOWN_ARROW = 0xfdb04f                                                   
BUTTON_0 = 0xfd30cf                                                   
BUTTON_1 = 0xfd08f7                                                   
BUTTON_2 = 0xfd8877                                                   
BUTTON_3 = 0xfd48b7                                                   
BUTTON_4 = 0xfd28d7                                                   
BUTTON_5 = 0xfda857                                                   
BUTTON_6 = 0xfd6897                                                   
BUTTON_7 = 0xfd18e7                                                   
BUTTON_8 = 0xfd9867                                                   
BUTTON_9 = 0xfd58a7                                                   

key = keyboard.Keyboard()
# layout = keyboard_layout_us.KeyboardLayoutUS(key)

recvr = IRrecvPCI.IRrecvPCI(board.D2)
recvr.enableIRIn()

dec = IRLib_P01_NECd.IRdecodeNEC()

built_in_led = digitalio.DigitalInOut(board.D13)
built_in_led.switch_to_output()

if MAC_COMPUTER:
    mod_key = keyboard.Keycode.LEFT_GUI
else:
    mod_key = keyboard.Keycode.LEFT_CONTROL

def enter_fullscreen():
    key.press(mod_key, keyboard.Keycode.F)
    key.release_all()

    built_in_led.value = True

def play_pause():
    key.press(keyboard.Keycode.SPACEBAR)
    key.release_all()

    built_in_led.value = True

def volume_up():
    key.press(mod_key, keyboard.Keycode.UP_ARROW)
    key.release_all()

    built_in_led.value = True

def volume_down():
    key.press(mod_key, keyboard.Keycode.DOWN_ARROW)
    key.release_all()

    built_in_led.value = True

def speed_up():
    key.press(mod_key, keyboard.Keycode.EQUALS)
    key.release_all()

    built_in_led.value = True

def speed_down():
    key.press(mod_key, keyboard.Keycode.MINUS)
    key.release_all()

    built_in_led.value = True

def get_signal():
    while not recvr.getResults():
        pass
    recvr.enableIRIn()
    dec.decode()
    # print(dec.value)
    return dec.value

while True:
    tmp_sig = get_signal()
    if   tmp_sig == PLAY_PAUSE: play_pause()
    elif tmp_sig == ENTER: enter_fullscreen()
    elif tmp_sig == VOLUME_UP: volume_up()
    elif tmp_sig == VOLUME_DOWN: volume_down()
    elif tmp_sig == RIGHT_ARROW: speed_up()
    elif tmp_sig == LEFT_ARROW: speed_down()
    else:
        # flash a warning
        for i in range(10):
            time.sleep(.2)
            built_in_led.value = not built_in_led.value

    # turn LED off after command has been completed
    time.sleep(.1)
    built_in_led.value = False
