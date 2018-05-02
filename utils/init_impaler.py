from random import choice
from init_random import *

def init_impaler (board, players, adversary_number) :
    
    def adjacence (case) :
        """
        Give the coordonates of the cases next to the case of coordonates (x,y),
        whether they are still here or not.
        Return a list of coordonates.
        """
        nonlocal board
        (x, y) = case
        ad = []
        for [dx, dy] in [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]] :
            try :
                if y+dy >= 0 and x+dx >= 0 and board.cases_tab[y+dy][x+dx].state == 1 :
                    ad.append((x+dx, y+dy))
            except :
                pass
        return ad
    
    def path_to (case) :
        """
        Give all the case from which we can go to the considered case.
        """
        nonlocal board
        (x, y) = case
        ad = []
        for [dx, dy] in [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]] :
            for i in range (1, 8) : # The maximal distance per move is 7.
                try :
                    if y+i*dy >= 0 and x+i*dx >= 0 and board.cases_tab[y+i*dy][x+i*dx].state == 1 :
                        ad.append((x+i*dx, y+i*dy))
                except :
                    pass
        return ad
    
    targets = [(pawn.x, pawn.y) for pawn in players[adversary_number].pawns]
    attacks = {}
    obstacles = {}
    campane = []
    max = 0
    for case in targets :
        if case != (-1, -1) :
            for c in adjacence(case) :
                if board.cases_tab[case[1]][case[0]] == 1 :
                    try :
                        attacks[c] += 1
                    except KeyError :
                        attacks[case] = 1
                    if attacks[c] > max :
                        max += 1
                        campane = [c]
                    elif attacks[c] == max :
                        campane.append(c)
    if max != 0 :
        return choice(campane)
    
    for case in targets :
        if case != (-1, -1) :
            for c in path_to(case) :
                if board.cases_tab[case[1]][case[0]] == 1 :
                    try :
                        attacks[c] += 1
                    except KeyError :
                        attacks[case] = 1
                    if attacks[c] > max :
                        max += 1
                        campane = [c]
                    elif attacks[c] == max :
                        campane.append(c)
    if max != 0 :
        return choice(campane)
    
    return init_random (board)