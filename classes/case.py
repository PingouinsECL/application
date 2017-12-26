class Case:

    """
    Class defining a case, characterised by :
    - its coordinates
    - its score
    - its state (1 for accessible, 0 for removed, 2 for occupied)
    - its owner (-1 for none, number of player otherwise)
    """

    def __init__(self, pos_x, pos_y, n, state = True):
        self.x = pos_x
        self.y = pos_y
        self.score = n
        self.state = 1
        self.owner = -1

    def change_state(self, new_state):
        self.state = new_state
    
    def change_owner(self, new_owner):
        self.owner = new_owner
