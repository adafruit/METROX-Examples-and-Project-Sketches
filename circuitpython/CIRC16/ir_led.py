# CIRC16 - IR Sensor
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber for Adafruit Industries

import board
import digitalio
import IRrecvPCI
import IRLib_P01_NECd

# NEC button 1
button_1 = 16582903

led = digitalio.DigitalInOut(board.D6)
led.switch_to_output()

recvr = IRrecvPCI.IRrecvPCI(board.D3)
recvr.enableIRIn()

dec = IRLib_P01_NECd.IRdecodeNEC()

def get_signal():
    # wait until results are available
    while not recvr.getResults():
        pass
    recvr.enableIRIn()
    dec.decode()
    return dec.value

while True:
    if get_signal() == button_1:
        print('but 1 pressed')
        led.value = True
    else:
        led.value = False
