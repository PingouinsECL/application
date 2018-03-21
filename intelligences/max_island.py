def max_island(board, players, p, pawns_on_island, max_point):

    maxi = players[p].score + max_point
    def max_island_rec() :
        nb_pawns = len(pawns_on_island)
        i = 0
        players[p].pawns[pawns_on_island[i]].compute_accessible_island(board)
        while i < nb_pawns and players[p].pawns[pawns_on_island[i]].accessibles == [0]*6 :
            i += 1
            if i < nb_pawns :
                players[p].pawns[pawns_on_island[i]].compute_accessible_island(board)
        if i == nb_pawns:
            sc = players[p].score
            for i in pawns_on_island:
                sc += board.cases_tab[players[p].pawns[i].y][players[p].pawns[i].x].score
            return sc, []
        v = players[p].score

        for i in pawns_on_island :
            players[p].pawns[i].compute_accessible_island(board)
            acce = players[p].pawns[i].accessibles
            for j in range(len(acce)):
                for k in range(1, 1+acce[j], max(1, acce[j]-1)) :
                    players[p].pawns[i].move(board, players[p], j, k)
                    (w, list_actions) = max_island_rec()
                    players[p].pawns[i].anti_move(board, players[p], j, k)
                    if w == maxi:
                        list_actions.append([j, k, i])
                        return w, list_actions
                    if w > v:
                        v = w
                        action = list_actions[:]
                        action.append([j, k, i])
        return v, action
    return max_island_rec()[1]