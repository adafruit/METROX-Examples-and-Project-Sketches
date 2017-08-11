# CIRC16 - IR Sensor make it better rgb
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries

import board
import digitalio
import IRrecvPCI
import IRLib_P01_NECd # remote uses NEC


LEDs = [digitalio.DigitalInOut(board.D4), digitalio.DigitalInOut(board.D1), digitalio.DigitalInOut(board.D2)]

for i in LEDs:
    i.switch_to_output()

# only red
RED     = [True, False, False]  
# only green
GREEN   = [False, True, False]  
# only blue
BLUE    = [False, False, True]  
# red+green
YELLOW  = [True, True, False]   
# green+blue
CYAN    = [False, True, True]   
# red+blue
MAGENTA = [True, False, True]   
# all on
WHITE   = [True, True, True]    
# all off
BLACK   = [False, False, False] 

# dict of button values and their corresponding colors
buttons = {
16582903: RED ,
16615543: GREEN,
16599223: BLUE,
16591063: YELLOW,
16623703: CYAN,
16607383: MAGENTA,
16586983: WHITE,
16619623: BLACK}

def set_color(color):
    for i in range(len(LEDs)):
        LEDs[i].value = not color[i]


recvr = IRrecvPCI.IRrecvPCI(board.D3)
recvr.enableIRIn()

dec = IRLib_P01_NECd.IRdecodeNEC()
print('awaiting signal!')

def get_signal():
    while not recvr.getResults():
        pass
    recvr.enableIRIn()
    dec.decode()
    #dec.dumpResults(True)
    return dec.value
while True:
    tmp = get_signal()
    if tmp in buttons:
        set_color(buttons[tmp])
    # if none of the mapped buttons were pressed, turn LED off
    else:
        set_color(BLACK)
