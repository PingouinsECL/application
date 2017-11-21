import random

def ai_random(N, players, board):

    number_pawns = len(players[N].pawns)

    # calcul des possibles
    for i in range(number_pawns):
        players[N].pawns[i].compute_accessible(board)

    # activite des pions et suppression des pions isoles
    to_delete = []
    for k in range(number_pawns):
        if players[N].pawns[k].accessibles == [0]*6:
            print('Le pion ', k, ' du joueur ', N, ' TOMBE à l\'eau')
            to_delete.append(k)

    to_delete = to_delete[::-1]
    number_pawns -= len(to_delete)
    for i in to_delete:
        del players[N].pawns[i]

    # decision

    if number_pawns == 0:
        fail = True
        direction = 0
        dist = 0
        pawn_number = 0
    else:
        fail = False

        # choix du numéro du pion
        pawn_number = random.randint(0, number_pawns - 1)

        # choix de la direction
        etat_pawn = players[N].pawns[pawn_number].accessibles

        directions_possibles = [k for k in range(len(etat_pawn)) if etat_pawn[k] != 0]
        random_indice = random.randint(0, len(directions_possibles)-1)
        direction = directions_possibles[random_indice]

        # choix de la distance
        dist_max = etat_pawn[direction]
        dist = random.randint(1, dist_max)

    return players[N].pawns, fail, direction, dist, pawn_number
