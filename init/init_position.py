from init_random import *
from init_human import *

def init_position(board, players):

    print("\nPositions de départ des pions\n")
    for l in range(len(players[0].pawns)):
        for k in range(len(players)):

            mode = players[k].mode
            print("Paramétrage du joueur numéro ", k, " qui a le mode ", mode, "\n")

            x, y = 0, 0

            # selecting the position mode

            if mode == 0:
                x, y = init_human(board, players, l)
            elif mode == 1:
                x, y = init_random(board, players)
            else:
                x, y = 0, 0

            players[k].pawns[l].place(board, x, y)

        print("Fin du paramétrage du joueur ", k, "\n")

    print("Fin du paramétrage des positions initiales\n")

    return players
