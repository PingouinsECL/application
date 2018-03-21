from pawn import *

from ai_random import *
from ai_human import *
from ai_maxN import *
from ai_maxN_ab import *
from ai_maxN_time import *
from ai_monte_carlo import *
from ai_monte_carlo_guided import *


def select_mode(board, players, display, player_number):
    mode = players[player_number].mode

    number_pawns = len(players[player_number].pawns)

    # calculating possibilities and reporting inactive pawns
    for i in range(number_pawns):
        for k in range(len(players)):
            players[k].pawns[i].compute_accessible(board)
            # if not(players[k].pawns[i].remain):
                # print('Le pion ' + str(i) + ' du joueur ' + str(player_number) + ' TOMBE à l\'eau')

    list_active_pawns = []
    list_isolated_pawns = []
    for k in range(number_pawns):
        if players[player_number].pawns[k].active:
            if not players[player_number].pawns[k].isolate:
                list_active_pawns.append(k)
            elif players[player_number].pawns[k].remaining_actions != []:
                list_isolated_pawns.append(k)

    # selection of the game mode

    fail = (len(list_active_pawns) == 0 and len(list_isolated_pawns) == 0)

    if fail:
        return True, players[player_number].pawns, (0, 0, 0)
    else:
        if mode == 0:
            return fail, players[player_number].pawns, ai_human(board, players, display, player_number, list_active_pawns+list_isolated_pawns)
        elif len(list_active_pawns) != 0:
            elif mode == 1:
                return fail, players[player_number].pawns, ai_random(players, player_number, list_active_pawns)
            elif mode == 2:
                return fail, players[player_number].pawns, ai_maxN(board, players, player_number, 3) # dernier nb à changer, pour test
            elif mode == 3:
                return fail, players[player_number].pawns, ai_maxN_ab(board, players, player_number, 3) # dernier nb à changer, pour test
            elif mode == 4:
                return fail, players[player_number].pawns, ai_maxN_time(board, players, player_number, 2) # dernier nb à changer, pour test
            elif mode == 5:
                return fail, players[player_number].pawns, ai_monte_carlo(board, players, player_number, itermax=2000, timemax=3) # dernier nb à changer, pour test
            elif mode == 6:
                return fail, players[player_number].pawns, ai_monte_carlo_guided(board, players, player_number, itermax=2000, timemax=3) # dernier nb à changer, pour test
            else:
                return fail, players[player_number].pawns, ai_random(players, player_number, list_active_pawns)
        elif len(list_isolated_pawns) != 0:
            return fail, players[player_number].pawns, players[player_number].pawns[list_isolated_pawns[0]].remaining_actions.pop()
        else:
            return fail, players[player_number].pawns, ai_random(players, player_number, list_active_pawns)
