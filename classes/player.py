from pawn import *

class Player:

    """
    Class defining a player. It can have multiple modes:
    0 -> human
    1 -> IA 1
    """

    number_player = 0

    def __init__(self, mode, total_number):
        self.score = 0
        self.mode = mode

        p = []
        p.append(Pawn(Player.number_player))
        p.append(Pawn(Player.number_player))

        if total_number <= 3:
            p.append(Pawn(Player.number_player))
        if total_number == 2:
            p.append(Pawn(Player.number_player))

        self.pawns = p

        Player.number_player += 1

    def can_play(self):

        pawns = self.pawns
        n = len(pawns)
        can = n * [0]

        for i, p in enumerate(pawns):
            acc = p.accessibles
            if acc != []:
                can[i] = 1
        return can
