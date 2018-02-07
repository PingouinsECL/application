import pygame
from pygame.locals import *
from const import *

def init_human(board, k, display):

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

    # asking the players for coordinates

    x = -1
    y = -1
    
    selected = False

    while not(selected):

        # selecting target

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = getCase(event.pos)

                case_pawn = board.cases_tab[y][x]

                if case_pawn != 0 and case_pawn.score == 1 and case_pawn.state == 1:
                    selected = True

    return x, y
