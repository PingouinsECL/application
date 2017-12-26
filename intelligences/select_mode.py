from ai_random import *
from ai_human import *

def select_mode(N, players, board, display):
    mode = players[N].mode

    number_pawns = len(players[N].pawns)

    # calculating possibilities and reporting inactive pawns
    for i in range(number_pawns):
        players[N].pawns[i].compute_accessible(board)
        if not(players[N].pawns[i].remain):
            print('Le pion ', i, ' du joueur ', N, ' TOMBE à l\'eau')

    list_active_pawns = []
    for k in range(number_pawns):
        if players[N].pawns[k].active:
            list_active_pawns.append(k)

    # selection of the game mode

    fail = (len(list_active_pawns) == 0)

    if fail:
        return True, players[N].pawns, (0, 0, 0)
    else:
        if mode == 0:
            print("A vous de jouer")
            return fail, players[N].pawns, ai_human(N, players, board, list_active_pawns, display)
        elif mode == 1:
            print("Au joueur ", str(N), " de jouer selon le mode ", mode)
            return fail, players[N].pawns, ai_random(N, players, list_active_pawns)
        else:
            print("Au joueur ", str(N), " de jouer selon le mode ", mode)
            return fail, players[N].pawns, ai_random(N, players, list_active_pawns)
