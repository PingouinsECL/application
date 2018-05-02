from ai_maxN_time import *
tmax = 3

def ai_impaler (board, players, player_number, adversary_number, list_active_pawns) :
    """
    Try to block the pawns of the player adversary_number.
    If it can not, try to move a pawn in order to be able to do it later.
    """
    def adjacence (x, y) :
        """
        Give the coordonates of the cases next to the case of coordonates (x,y),
        whether they are still here or not.
        Return a list of coordonates.
        """
        nonlocal board
        h, w = len(board.cases_tab), len(board.cases_tab[0])
        ad = []
        for [dx, dy] in [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]] :
            try :
                if h > y+dy >= 0 and w > x+dx >= 0 and board.cases_tab[y+dy][x+dx].state == 1 :
                    ad.append((x+dx, y+dy))
            except AttributeError :
                pass
        return ad
    
    def path_to (case) :
        """
        Give all the case from which we can go to the considered case.
        """
        nonlocal board
        h, w = len(board.cases_tab), len(board.cases_tab[0])
        (x, y) = case
        ad = []
        for [dx, dy] in [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]] :
            for i in range (1, 8) : # The maximal distance per move is 7.
                try :
                    if h > y+i*dy >= 0 and w > x+i*dx >= 0 and board.cases_tab[y+i*dy][x+i*dx].state == 1 :
                        ad.append((x+i*dx, y+i*dy))
                except AttributeError :
                    pass
        return ad

    def list_access (pawn) :
        """
        Give the list of the accessible cases for the pawn.
        """
        nonlocal board
        dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]
        list = []
        for i in range(6) :
            for h in range(1, pawn.accessibles[i]+1) :
                list.append([pawn.x+h*dirs[i][0],pawn.y+h*dirs[i][1]])
        return list
    
    def getDirDist(x_pawn, y_pawn, x_aim, y_aim) :
        """
        Give the number of the direction and the distance to go from the current case to the aim.
        """
        dx = x_aim - x_pawn
        dy = y_aim - y_pawn

        if dx > 0 and dy < 0 and -dy//dx == -dy/dx :
            return 0, -dy
        if dy == 0 and dx > 0:
            return 1, dx//2
        if dx > 0 and dy > 0 and dy//dx == dy/dx :
            return 2, dy
        if dx < 0 and dy > 0 and -dy//dx == -dy/dx :
            return 3, dy
        if dy == 0 and dx < 0:
            return 4, -dx//2
        if dx < 0 and dy < 0 and dy//dx == dy/dx :
            return 5, -dy
    
    nb_pawns = len(players[player_number].pawns)
    paths = [] # (p, [(x,y)]) is where the p pawn can go
    for i in range(nb_pawns) :
        paths.append ((i, list_access(players[player_number].pawns[i])))
    
    targets = [] # (c, [(x,y)]) is adjacency cases of pawn c
    places = [] # Number of escapes for each pawn
    for c in range(nb_pawns) :
        try :
            a = adjacence(players[adversary_number].pawns[c].x, players[adversary_number].pawns[c].y)
        except IndexError :
            return ai_maxN_time (board, players, player_number, tmax)
        targets.append((c, a))
        places.append((len(a), c))
    
    def target_to_attacks (targets) :
        """
        Find and chose a pawn to attack and how attack it with the targets' list.
        """
        def find_attacks (targets) :
            """
            With the targets chosen and the paths of each attacker, find the attacks
            and the number of attacks per pawn.
            """
            nonlocal nb_pawns, paths
            attacks = [[]]*nb_pawns # Attacks on each pawn
            attacked = [False]*nb_pawns # If a pawn can be attacked
            nb_of_possible_attacks = [0]*nb_pawns # Number of attacks of each pawn
            
            for (p, l) in paths :
                for (x, y) in l :
                    for (c, m) in targets :
                        if (x, y) in m :
                            attacks[c].append((p, (x,y))) # Attacker p, cible c, case (x, y)
                            attacked[c] = True
                            nb_of_possible_attacks[p] += 1
            return attacks, attacked, nb_of_possible_attacks
        
        def chose_attack (attacks, attacked, places) :
            """
            Choice of the attack : always attack the weakest (the one who can escape the less).
            Return None if no attack found.
            """
            places = sorted(places)
            for (_, c) in places :
                if attacked[c] : 
                    return attacks[c]
        
        attacks, attacked, nb_of_possible_attacks = find_attacks (targets)
        campane = chose_attack (attacks, attacked, places)
        return campane, nb_of_possible_attacks
    
    campane, nb_of_possible_attacks = target_to_attacks (targets)
    
    n = 0 # In case there will never be any possible attack
    while campane == None and n < 10 : # The 10 is arbitrary
        # If it can not attack, then it will try to put a pawn in an attack stance
        new_targets = []
        for (c, l_case) in targets :
            a = []
            for case in l_case :
                a.extend(path_to(case))
            new_targets.append((c, a))
            places.append((len(a), c))
        targets = [(c, l[:]) for (c, l) in new_targets]
        
        campane, nb_of_possible_attacks = target_to_attacks (targets)
        n += 1
            
    if campane != None :
        # If an attack is possible
        attacker, land, min = -1, (-1, -1),  100
        for (p, (x,y)) in campane :
            if nb_of_possible_attacks[p] < min :
                attacker, land, min = p, (x,y), nb_of_possible_attacks[p]
        j, k = getDirDist(players[player_number].pawns[attacker].x, players[player_number].pawns[attacker].y, land[0], land[1])
        return [j, k, attacker]
    
    # If no attack has been found : maxn
    return ai_maxN_time (board, players, player_number, tmax)