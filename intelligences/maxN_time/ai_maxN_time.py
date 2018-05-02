from time import clock
from random import choice

def ai_maxN_time (board, players, player_number, t_max, number_h = 0) :
    """
    Maxn algorith applied to the 2 to 4 players in this game.
    """
    #number_h = 3  # Choice of the heuristic
    t_f = clock() + t_max
    somme = 100 # Nombre de points total sur le plateau
    nb_pawns = len(players[player_number].pawns)
    
    def terminate () :
        """
        Return a boolean telling if the given time is elapsed.
        """
        nonlocal t_f
        return clock() > t_f
    
    def heuristique () :
        # Heuristique donnant les pseudo-scores de chaque joueur
        nonlocal board, players, number_h, nb_pawns, player_number
        rep = [] # Effective scores of the players (with the points of the case they are on)
        for p in range (len(players)) :
            s = players[p].score
            for q in range (nb_pawns) :
                s += board.cases_tab[players[p].pawns[q].y][players[p].pawns[q].x].score
            rep.append(s)
        if number_h == 0 : # Mode 0 : chaque joueur maximise son score
            return rep
        elif number_h == 1 : # Mode 1 : chaque joueur maximise son score tout en minimisant la somme des scores des autres joueurs (poids identiques sur ces 2 facteurs)
            s = sum(rep)
            return [2*rep[p]-s for p in range (len(players))]
        elif number_h == 2 : # Mode 2 : chaque joueur maximise son score tout en minimisant le max des scores des autres joueurs (poids identiques sur ces 2 facteurs)
            m = max(rep)
            l = [i for i, j in enumerate(rep) if j == m]
            for p in range (len(players)) :
                if p in l and len(l) == 1 :
                    ll = l[:]
                    del ll[p]
                    rep[p] -= max(ll)
                else :
                    rep[p] -= m
            return [rep[p] for p in range (len(players))]
        elif number_h == 3 : # Mode 3 : bloquer les pions des autres joueurs, qui eux maximisent leurs scores
            for p in range (len(players)) :
                if p != player_number :
                    for pawn in players[p].pawns :
                        if pawn.active :
                            rep[player_number] -= 100
            return rep
        # Mode minimiser le score d'un autre joueur ? autres joueurs maximisent normal
        # Mode maximiser le score d'un autre joueur ?
        # maximiser la différence ses points – points joueur
        # Faire des mixtes

    def max_value (p, d, bound, r = 0) :
        """
        Maximise the points of player p given by the heuristic chosen.
        """
        nonlocal board, players, somme, d_max, nb_pawns
        if d == 0 or r == len(players) :
            return heuristique ()
        
        next_p = (p+1)%len(players) # Next player
        
        iu = 0
        players[p].pawns[iu].compute_accessible_like (board)
        while iu < nb_pawns and players[p].pawns[iu].accessibles == [0]*6 :
            iu += 1
            if iu < nb_pawns :
                players[p].pawns[iu].compute_accessible_like (board)
        if iu ==  nb_pawns :
            return max_value (next_p, d-1, somme, r = r + 1)
        
        if terminate () :
            return
        acce = players[p].pawns[iu].accessibles
        ju = 0
        while acce[ju] == 0 :
            ju += 1
        players[p].pawns[iu].move (board, players[p], ju, 1)
        v = max_value (next_p, d-1, somme)
        players[p].pawns[iu].anti_move (board, players[p], ju, 1)
        if v == None :
            return
        v = [v]
        if d == d_max :
            action = [[ju, 1, iu]]
        
        for i in range(iu, nb_pawns) :
            if i != iu :
                players[p].pawns[i].compute_accessible_like (board)
                acce = players[p].pawns[i].accessibles
            for j in range(len(acce)) :
                for k in range (1,acce[j]+1) :
                    if v[0][p] >= bound :
                        return choice(action) if d == d_max else choice(v)
                    if terminate () :
                        return
                    if not (i == iu and (j < ju or (j == ju and k == 1))) : # Chemins déja explorés
                        players[p].pawns[i].move (board, players[p], j, k)
                        w = max_value (next_p, d-1, somme - v[0][p])
                        players[p].pawns[i].anti_move (board, players[p], j, k)
                        if w == None :
                            return
                        if v[0][p] == w[p] : # Cas d'égalité : on choisit une solution au hasard ; limiter le max des scores des autres ? leur somme ? autre chose ?
                            if d == d_max :
                                action.append([j, k, i])
                            v.append(w[:])
                        elif v[0][p] < w[p] :
                            if d == d_max :
                                action = [[j, k, i]]
                            v = [w[:]]
        return choice(action) if d == d_max else choice(v)
    
    d_max = 1
    action = max_value (player_number, d_max, somme)
    while not terminate () :
        d_max += 1
        ac = max_value (player_number, d_max, somme)
        if ac != None :
            action = ac
    return action