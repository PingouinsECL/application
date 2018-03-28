import random
import pygame

from case import *
from button import *

from const import *

window = pygame.display.set_mode((0, 0))

one = pygame.image.load(path_one)
two = pygame.image.load(path_two)
three = pygame.image.load(path_three)

one_2 = pygame.image.load(path_one_2)
two_2 = pygame.image.load(path_two_2)
three_2 = pygame.image.load(path_three_2)


image_number_highlight = [one_2, two_2, three_2]

a = pygame.image.load(path_a)
b = pygame.image.load(path_b)
c = pygame.image.load(path_c)
d = pygame.image.load(path_d)
image_player = [a, b, c, d]

# Player 0
player001 = pygame.image.load(path_player001)
player002 = pygame.image.load(path_player002)
player003 = pygame.image.load(path_player003)

player011 = pygame.image.load(path_player011)
player012 = pygame.image.load(path_player012)
player013 = pygame.image.load(path_player013)

player021 = pygame.image.load(path_player021)
player022 = pygame.image.load(path_player022)
player023 = pygame.image.load(path_player023)

player031 = pygame.image.load(path_player031)
player032 = pygame.image.load(path_player032)
player033 = pygame.image.load(path_player033)

player041 = pygame.image.load(path_player041)
player042 = pygame.image.load(path_player042)
player043 = pygame.image.load(path_player043)

player051 = pygame.image.load(path_player051)
player052 = pygame.image.load(path_player052)
player053 = pygame.image.load(path_player053)


# Player 1
player101 = pygame.image.load(path_player101)
player102 = pygame.image.load(path_player102)
player103 = pygame.image.load(path_player103)

player111 = pygame.image.load(path_player111)
player112 = pygame.image.load(path_player112)
player113 = pygame.image.load(path_player113)

player121 = pygame.image.load(path_player121)
player122 = pygame.image.load(path_player122)
player123 = pygame.image.load(path_player123)

player131 = pygame.image.load(path_player131)
player132 = pygame.image.load(path_player132)
player133 = pygame.image.load(path_player133)

player141 = pygame.image.load(path_player141)
player142 = pygame.image.load(path_player142)
player143 = pygame.image.load(path_player143)

player151 = pygame.image.load(path_player151)
player152 = pygame.image.load(path_player152)
player153 = pygame.image.load(path_player153)


# Player 2
player201 = pygame.image.load(path_player201)
player202 = pygame.image.load(path_player202)
player203 = pygame.image.load(path_player203)

player211 = pygame.image.load(path_player211)
player212 = pygame.image.load(path_player212)
player213 = pygame.image.load(path_player213)

player221 = pygame.image.load(path_player221)
player222 = pygame.image.load(path_player222)
player223 = pygame.image.load(path_player223)

player231 = pygame.image.load(path_player231)
player232 = pygame.image.load(path_player232)
player233 = pygame.image.load(path_player233)

player241 = pygame.image.load(path_player241)
player242 = pygame.image.load(path_player242)
player243 = pygame.image.load(path_player243)

player251 = pygame.image.load(path_player251)
player252 = pygame.image.load(path_player252)
player253 = pygame.image.load(path_player253)



# Player 3
player301 = pygame.image.load(path_player301)
player302 = pygame.image.load(path_player302)
player303 = pygame.image.load(path_player303)

player311 = pygame.image.load(path_player311)
player312 = pygame.image.load(path_player312)
player313 = pygame.image.load(path_player313)

player321 = pygame.image.load(path_player321)
player322 = pygame.image.load(path_player322)
player323 = pygame.image.load(path_player323)

player331 = pygame.image.load(path_player331)
player332 = pygame.image.load(path_player332)
player333 = pygame.image.load(path_player333)

player341 = pygame.image.load(path_player341)
player342 = pygame.image.load(path_player342)
player343 = pygame.image.load(path_player343)

player351 = pygame.image.load(path_player351)
player352 = pygame.image.load(path_player352)
player353 = pygame.image.load(path_player353)




image_number = [one, two, three]
image_player = [player021,player121,player221,player321]

image_player_animation = [[[player001,player002,player003,player002],[player011,player012,player013,player012],[player021,player022,player023,player022],[player031,player032,player033,player032],[player041,player042,player043,player042],[player051,player052,player053,player052]],[[player101,player102,player103,player102],[player111,player112,player113,player112],[player121,player122,player123,player122],[player131,player132,player133,player132],[player141,player142,player143,player142],[player151,player152,player153,player152]],[[player201,player202,player203,player202],[player211,player212,player213,player212],[player221,player222,player223,player222],[player231,player232,player233,player232],[player241,player242,player243,player242],[player251,player252,player253,player252]],[[player301,player302,player303,player302],[player311,player312,player313,player312],[player321,player322,player323,player322],[player331,player332,player333,player332],[player341,player342,player343,player342],[player351,player352,player353,player352]]]
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
            island_score = 0   
            occupied = []

            cur_case = active_cases[0]
            if cases[cur_case[1]][cur_case[0]].state == 2:
                occupied.append(cases[cur_case[1]][cur_case[0]].owner)

            active_cases.remove(cur_case)
            cur_island.append(cur_case)
            island_score += cases[cur_case[1]][cur_case[0]].score

            reachable = [(cur_case[0] + d[0], cur_case[1] + d[1]) for d in dirs if (cur_case[0] + d[0], cur_case[1] + d[1]) in active_cases]

            while reachable != []:
                cur_case = reachable[0]
                if cases[cur_case[1]][cur_case[0]].state == 2 and cases[cur_case[1]][cur_case[0]].owner not in occupied:
                    occupied.append(cases[cur_case[1]][cur_case[0]].owner)

                reachable.remove(cur_case)
                active_cases.remove(cur_case)
                cur_island.append(cur_case)
                island_score +=cases[cur_case[1]][cur_case[0]].score

                reachable += [(cur_case[0] + d[0], cur_case[1] + d[1]) for d in dirs if (cur_case[0] + d[0], cur_case[1] + d[1]) in active_cases and (cur_case[0] + d[0], cur_case[1] + d[1]) not in reachable]

            islands_list.append([occupied, cur_island, island_score])

        self.islands = islands_list


    def display(self, window, list=[],l_init=-10, k_init=-10):

        sx, sy = case_width, case_height - case_height_margin
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
                        table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                        table_but[k][l].show(window, [0, 0])
                        if (k!=k_init or l!=l_init):
                            window.blit(image_player[c.owner], (pos[0],pos[1]))
                    elif [l,k] in list:
                        s += str(c.score) + ' '
                        table_but[k][l] = Button(image_number_highlight[c.score - 1], one, pos, 1)
                        table_but[k][l].show(window, [0, 0])
                    else:
                        s += str(c.score) + ' '
                        table_but[k][l] = Button(image_number[c.score - 1], one, pos, 1)
                        table_but[k][l].show(window, [0, 0])

            # print(s)
        return table_but

