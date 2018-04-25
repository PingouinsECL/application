import pygame
from pygame.locals import *

from init_random import *
from init_human import *
from init_maxN_time import *
from init_monte_carlo_guided import *
from init_impaler import *

from init_lexicographic import *
from init_sum import *

def init_position(board, players, display, window, background, pos_background):

    for l in range(len(players[0].pawns)):
        for k in range(len(players)):

            mode = players[k].mode
            x, y = 0, 0

            # selecting the position mode
            if mode == 0:
                x, y = init_human(board, l, display)
            elif mode != 4:
                x,y=init_lexicographic(board)
            else:
                x,y=init_impaler(board,players,0)

            players[k].pawns[l].place(board, x, y)

            window.blit(background, pos_background)
            display = board.display(window)
            pygame.display.flip()

    return players
