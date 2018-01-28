import pygame
from pygame.locals import *

from init_random import *
from init_human import *
from init_max import *

def init_position(board, players, display, window, background, pos_background):

    for l in range(len(players[0].pawns)):
        for k in range(len(players)):

            mode = players[k].mode
            x, y = 0, 0

            # selecting the position mode

            if mode == 0:
                x, y = init_human(board, l, display)
            elif mode == 1:
                x, y = init_random(board)
            elif mode == 2 :
                x, y = init_max(board)
            else:
                x, y = 0, 0

            players[k].pawns[l].place(board, x, y)

            window.blit(background, pos_background)
            display = board.display(window)
            pygame.display.flip()

    return players
