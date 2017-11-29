import pygame
from pygame.locals import *

def ai_human(N, players, board, list_number_pawns, number_pawns):

    # if no move can be done

    if number_pawns == 0 or not(players[N].can_play()):
        fail = True
        direction = 0
        dist = 0
        pawn_number = 0

    # else
    else:
        fail = False
        direction = 0
        dist = 100
        pawn_number = 0

        first = True

        for k in list_number_pawns:
            print(k, players[N].pawns[k].accessibles)

        while first or (dist > players[N].pawns[pawn_number].accessibles[direction]):
            if first:
                first = False
                print("Veuillez choisir un déplacement valide")
            else:
                print("Déplacement impossible. Veuillez choisir un déplacement valide")

            # asking choices to the player
            
            pawn_number = int(input("Numéro du pion :"))
            direction = int(input("Direction :"))
            dist = int(input("Distance :"))

    return fail, direction, dist, pawn_number
