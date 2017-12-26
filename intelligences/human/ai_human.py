import pygame
from pygame.locals import *
from const import *

def ai_human(N, players, board, list_active_pawns, display):

    number_pawns = len(players[N].pawns)

    def getCase(t):
        x, y = t

        nx = (x-mx) // case_width
        ny = (y-my) // case_height

        if display[ny][nx] != 0 and display[ny][nx].hover((x, y)):
            return nx, ny
        elif nx > 1 and display[ny][nx-2] != 0 and display[ny][nx-2].hover((x, y)):
            return nx-2, ny
        elif nx > 0 and ny > 0 and display[ny-1][nx-1] != 0 and display[ny-1][nx-1].hover((x, y)):
            return nx-1, ny-1
        elif nx < 14 and ny > 0 and display[ny-1][nx+1] != 0 and display[ny-1][nx+1].hover((x, y)):
            return nx+1, ny-1
        elif nx < 13 and display[ny][nx+2] != 0 and display[ny][nx+2].hover((x, y)):
            return nx+2, ny
        elif nx < 14 and ny < 7 and display[ny+1][nx+1] != 0 and display[ny+1][nx+1].hover((x, y)):
            return nx+1, ny+1
        elif nx > 0 and ny < 7 and display[ny+1][nx-1] != 0 and display[ny+1][nx-1].hover((x, y)):
            return nx-1, ny+1
        else:
            return -1, -1
    
    def getPawnNumber(case_pawn):
        k = 0
        while k < number_pawns:
            if k in list_active_pawns and players[N].pawns[k].x == case_pawn.x and players[N].pawns[k].y == case_pawn.y :
                return k
            k += 1
        return -1

    def getDirDist(x_pawn, y_pawn, x_aim, y_aim):
        dx = x_aim - x_pawn
        dy = y_aim - y_pawn

        if dx > 0 and dy < 0 and -dy//dx == -dy/dx :
            return 0, -dy
        if dy == 0 and dx > 0:
            return 1, dx//2
        if dx > 0 and dy > 0 and dy//dx == dy/dx:
            return 2, dy
        if dx < 0 and dy > 0 and -dy//dx == -dy/dx:
            return 3, dy
        if dy == 0 and dx < 0:
            return 4, -dx//2
        if dx < 0 and dy < 0 and dy//dx == dy/dx:
            return 5, -dy
        else:
            return -1, -1
        
        

    selected = False

    for k in range(number_pawns):
        if k in list_active_pawns:
            print(k, players[N].pawns[k].accessibles)
        else:
            print("Le pion ", k, " ne peut pas jouer")

    while not(selected):

        # asking choices to the player

        pawn_number = -1
        direction = -1
        dist = -1

        while (pawn_number < 0 or pawn_number > number_pawns):

            # print("Selection du pion", number_pawns, pawn_number)

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x_pawn, y_pawn = getCase(event.pos)
                    case_pawn = board.cases_tab[y_pawn][x_pawn]
                    if case_pawn != 0 and case_pawn.owner == N:
                        pawn_number = getPawnNumber(case_pawn)
                        print("Pion selectionne")
                    else:
                        print('Case invalide')
        
        while (dist < 0 or direction < 0):

            # print("Selection de la case cible")

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x_aim, y_aim = getCase(event.pos)

                    direction, dist = getDirDist(x_pawn, y_pawn, x_aim, y_aim)
                    dist = int(dist)

                    if (-1 < direction < 6 and 0 < dist <= players[N].pawns[pawn_number].accessibles[direction]):
                        selected = True
                    else:
                        pawn_number = -1
                        direction = -1
                        dist = -1
        
    print("Joué !")
    return direction, dist, pawn_number
