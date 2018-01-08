import copy

def ai_max (N, players, board, d_max) :
    """
    Pseudo-minimax algorith applied to the 2 to 4 players in this game.
    """
    
    def heuristique (i) :
        # Heuristique donnant les pseudo-scores de chaque joueur
        if i == 0 : # Mode maximiser son score ☺
            return [players[p].score for p in range (len(players))]
        # Mode minimiser le score d'un autre joueur ?
        # Mode maximiser le score d'un autre joueur ?
        # Mode bloquer les pions d'un joueur ? Ne pas bloquer ses pions ?
        #Faire des mixtes
    
    def compute_accessible_like(pawn, board):
        if pawn.active:
            x = pawn.x
            y = pawn.y

            dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]

            def advance(x, y, dx, dy):
                k = 0
                while 0 <= x+dx < 15 and 0 <= y+dy < 8 and \
                    board.cases_tab[y+dy][x+dx].state == 1:
                    k += 1
                    x += dx
                    y += dy
                return k

            max_per_dir = []

            for (dx, dy) in dirs:
                max_per_dir.append(advance(x, y, dx, dy))

            pawn.accessibles = max_per_dir

            if pawn.accessibles == [0, 0, 0, 0, 0, 0]:
                pawn.remain = 0
            else:
                pawn.remain = 1
    
    def max_value (p, board, d) :
        """
        Maximise the points of player p given by the heuristic chosen.
        """
        if d == 0 :
            return heuristique(0) # Choice of the heuristic
        
        next_p = (p+1)%len(players) # Next player
        for i in range (len(players[p].pawns)):
            compute_accessible_like (players[p].pawns[i], board)
        
        i = 0
        while i < len(players[p].pawns) and players[p].pawns[i].remain == 0 :
            i += 1
        if i ==  len(players[p].pawns):
            return (max_value (next_p, board,  d-1))
        
        v = [0 for _ in range (len(players))]
        for i in range (len(players[p].pawns)):
            acce = players[p].pawns[i].accessibles
            for j in range(len(acce)) :
                for k in range (1,acce[j]+1) :
                    players[p].pawns[i].move (board, players[p], j, k)
                    w = max_value (next_p, board,  d-1)
                    players[p].pawns[i].anti_move (board, players[p], j, k)
                    if v[p] <= w[p] : # rajouter un choix en cas d'égalité ? limiter le max des scores des autres ? leur somme ? autre chose ?
                        if d == d_max :
                            action = [j, k, i]
                        v = copy.copy(w)
        return (action if d == d_max else v)
    
    action = max_value(N, board, d_max)
    return (action)
