from ai_random import *
from ai_human import *
from ai_max import *

def select_mode(N, players, board, display):
    mode = players[N].mode

    number_pawns = len(players[N].pawns)

    # calculating possibilities
    for i in range(number_pawns):
        if players[N].pawns[i] != 0:
            players[N].pawns[i].compute_accessible(board)

    # active pawns and cleaning isolated ones
    for k in range(number_pawns):
        if players[N].pawns[k] != 0 and players[N].pawns[k].accessibles == [0]*6:
            print('Le pion ', k, ' du joueur ', N, ' TOMBE à l\'eau')
            # to_delete.append(k)
            players[N].pawns[k] = 0

    list_number_pawns = []
    for k in range(len(players[N].pawns)):
        if players[N].pawns[k] != 0:
            list_number_pawns.append(k)
    number_pawns = len(list_number_pawns)

    # selection of the game mode

    fail = (number_pawns == 0)

    if fail:
        return True, players[N].pawns, (0, 0, 0)
    else:
        if mode == 0:
            print("A vous de jouer")
            return fail, players[N].pawns, ai_human(N, players, board, list_number_pawns, number_pawns, display)
        elif mode == 1:
            print("Au joueur ", str(N), " de jouer selon le mode ", mode)
            return fail, players[N].pawns, ai_random(N, players, board, list_number_pawns, number_pawns)
        elif mode == 2:
            print("Au joueur ", str(N), " de jouer selon le mode ", mode)
            return fail, players[N].pawns, ai_max(N, players, board, list_number_pawns, 5) # dernier nb à changer, pour test
        else:
            print("Au joueur ", str(N), " de jouer selon le mode ", mode)
            return fail, players[N].pawns, ai_random(N, players, board, list_number_pawns, number_pawns)
