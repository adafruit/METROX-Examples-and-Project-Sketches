import pov_display
import board
pins = [board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9]

pov = pov_display.pov(pins)

pov.print_str('METRO EXPRESS')