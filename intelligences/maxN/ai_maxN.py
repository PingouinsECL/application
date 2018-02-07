def ai_maxN (board, players, player_number, d_max) :
    """
    Maxn algorith applied to the 2 to 4 players in this game.
    """
    
    def heuristique (i) :
        # Heuristique donnant les pseudo-scores de chaque joueur
        rep = []
        for p in range (len(players)) :
            s = players[p].score
            for q in range (len(players[p].pawns)) :
                s += board.cases_tab[players[p].pawns[q].y][players[p].pawns[q].x].score
            rep.append(s)
        if i == 0 : # Mode 0 : chaque joueur maximise son score ☺
            return (rep)
        elif i == 1 : # Mode : chaque joueur maximise son score tout en minimisant la somme des scores des autres joueurs (poids identiques sur ces 2 facteurs)
            s = sum(rep)
            return ([2*rep[p]-s for p in range (len(players))])
        elif i == 2 : # Mode : chaque joueur maximise son score tout en minimisant le max des scores des autres joueurs (poids identiques sur ces 2 facteurs)
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
    
    def max_value (p, d) :
        """
        Maximise the points of player p given by the heuristic chosen.
        """
        if d == 0 :
            return heuristique (0) # Choice of the heuristic
        
        next_p = (p+1)%len(players) # Next player
        for i in range (len(players[p].pawns)):
            players[p].pawns[i].compute_accessible_like (board)
        
        i = 0
        while i < len(players[p].pawns) and players[p].pawns[i].accessibles == [0]*6 :
            i += 1
        if i ==  len(players[p].pawns) :
            return (max_value (next_p, d-1))
        
        v = [0] * len(players)
        for i in range (len(players[p].pawns)) :
            acce = players[p].pawns[i].accessibles
            for j in range(len(acce)) :
                for k in range (1,acce[j]+1) :
                    players[p].pawns[i].move (board, players[p], j, k)
                    w = max_value (next_p, d-1)
                    players[p].pawns[i].anti_move (board, players[p], j, k)
                    if v[p] <= w[p] : # rajouter un choix en cas d'égalité ? limiter le max des scores des autres ? leur somme ? autre chose ?
                        if d == d_max :
                            action = [j, k, i]
                        v = w[:]
        return (action if d == d_max else v)
    
    return (max_value (player_number, d_max))