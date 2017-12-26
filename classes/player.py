from pawn import *

class Player:

    """
    Class defining a player. It can have multiple modes:
    0 -> human
    1 -> random
    2 -> minimax
    """

    number_player = 0

    def __init__(self, mode, total_number):
        self.score = 0
        self.mode = mode
        self.number = Player.number_player

        p = []
        for k in range(total_number):
            p.append(Pawn(self.number))

        self.pawns = p

        Player.number_player += 1

    def can_play(self):

        pawns = self.pawns
        n = len(pawns)
        can = n * [0]

        for i, p in enumerate(pawns):
            acc = p.accessibles
            if acc != [0, 0, 0, 0, 0, 0]:
                can[i] = 1
        return can
