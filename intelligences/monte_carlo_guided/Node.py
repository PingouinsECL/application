from numpy import sqrt, log

UTCK = 2

from numpy import sqrt, log

class Node:
    
    number = 0
    
    def __init__(self, move=None, parent=None, board=None, players=None, playerNumber=None):
        self.move = move
        self.parentNode = parent
        self.board = board
        self.players = players
        self.playerNumber = playerNumber
        
        self.number = Node.number
        Node.number += 1
        
        self.wins = 0
        self.visits = 0
        
        self.childNodes = []
        self.untriedMoves = []
        
        lip = []
        for k, (owners, _, score) in enumerate(board.islands): # score on isolated pawns
            if owners == [playerNumber]:
                for l in range(len(players[playerNumber].pawns)):
                    if players[playerNumber].pawns[l].island_number == k:
                        lip.append(l)
        
        
        for p in range(len(players[0].pawns)):
            if lip != None and p not in lip:
                players[self.playerNumber].pawns[p].compute_accessible(board)
                pawnMoves = players[self.playerNumber].pawns[p].accessibles
                for direction in range(len(pawnMoves)):
                    self.untriedMoves += [(p, direction, distancek) for distancek in range(1, pawnMoves[direction]+1) if pawnMoves[direction] > 0]
    
    def UTCselectChild(self):
        s = sorted(self.childNodes, key = lambda c : c.wins / c.visits + UTCK * sqrt(log(self.visits)/c.visits))[-1]
        return s
    
    def addChild(self, move, board, players, playerNumber):
        n = Node(move=move, parent=self, board=board, players=players, playerNumber=playerNumber)
        self.untriedMoves.remove(move)
        self.childNodes.append(n)
        return n
    
    def update(self, result):
        self.visits += 1
        self.wins += result