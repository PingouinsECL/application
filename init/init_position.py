from init_random import *

def init_position(board, players):

    print("\nPositions de départ des pions\n")
    for l in range(len(players[0].pawns)):
        for k in range(len(players)):

            mode = players[k].mode
            print("Paramétrage du joueur numéro ", k, " qui a le mode ", mode, "\n")

            if mode == 0:
                print("Paramétrage du pion numéro ", l, " (aidez-vous du plateau)")
                x = int(input("X ? (2, 4) \n"))
                y = int(input("X ? (2, 2) \n"))
                players[k].pawns[l].place(board, x, y)
            else:
                x, y = init_random(board, players)
                players[k].pawns[l].place(board, x, y)

        print("Fin du paramétrage du joueur ", k, "\n")

    print("Fin du paramétrage des positions initiales\n")

    return players
