import pygame
from pygame.locals import *

def ai_human(N, players, board, list_number_pawns, number_pawns):


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

    return direction, dist, pawn_number
