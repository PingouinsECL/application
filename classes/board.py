import random
import pygame

from case import *
from button import *
from const import *

window = pygame.display.set_mode((0, 0))

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
            n_case = 8 if k%2 == 0 else 7
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

    def cases_stat(self):
        numberLeft = 0
        scoreLeft = 0
        for i in range(0, 8):
            for j in range(0, 15):
                if self.cases_tab[i][j] != 0:
                    if self.cases_tab[i][j].state == 1:
                        numberLeft += 1
                        scoreLeft += self.cases_tab[i][j].score
        return numberLeft, scoreLeft

    def compute_islands(self, players):
        dirs = [(1, -1), (2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1)]

        cases = self.cases_tab
        active_cases = [(x, y) for x in range(len(cases[0])) for y in range(len(cases)) if cases[y][x] != 0 and cases[y][x].state > 0]

        islands_list = []

        while active_cases != []:
            island_cases = []
            island_score = 0
            island_owners = []

            cur_case = active_cases[0]
            if cases[cur_case[1]][cur_case[0]].state == 2:
                island_owners.append(cases[cur_case[1]][cur_case[0]].owner)

            active_cases.remove(cur_case)
            island_cases.append(cur_case)
            island_score += cases[cur_case[1]][cur_case[0]].score

            reachable = [(cur_case[0] + d[0], cur_case[1] + d[1]) for d in dirs if (cur_case[0] + d[0], cur_case[1] + d[1]) in active_cases]

            while reachable != []:
                cur_case = reachable[0]
                if cases[cur_case[1]][cur_case[0]].state == 2 and cases[cur_case[1]][cur_case[0]].owner not in island_owners:
                    island_owners.append(cases[cur_case[1]][cur_case[0]].owner)

                reachable.remove(cur_case)
                active_cases.remove(cur_case)
                island_cases.append(cur_case)
                island_score += cases[cur_case[1]][cur_case[0]].score

                reachable += [(cur_case[0] + d[0], cur_case[1] + d[1]) for d in dirs if (cur_case[0] + d[0], cur_case[1] + d[1]) in active_cases and (cur_case[0] + d[0], cur_case[1] + d[1]) not in reachable]

            islands_list.append([island_owners, island_cases, island_score])
            
            for player_number in island_owners:
                for k in range(len(players[player_number].pawns)):
                    if (players[player_number].pawns[k].x, players[player_number].pawns[k].y) in island_cases:
                        players[player_number].pawns[k].island_number = len(islands_list)-1

        self.islands = islands_list

    def display(self, window, list=[[], []], l_init=-10, k_init=-10, z=0):
        sx, sy = case_width, case_height - case_height_margin
        table_but = [[0 for k in range(15)] for k in range(8)]

        for k in range(0, 8):
            n_case = 8 if k%2 ==0 else 7
            s = '' if k%2==0 else '  '
            real_l = 0

            for l in range(0, 15):
                if self.cases_tab[k][l] != 0:
                    if k == k_init and l == l_init:
                        c = self.cases_tab[k][l]
                        pos = [sx * real_l + mx + (k%2)*sx//2+((-1)**z)*3, sy * k + my+z*5]
                        real_l += 1
    
                        if c.state == 0:
                            s += '* '
                        elif c.owner != -1:
                            letter = chr(ord('a')+c.owner)
                            s += letter + ' '
                            if [l,k] in list[1]:
                                table_but[k][l] = Button(image_number_hint[c.score - 1], one, pos, 1)
                            else:
                                table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                            if (k!=k_init or l!=l_init):
                                window.blit(image_player[c.owner], (pos[0]+offset_x,pos[1]))
                                
                        elif [l,k] in list[1]:
                            s += str(c.score) + ' '
                            table_but[k][l] = Button(image_number_hint[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                            
                        elif [l,k] in list[0]:
                            s += str(c.score) + ' '
                            table_but[k][l] = Button(image_number_highlight[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                        else:
                            s += str(c.score) + ' '
                            table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                    else:
                        c = self.cases_tab[k][l]
                        pos = [sx * real_l + mx + (k%2)*sx//2, sy * k + my]
                        real_l += 1
    
                        if c.state == 0:
                            s += '* '
                        elif c.owner != -1:
                            letter = chr(ord('a')+c.owner)
                            s += letter + ' '
                            if [l,k] in list[1]:
                                table_but[k][l] = Button(image_number_hint[c.score - 1], one, pos, 1)
                            else:
                                table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                            if (k!=k_init or l!=l_init):
                                window.blit(image_player[c.owner], (pos[0]+offset_x,pos[1]))
                                
                        elif [l,k] in list[1]:
                            s += str(c.score) + ' '
                            table_but[k][l] = Button(image_number_hint[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                            
                        elif [l,k] in list[0]:
                            s += str(c.score) + ' '
                            table_but[k][l] = Button(image_number_highlight[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                        else:
                            s += str(c.score) + ' '
                            table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
        
        return table_but
        
    def display_end(self, window, l_init=-10, k_init=-10, z=0):
        sx, sy = case_width, case_height - case_height_margin
        table_but = [[0 for k in range(15)] for k in range(8)]

        for k in range(0, 8):
            n_case = 8 if k%2 == 0 else 7
            real_l = 0

            for l in range(0, 15):
                if self.cases_tab[k][l] != 0:
                    if k == k_init and l == l_init:
                        c = self.cases_tab[k][l]
                        pos = [sx * real_l + mx + (k%2)*sx//2+((-1)**z)*3, sy * k + my+z*5]
                        real_l += 1
    
                        if c.owner != -1:
                            table_but[k][l] = Button(image_cases_players[c.owner][c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                        else:
                            table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                    else:
                        c = self.cases_tab[k][l]
                        pos = [sx * real_l + mx + (k%2)*sx//2, sy * k + my]
                        real_l += 1
                        
                        if c.owner != -1:
                            table_but[k][l] = Button(image_cases_players[c.owner][c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])
                        else:
                            table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                            table_but[k][l].show(window, [0, 0])