
import time

def ai_alphabeta (board, players, player_number, adversary_number, t_max) :
    """
    Minmax algorith with alphabeta applied to the only 2 players in this game.
    """
    t_f = time.clock() + t_max
    nb_pawns = len(players[player_number].pawns)
    
    def terminate () :
        """
        Return a boolean telling if the given time is elapsed.
        """
        nonlocal t_f
        return (time.clock() > t_f)
    
    def evaluate () :
        """
        Differential score up to this point.
        """
        nonlocal board, players, player_number, adversary_number
        value = players[player_number].score - players[adversary_number].score
        for q in range (len(players[player_number].pawns)) :
            value += board.cases_tab[players[player_number].pawns[q].y][players[player_number].pawns[q].x].score
            value -= board.cases_tab[players[adversary_number].pawns[q].y][players[adversary_number].pawns[q].x].score
        return (value)

    def max_value (d, min, max, r = 0, root = False) :
        """
        Maximise the differential score.
        """
        nonlocal board, players, player_number, nb_pawns
        if d == 0 or r == 2 :
            return (evaluate ())
        if terminate () :
            return (None)

        iu = 0
        players[player_number].pawns[iu].compute_accessible_like (board)
        while iu < nb_pawns and players[player_number].pawns[iu].accessibles == [0]*6 :
            iu += 1
            if iu < nb_pawns :
                players[player_number].pawns[iu].compute_accessible_like (board)
        if iu ==  nb_pawns :
            return (min_value (d-1, min, max, r = r + 1))
        
        acce = players[player_number].pawns[iu].accessibles[:]
        v = min
        
        for i in range(iu, len(players[player_number].pawns)) :
            if i != iu :
                players[player_number].pawns[i].compute_accessible_like (board)
                acce = players[player_number].pawns[i].accessibles
            for j in range(len(acce)) :
                for k in range (1,acce[j]+1) :
                    if terminate () :
                        return (None)
                    players[player_number].pawns[i].move (board, players[player_number], j, k)
                    w = min_value (d-1, v, max)
                    players[player_number].pawns[i].anti_move (board, players[player_number], j, k)
                    if w == None :
                        return (None)
                    if v < w : # rajouter un choix en cas d'égalité ? choix aléatoire ?
                        v = w
                        if v > max :
                            return max
                        if root :
                            action = [j, k, i]
        return (action if root else v)
    
    def min_value (d, min, max, r = 0) :
        """
        Minimise the differential score.
        """
        nonlocal board, players, adversary_number, nb_pawns
        if d == 0 or r == 2 :
            return (evaluate ())
        if terminate () :
            return (None)

        iu = 0
        players[adversary_number].pawns[iu].compute_accessible_like (board)
        while iu < nb_pawns and players[adversary_number].pawns[iu].accessibles == [0]*6 :
            iu += 1
            if iu < nb_pawns :
                players[adversary_number].pawns[iu].compute_accessible_like (board)
        if iu ==  nb_pawns :
            return (min_value (d-1, min, max, r = r + 1))
        
        acce = players[adversary_number].pawns[iu].accessibles[:]
        v = max
        
        for i in range(iu, len(players[adversary_number].pawns)) :
            if i != iu :
                players[adversary_number].pawns[i].compute_accessible_like (board)
                acce = players[adversary_number].pawns[i].accessibles
            for j in range(len(acce)) :
                for k in range (1,acce[j]+1) :
                    if terminate () :
                        return (None)
                    players[adversary_number].pawns[i].move (board, players[adversary_number], j, k)
                    w = max_value (d-1, min, v)
                    players[adversary_number].pawns[i].anti_move (board, players[adversary_number], j, k)
                    if w == None :
                        return (None)
                    if v > w : # rajouter un choix en cas d'égalité ? choix aléatoire ?
                        v = w
                        if v < min :
                            return min
        return (v)
    
    d_max = 1
    action = max_value (d_max, -float('inf'), float('inf'), root = True)
    while not terminate () :
        d_max += 1
        ac = max_value (d_max, -float('inf'), float('inf'), root = True)
        if ac != None :
            action = ac
return (action)
