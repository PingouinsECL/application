def make_input(players, board, number_player, pawn_number):
    
    dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]
    
    owners, island_cases, score = board.islands[players[number_player].pawns[pawn_number].island_number]
    
    # calcul du score faisable en un coup par chacun des pions sur l'île
    score_accessible = 0
    number_accessible = 0
    
    x, y = players[number_player].pawns[pawn_number].x, players[number_player].pawns[pawn_number].y

    for direction, dist in enumerate(players[number_player].pawns[pawn_number].accessibles):
        dx, dy = dirs[direction]
        for d in range(1, dist+1):
            score_accessible += board.cases_tab[y][x].score
            number_accessible += 1

    # calcul du nombre total de pions sur l'île
    number_on_island = 0
    for k in range(len(players)):
        if k in owners:
            for p in range(len(players[k].pawns)):
                if (players[k].pawns[p].x, players[k].pawns[p].y) in island_cases:
                    number_on_island += 1

    return [score, number_on_island, score_accessible, number_accessible]

def compute_input(players, board, number_player, not_isolated_pawns):
    inputs = []
    
    for k in not_isolated_pawns:
        inputs.append(make_input(players, board, number_player, k))
    
    return inputs

def compute_output(model, inputs):
    try:
        len(inputs[0])
    except:
        inputs = [inputs]
    if inputs != [[]]:
        return model.predict(inputs)
    else:
        return []
  
def anticipate_score(model, board, players, player_number):
    anticipated_score = players[player_number].score # current score
        
    isolated_pawns_indices = []
    board.compute_islands(players)

    for k, (owners, _, score) in enumerate(board.islands): # score on isolated pawns
        if owners == [player_number]:
            anticipated_score += score
            for l in range(len(players[player_number].pawns)):
                if players[player_number].pawns[l].island_number == k:
                    isolated_pawns_indices.append(l)
                    
    not_isolated_pawns_indices = [k for k in range(len(players[player_number].pawns)) if k not in isolated_pawns_indices]

    inputs = compute_input(players, board, player_number, not_isolated_pawns_indices)
    anticipated_score += sum(compute_output(model, inputs))
    
    return anticipated_score