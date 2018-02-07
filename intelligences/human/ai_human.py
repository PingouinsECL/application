import pygame
from pygame.locals import *
from const import *

def ai_human(board, players, display, player_number, list_active_pawns):

    number_pawns = len(players[player_number].pawns)

    def getCase(t):
        x, y = t

        nx = (x-mx) // case_width
        ny = (y-my) // case_height

        if -1 < nx < 15 and -1 < ny < 8 :
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
        else:
            return -1, -1
    
    def getPawnNumber(case_pawn):
        k = 0
        while k < number_pawns:
            if k in list_active_pawns and players[player_number].pawns[k].x == case_pawn.x and \
                players[player_number].pawns[k].y == case_pawn.y :
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

    """
    for k in range(number_pawns):
        if k in list_active_pawns:
            print(k, players[player_number].pawns[k].accessibles)
    """

    while not(selected):

        # asking choices to the player

        pawn_number = 100
        direction = -1
        dist = -1

        while (pawn_number < 0 or pawn_number > number_pawns):

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x_pawn, y_pawn = getCase(event.pos)
                    case_pawn = board.cases_tab[y_pawn][x_pawn]
                    if case_pawn != 0 and case_pawn.owner == player_number:
                        pawn_number = getPawnNumber(case_pawn)
                        if pawn_number in list_active_pawns :
                            restart = False
                            # print("Pion selectionne")
                        else:
                            pawn_number = 100
                    # else:
                        # print('Case invalide')

        while not(restart) and (dist < 0 or direction < 0):

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x_aim, y_aim = getCase(event.pos)

                    if board.cases_tab[y_aim][x_aim] != 0:

                        direction, dist = getDirDist(x_pawn, y_pawn, x_aim, y_aim)
                        dist = int(dist)

                        if (-1 < direction < 6 and 0 < dist <= players[player_number].pawns[pawn_number].accessibles[direction]):
                            # print("Case sélectionnée. Déplacement")
                            selected = True
                    
                    else:
                        # print("Case invalide. Sélection du pion")
                        restart = True
                        pawn_number = 100
                        direction = -1
                        dist = -1
        
    print("Joué !")
    return direction, dist, pawn_number
