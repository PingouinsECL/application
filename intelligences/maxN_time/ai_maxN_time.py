from time import clock
from random import choice

def ai_maxN_time (board, players, player_number, t_max) :
    """
    Maxn algorith applied to the 2 to 4 players in this game.
    """
    number_h = 0  # Choice of the heuristic
    t_f = clock() + t_max
    sum = 100 # Nombre de points total sur le plateau
    nb_pawns = len(players[player_number].pawns)
    
    def terminate () :
        """
        Return a boolean telling if the given time is elapsed.
        """
        nonlocal t_f
        return (clock() > t_f)
    
    def heuristique () :
        # Heuristique donnant les pseudo-scores de chaque joueur
        nonlocal board, players, number_h, nb_pawns
        rep = []
        for p in range (len(players)) :
            s = players[p].score
            for q in range (nb_pawns) :
                s += board.cases_tab[players[p].pawns[q].y][players[p].pawns[q].x].score
            rep.append(s)
        if number_h == 0 : # Mode 0 : chaque joueur maximise son score ☺
            return (rep)
        elif number_h == 1 : # Mode : chaque joueur maximise son score tout en minimisant la somme des scores des autres joueurs (poids identiques sur ces 2 facteurs)
            s = sum(rep)
            return ([2*rep[p]-s for p in range (len(players))])
        elif number_h == 2 : # Mode : chaque joueur maximise son score tout en minimisant le max des scores des autres joueurs (poids identiques sur ces 2 facteurs)
            m = max(rep)
            l = [i for i, j in enumerate(rep) if j == m]
            for p in range (len(players)) :
                if p in l and len(l) == 1 :
                    ll = l[:]
                    del l[p]
                    rep[p] -= max(ll)
                else :
                    rep[p] -= m
            return ([2*rep[p]-s for p in range (len(players))])
        # Mode minimiser le score d'un autre joueur ?
        # Mode maximiser le score d'un autre joueur ?
        # Mode bloquer les pions d'un joueur ? Ne pas bloquer ses pions ?
        # Faire des mixtes

    def max_value (p, d, bound, r = 0) :
        """
        Maximise the points of player p given by the heuristic chosen.
        """
        nonlocal board, players, sum, d_max, nb_pawns
        if d == 0 or r == len(players) :
            return (heuristique ())
        
        next_p = (p+1)%len(players) # Next player
        
        iu = 0
        players[p].pawns[iu].compute_accessible_like (board)
        while iu < nb_pawns and players[p].pawns[iu].accessibles == [0]*6 :
            iu += 1
            if iu < nb_pawns :
                players[p].pawns[iu].compute_accessible_like (board)
        if iu ==  nb_pawns :
            return (max_value (next_p, d-1, sum, r = r + 1))
        
        if terminate () :
            return (None)
        acce = players[p].pawns[iu].accessibles
        ju = 0
        while acce[ju] == 0 :
            ju += 1
        players[p].pawns[iu].move (board, players[p], ju, 1)
        v = max_value (next_p, d-1, sum)
        players[p].pawns[iu].anti_move (board, players[p], ju, 1)
        if v == None :
            return (None)
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
                        return (action[randint(0, len(v)-1)] if d == d_max else v[randint(0, len(v)-1)])
                    if terminate () :
                        return (None)
                    if not (i == iu and (j < ju or (j == ju and k == 1))) : # Chemins déja explorés
                        players[p].pawns[i].move (board, players[p], j, k)
                        w = max_value (next_p, d-1, sum - v[0][p])
                        players[p].pawns[i].anti_move (board, players[p], j, k)
                        if w == None :
                            return (None)
                        if v[0][p] == w[p] : # Cas d'égalité : on choisit une solution au hasard ; limiter le max des scores des autres ? leur somme ? autre chose ?
                            if d == d_max :
                                action.append([j, k, i])
                            v.append(w[:])
                        elif v[0][p] < w[p] :
                            if d == d_max :
                                action = [[j, k, i]]
                            v = [w[:]]
        return (choice(action) if d == d_max else choice(v))
    
    d_max = 1
    action = max_value (player_number, d_max, sum)
    while not terminate () :
        d_max += 1
        ac = max_value (player_number, d_max, sum)
        if ac != None :
            action = ac
    return (action)