# PROJ03 - MetroPOV Display
# (CircuitPython)
# this circuit was designed for use with the Metro Express Explorers Guide on Learn.Adafruit.com

# by Asher Lieber or Adafruit Industries

import pov_display
import board
pins = [board.D2, board.D3, board.D4, board.D5, board.D6, board.D8, board.D9, board.D10]

pov = pov_display.pov(pins)

pov.print_str('METRO EXPRESS')
