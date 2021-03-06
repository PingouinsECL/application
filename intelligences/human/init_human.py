import pygame
from pygame.locals import *
from const import *

def init_human(board, k, display):

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
