import pygame
from pygame.locals import *

from init_random import *
from init_human import *

def init_position(board, players, display, window, background, pos_background):

    print("\n###\t Positions de départ des pions \t###")
    print("Choisir une case accessible de score 1\n")

    for l in range(len(players[0].pawns)):
        for k in range(len(players)):

            mode = players[k].mode
            print("###\t###\tParamétrage du joueur numéro ", k, " qui a le mode ", mode, "\t###\t###\n")

            x, y = 0, 0

            # selecting the position mode

            if mode == 0:
                x, y = init_human(board, players, l, display)
            elif mode == 1:
                x, y = init_random(board)
            else:
                x, y = 0, 0

            players[k].pawns[l].place(board, x, y)

            window.blit(background, pos_background)
            display = board.display(window)
            pygame.display.flip()

        print("###\t###\t Fin du paramétrage du joueur ", k, "\t###\t###\n")

    print("\n###\tFin du paramétrage des positions initiales\t###\n")

    return players
