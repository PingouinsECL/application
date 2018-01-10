from ai_random import *
from ai_human import *
from ai_max import *
from pawn import *

def select_mode(board, players, display, player_number):
    mode = players[player_number].mode

    number_pawns = len(players[player_number].pawns)

    # calculating possibilities and reporting inactive pawns
    for i in range(number_pawns):
        for k in range(len(players)):
            players[k].pawns[i].compute_accessible(board)
        if not(players[k].pawns[i].remain):
            print('Le pion ' + str(i) + ' du joueur ' + str(player_number) + ' TOMBE à l\'eau')

    list_active_pawns = []
    for k in range(number_pawns):
        if players[player_number].pawns[k].active:
            list_active_pawns.append(k)

    # selection of the game mode

    fail = (len(list_active_pawns) == 0)

    if fail:
        return True, players[player_number].pawns, (0, 0, 0)
    else:
        if mode == 0:
            print("A vous de jouer")
            return fail, players[player_number].pawns, ai_human(board, players, display, player_number, list_active_pawns)
        elif mode == 1:
            print("Au joueur " + str(player_number) + " de jouer selon le mode " + str(mode))
            return fail, players[player_number].pawns, ai_random(players, player_number, list_active_pawns)
        elif mode == 2:
            print("Au joueur " + str(player_number) + " de jouer selon le mode " + str(mode))
            return fail, players[player_number].pawns, ai_max(board, players, player_number, 3) # dernier nb à changer, pour test
        else:
            print("Au joueur " + str(player_number) + " de jouer selon le mode " + str(mode))
            return fail, players[player_number].pawns, ai_random(players, player_number, list_active_pawns)
