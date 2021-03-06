from time import clock

def update_islands(board, players, recalculate):
    board.compute_islands(players)
    for island in board.islands:
        occupiers, island_cases, score = island
        if occupiers == []:
            for (x, y) in island_cases:
                board.cases_tab[y][x].change_state(0)
        if len(occupiers) == 1:
            if len(island_cases)!=1:
                pawns_on_island = []
                calc = False
                for i in range(len(players[occupiers[0]].pawns)):
                    pawn = players[occupiers[0]].pawns[i]
                    if (pawn.x,pawn.y) in island_cases:
                        if pawn.isolate == False or recalculate:
                            pawn.isolate = True
                            pawns_on_island.append(i)
                        else:
                            calc = True
                            break
                if not calc or recalculate:
                    m_island = max_island(board,players,occupiers[0],pawns_on_island, score)
                    if m_island == False:
                        for i in pawns_on_island:
                            players[occupiers[0]].pawns[i].isolate = False    
                    else:
                        for i in pawns_on_island:
                            players[occupiers[0]].pawns[i].remaining_actions = m_island 

def max_island(board, players, p, pawns_on_island, max_point):

    maxi = players[p].score + max_point
    time_a = clock()
    def max_island_rec() :
        if clock() > time_a + 10:
            return [[],False]
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
                    result = max_island_rec()
                    players[p].pawns[i].anti_move(board, players[p], j, k)
                    if result[1] == False:
                        return [[],False]
                    (w, list_actions) = result
                    if w == maxi:
                        list_actions.append([j, k, i])
                        return w, list_actions
                    if w > v:
                        v = w
                        action = list_actions[:]
                        action.append([j, k, i])
        return v, action
    return max_island_rec()[1]