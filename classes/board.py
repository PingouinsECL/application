import random
import pygame

from case import *
from button import *

from const import *

window = pygame.display.set_mode((0, 0))

one = pygame.image.load(path_one)
two = pygame.image.load(path_two)
three = pygame.image.load(path_three)

a = pygame.image.load(path_a)
b = pygame.image.load(path_b)
c = pygame.image.load(path_c)
d = pygame.image.load(path_d)

image_number = [one, two, three]
image_player = [a, b, c, d]

class Board:

    """
    Class defining a board, set of cases
    """

    def __init__(self):
        n_1 = 30
        n_2 = 20
        n_3 = 10
        n_fish_tab = n_1*[1] + n_2*[2] + n_3*[3]
        for k in range(10):
            random.shuffle(n_fish_tab)

        cases_tab = []

        # number of cases already created
        i = 0

        for k in range(0, 8):

            if k % 2 == 0:
                n_case = 8
            else:
                n_case = 7

            line = []

            # to have a constant number of rows per line
            if k % 2 == 1:
                line.append(0)

            for l in range(0, n_case):

                n_fish = n_fish_tab[i]

                # creation of the case
                c = Case(2*l + k % 2, k, n_fish)
                line.append(c)
                line.append(0)

                i += 1

            # to have a constant number of rows per line
            if k % 2 == 0:
                line = line[:-1]

            cases_tab.append(line)

        self.cases_tab = cases_tab
        self.compute_islands()
    
    def casesStat(self):
        numberLeft = 0
        scoreLeft = 0
        for i in range(0, 8):
            for j in range(0, 15):
                if self.cases_tab[i][j] != 0:
                    if self.cases_tab[i][j].state == 1:
                        numberLeft += 1
                        scoreLeft += self.cases_tab[i][j].score
        return numberLeft, scoreLeft


    def compute_islands(self):
        dirs = [(1, -1), (2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1)]

        cases = self.cases_tab
        active_cases = [(x, y) for x in range(len(cases[0])) for y in range(len(cases)) if cases[y][x] != 0 and cases[y][x].state > 0]

        islands_list = []

        while active_cases != []:
            cur_island = []        
            occupied = []

            cur_case = active_cases[0]
            if cases[cur_case[1]][cur_case[0]].state == 2:
                occupied.append(cases[cur_case[1]][cur_case[0]].owner)

            active_cases.remove(cur_case)
            cur_island.append(cur_case)

            reachable = [(cur_case[0] + d[0], cur_case[1] + d[1]) for d in dirs if (cur_case[0] + d[0], cur_case[1] + d[1]) in active_cases]

            while reachable != []:
                cur_case = reachable[0]
                if cases[cur_case[1]][cur_case[0]].state == 2 and cases[cur_case[1]][cur_case[0]].owner not in occupied:
                    occupied.append(cases[cur_case[1]][cur_case[0]].owner)

                reachable.remove(cur_case)
                active_cases.remove(cur_case)
                cur_island.append(cur_case)

                reachable += [(cur_case[0] + d[0], cur_case[1] + d[1]) for d in dirs if (cur_case[0] + d[0], cur_case[1] + d[1]) in active_cases and (cur_case[0] + d[0], cur_case[1] + d[1]) not in reachable]

            islands_list.append([occupied, cur_island])

        self.islands = islands_list

    def display(self, window):

        sx, sy = case_width, case_height
        table_but = [[0 for k in range(15)] for k in range(8)]

        for k in range(0, 8):

            if k % 2 == 0:
                n_case = 8
            else:
                n_case = 7

            s = ''
            if k % 2 == 1:
                s += ' '
            real_l = 0

            for l in range(0, 15):
                if self.cases_tab[k][l] != 0:
                    c = self.cases_tab[k][l]
                    pos = [sx * real_l + mx + (k%2)*sx//2, sy * k + my]
                    real_l += 1

                    if c.state == 0:
                        s += '* '
                    elif c.owner != -1:
                        letter = chr(ord('a')+c.owner)
                        s += letter + ' '
                        table_but[k][l] = Button(image_player[c.owner], image_player[c.owner], pos, 1)
                        table_but[k][l].show(window, [0, 0])
                    else:
                        s += str(c.score) + ' '
                        table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                        table_but[k][l].show(window, [0, 0])

            # print(s)
        return table_but
