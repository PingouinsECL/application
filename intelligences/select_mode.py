from pawn import *

from ai_random import *
from ai_human import *
from ai_maxN_time import *
from ai_alphabeta import *
from ai_monte_carlo_guided import *
from ai_impaler import *


def select_mode(board, players, display, player_number, players_lost, window, background, pos_background, adversary_numbers, points):
    mode = players[player_number].mode

    number_pawns = len(players[player_number].pawns)

    # calculating possibilities and reporting inactive pawns
    for i in range(number_pawns):
        for k in range(len(players)):
            players[k].pawns[i].compute_accessible(board)

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
            return fail, players[player_number].pawns, ai_human(board, players, display, player_number, list_active_pawns, list_isolated_pawns, window, background, pos_background)
        
        elif len(list_active_pawns) != 0:
            
            if mode == 1:
                return fail, players[player_number].pawns, ai_random(players, player_number, list_active_pawns)

            elif mode == 2:
                return fail, players[player_number].pawns, ai_monte_carlo_guided(board, players, player_number, itermax=2000, timemax=3) # dernier nb à changer, pour test
            
            elif mode == 3:
                return fail, players[player_number].pawns, ai_impaler(board, players, player_number, list_active_pawns, adversary_numbers[player_number], points = points[player_number])

            elif mode == 4:
                tmax = 5
                if sum(players_lost[:len(players)]) == len(players) - 2:
                    adversary_number = 0
                    b = adversary_number != player_number and players_lost[adversary_number] == 0
                    while adversary_number < len(players) and not b:
                        adversary_number += 1
                        b = adversary_number != player_number and players_lost[adversary_number] == 0
                    return fail, players[player_number].pawns, ai_alphabeta(board, players, player_number, adversary_number, tmax)
                else:
                    return fail, players[player_number].pawns, ai_maxN_time(board, players, player_number, tmax)

            else:
                return fail, players[player_number].pawns, ai_random(players, player_number, list_active_pawns)
        
        # sequence to maximise score on the island
        elif len(list_isolated_pawns) != 0:
            return fail, players[player_number].pawns, players[player_number].pawns[list_isolated_pawns[0]].remaining_actions.pop()
        
        else:
            return fail, players[player_number].pawns, ai_random(players, player_number, list_active_pawns)
