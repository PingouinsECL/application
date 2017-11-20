from ai_random import *

def select_mode(N, players, board):
    mode = players[N].mode

    if mode == 0:
        print("A vous de jouer")
        return False, 0, 0, 0
    else:
        print("Au joureur ", str(N), " de jouer selon le mode ", mode)
        if mode == 1:
            return ai_random(N, players, board)
