import board
import digitalio
import IRrecvPCI
import IRLib_P01_NECd # remote uses NEC


LEDs = [digitalio.DigitalInOut(board.D4), digitalio.DigitalInOut(board.D1), digitalio.DigitalInOut(board.D2)]

for i in LEDs:
    i.switch_to_output()

RED     = [True, False, False]   # only red
GREEN   = [False, True, False]   # only green
BLUE    = [False, False, True]   # only blue
YELLOW  = [True, True, False]    # red+green
CYAN    = [False, True, True]    # green+blue
MAGENTA = [True, False, True]    # red+blue
WHITE   = [True, True, True]     # all on
BLACK   = [False, False, False]  # all off

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
    else:
        set_color(BLACK)
