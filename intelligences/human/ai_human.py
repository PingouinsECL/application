import pygame
from pygame.locals import *
from const import *
from display_scores import *

def ai_human(board, players, display, player_number, list_active_pawns, window, background, pos_background):

    number_pawns = len(players[player_number].pawns)

    def getCase(t):
        x, y = t

        
        ny = (y-my) // case_height
        if ny % 2 == 0:
            nx = 2 * int((x-mx) // case_width)
        else:
            nx = 2 * int((x-mx-case_width//2)//case_width) + 1

        if -1 < nx < 15 and -1 < ny < 8 and display[ny][nx] != 0 and display[ny][nx].hover((x, y)):
                return nx, ny
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
        
    def list_access(pawn):
        access=pawn.accessibles
        dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]
        list=[]
        for i in range(6):
            for h in range(access[i]+1):
                list.append([pawn.x+h*dirs[i][0],pawn.y+h*dirs[i][1]])
        return(list)
        
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
            
            scores = [player.score for player in players]

            window.blit(background, pos_background)
            board.display(window,list_access(players[player_number].pawns[pawn_number]))
            display_scores(scores, window)
            pygame.display.flip()
            
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
        
    return direction, dist, pawn_number
