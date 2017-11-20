import random

def ai_random(N, players, board):
    # calcul des possibles

    for i in range(len(players[N].pawns)):
        players[N].pawns[i].compute_accessible(board)

    # choix du numéro du pion
    pawn_number = random.randint(0, len(players[N].pawns)-1)

    # choix de la direction
    etat_pawn = players[N].pawns[pawn_number].accessibles

    print(etat_pawn)
    if(etat_pawn == [0]*6):
        fail = True
        direction = 0
        dist = 0
        pawn_number = 0
    else:
        fail = False
        directions_possibles = [k for k in range(len(etat_pawn)) if etat_pawn[k] != 0]
        random_indice = random.randint(0, len(directions_possibles)-1)
        direction = directions_possibles[random_indice]

        # choix de la distance
        dist_max = etat_pawn[direction]
        dist = random.randint(1, dist_max)

    return fail, direction, dist, pawn_number
