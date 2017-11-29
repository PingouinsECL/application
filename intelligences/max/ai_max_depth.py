def ai_max (N, players, board, list_number_pawns, d_max) :
    """
    Pseudo-minimax algorith applied to the 2 to 4 players in this game.
    """
    
    def max_value (new_board, p, d) :
        """
        Maximise the points of player p given by the heuristic chosen.
        """
        
        if d == 0 : #rajouter "ou partie finie" ?
            return heuristique(0) # choisir heuristique
        
        next_p = (p+1)%Player.number_player
        v = [0 for _ in range (N)]
        action = None
        for i in list_number_pawns :
            acce = players[p].pawns[i].accessibles
            for j in range(len(acce)) :
                for k in range (acce[j]) :
                    new2_board = [[new_board[i][j] for j in range(len(new_board[0]))] for i in range(len(new_board))]
                    i.move (new2_board, p, j, k)
                    w = max_value(new2_board, next_p, d-1)[0]
                    p.score -= board.cases_tab[i.x][i.y].score
                    if v[p] < w[p] : # rajouter un choix en cas d'égalité ? limiter le max des scores des autres ? leur somme ? autre chose ?
                        action = [j, k, i]
                        v = w.copy()
        return v, action
    
    return max_value(board, N, d_max)[1]

def heuristique (i) :
    # Heuristique donnant les pseudo-scores de chaque joueur
    if i == 0 : # Mode maximiser son score ☺
        return [players[i].score for i in range (N)], None
    elif i == 1 : # Mode minimiser le score d'un autre joueur ?
        return[p , None # Mode maximiser le score d'un autre joueur ?
    # Mode bloquer les pions d'un joueur ? Ne pas bloquer ses pions ?
    #Faire des mixtes
