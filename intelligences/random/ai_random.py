import random

def ai_random(players, player_number, list_active_pawns):

    # choix du numéro du pion
    random.shuffle(list_active_pawns)
    pawn_number = list_active_pawns[0]

    # choix de la direction
    accessibles_pawn = players[player_number].pawns[pawn_number].accessibles

    directions_possibles = [k for k in range(len(accessibles_pawn)) if accessibles_pawn[k] != 0]
    random_indice = random.randint(0, len(directions_possibles)-1)
    direction = directions_possibles[random_indice]

    # choix de la distance
    dist_max = accessibles_pawn[direction]
    dist = random.randint(1, dist_max)

    return direction, dist, pawn_number
