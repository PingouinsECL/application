import random

def ai_random(N, players, board, list_number_pawns, number_pawns):


    # choix du numéro du pion
    random.shuffle(list_number_pawns)
    pawn_number = list_number_pawns[0]

    # choix de la direction
    etat_pawn = players[N].pawns[pawn_number].accessibles

    directions_possibles = [k for k in range(len(etat_pawn)) if etat_pawn[k] != 0]
    random_indice = random.randint(0, len(directions_possibles)-1)
    direction = directions_possibles[random_indice]

    # choix de la distance
    dist_max = etat_pawn[direction]
    dist = random.randint(1, dist_max)

    return direction, dist, pawn_number
