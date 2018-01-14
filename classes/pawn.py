class Pawn:

    """
    Class defining what a pawn is. It is characterised by :
    - its coordinates
    - its player
    - where it can go
    """

    def __init__(self, id_player):
        self.x = 0
        self.y = 0
        self.id = id_player
        self.accessibles = []
        self.active = True
        self.remain = 1

    def move(self, board, player, direction, distance):
        """
        0 -> upper right (+1, -1)
        1 -> right (+2, 0)
        2 -> lower right (+1, +1)
        3 -> lower left (-1, +1)
        4 -> left (-2, 0)
        5 -> upper left (-1, -1)
        """

        player.score += board.cases_tab[self.y][self.x].score
        board.cases_tab[self.y][self.x].change_state(0)

        if direction == 0:
            self.x += distance
            self.y -= distance
        elif direction == 1:
            self.x += 2*distance
        elif direction == 2:
            self.x += distance
            self.y += distance
        elif direction == 3:
            self.x -= distance
            self.y += distance
        elif direction == 4:
            self.x -= 2*distance
        elif direction == 5:
            self.x -= distance
            self.y -= distance

        board.cases_tab[self.y][self.x].change_state(2)
        board.cases_tab[self.y][self.x].owner = self.id

    def anti_move (self, board, player, direction, distance):
        board.cases_tab[self.y][self.x].change_state(1)
        board.cases_tab[self.y][self.x].owner = -1
        
        if direction == 0:
            self.x -= distance
            self.y += distance
        elif direction == 1:
            self.x -= 2*distance
        elif direction == 2:
            self.x -= distance
            self.y -= distance
        elif direction == 3:
            self.x += distance
            self.y -= distance
        elif direction == 4:
            self.x += 2*distance
        elif direction == 5:
            self.x += distance
            self.y += distance

        player.score -= board.cases_tab[self.y][self.x].score
        board.cases_tab[self.y][self.x].change_state(2)
    
    def place(self, board, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

        board.cases_tab[pos_y][pos_x].change_state(2)
        board.cases_tab[pos_y][pos_x].owner = self.id

    def compute_accessible(self, board):

        """
        we try each direction one after another and collect the data under the format
        [a, b, c, d, e, f] where each letter accounts for the number of reachable (inclusive) cases in the given direction
        """

        if self.active:
            x = self.x
            y = self.y

            dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]

            def advance(x, y, dx, dy):
                k = 0
                while 0 <= x+dx < 15 and 0 <= y+dy < 8 and \
                    board.cases_tab[y+dy][x+dx].state == 1:
                    k += 1
                    x += dx
                    y += dy
                return k

            max_per_dir = []

            for (dx, dy) in dirs:
                max_per_dir.append(advance(x, y, dx, dy))

            self.accessibles = max_per_dir

            if self.accessibles == [0, 0, 0, 0, 0, 0]:
                self.active = False
                self.remain = 0
            else:
                self.remain = 1
        else:
            self.remain = 1
