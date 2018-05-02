import pygame
from pygame.locals import *
from const import *
from button import *
from display_scores import *
from max_island import *
from ai_maxN_time import *

def ai_human(board, players, display, player_number, list_active_pawns, window, background, pos_background):

    number_pawns = len(players[player_number].pawns)

    def getCase(t):
        x, y = t
        
        ny = (y-my) // (case_height - case_height_margin)

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
        
    def list_access(pawn,access=[]):
        if access == []:
            access=pawn.accessibles
            dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]
            list=[]
            for i in range(6):
                for h in range(access[i]+1):
                    list.append([pawn.x+h*dirs[i][0],pawn.y+h*dirs[i][1]])
            return(list)
        dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]
        list=[[pawn.x,pawn.y]]
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
        hint_image = pygame.image.load(path_hint).convert()
        hint_image_hover = pygame.image.load(path_hint_hover).convert()
        hint_but = Button(hint_image, hint_image_hover, pos_hint, 0)
        hint = False
        hinted_cases=[]
        cursor = [0, 0]

        while (pawn_number < 0 or pawn_number > number_pawns):
            
            scores = [player.score for player in players]
            
            window.blit(background, pos_background)
            board.display(window,list=[[],hinted_cases])
            display_scores(scores, window)
            hint_but.show(window,cursor)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cursor = event.pos
                    x_pawn, y_pawn = getCase(cursor)
                    case_pawn = board.cases_tab[y_pawn][x_pawn]
                    if case_pawn != 0 and case_pawn.owner == player_number:
                        pawn_number = getPawnNumber(case_pawn)
                        if pawn_number in list_active_pawns :
                            restart = False
                            # print("Pion selectionne")
                        else:
                            pawn_number = 100
                    if hint_but.hover(cursor):
                        hint = True
                        if hinted_cases == []:
                            flag=update_islands(board, players, True)
                            if flag :
                                h_direction, h_dist, h_pawn_number = players[player_number].pawns[list_active_pawns[0]].remaining_actions[-1]
                            else :
                                h_direction, h_dist, h_pawn_number = ai_maxN_time(board, players, player_number, 1)
                            for i in range(number_pawns):
                                players[player_number].pawns[i].compute_accessible(board)
                            access=[0,0,0,0,0,0]
                            access[h_direction]=h_dist
                            hinted_cases=list_access(players[player_number].pawns[h_pawn_number],access)
                        
                elif event.type == MOUSEMOTION:
                    cursor = event.pos
                    
            
                    # else:
                        # print('Case invalide')

        while not(restart) and (dist < 0 or direction < 0):

            scores = [player.score for player in players]

            window.blit(background, pos_background)
            board.display(window,list=[list_access(players[player_number].pawns[pawn_number]),hinted_cases])
            display_scores(scores, window)
            hint_but.show(window,cursor)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cursor = event.pos
                    x_aim, y_aim = getCase(cursor)
                    case_aim = board.cases_tab[y_aim][x_aim]

                    if case_aim != 0:

                        direction, dist = getDirDist(x_pawn, y_pawn, x_aim, y_aim)
                        dist = int(dist)

                        if (-1 < direction < 6 and 0 < dist <= players[player_number].pawns[pawn_number].accessibles[direction]):
                            # print("Case sélectionnée. Déplacement")
                            selected = True
                        
                        elif case_aim.owner == player_number:
                            x_pawn, y_pawn = x_aim, y_aim
                            pawn_number = getPawnNumber(case_aim)
                            direction = -1
                            dist = -1
                            if pawn_number not in list_active_pawns :
                                restart = True
                                pawn_number = 100
                    elif hint_but.hover(cursor):
                        hint = True
                        if hinted_cases == []:
                            h_direction, h_dist, h_pawn_number = ai_maxN_time(board, players, player_number, 3)
                            for i in range(number_pawns):
                                players[player_number].pawns[i].compute_accessible(board)
                            access=[0,0,0,0,0,0]
                            access[h_direction]=h_dist
                            hinted_cases=list_access(players[player_number].pawns[h_pawn_number],access)
                    else:
                        # print("Case invalide. Sélection du pion")
                        restart = True
                        pawn_number = 100
                        direction = -1
                        dist = -1
                elif event.type == MOUSEMOTION:
                    cursor = event.pos
        
    return direction, dist, pawn_number
