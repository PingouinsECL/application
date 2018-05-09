from Node import *
from utils_mc import anticipate_score

import random
import time
import copy
import numpy as np
import os

from sklearn.externals import joblib

model = joblib.load(os.getcwd() + '/intelligences/monte_carlo_guided/model.pkl')

UTCK = 2

def UTC(rootboard, rootplayers, rootplayernumber, itermax, timemax, verbose=False):
    
    rootnode = Node(board=rootboard, players=rootplayers, playerNumber=rootplayernumber)
    numberPlayers = len(rootplayers)
    
    if len(rootnode.untriedMoves) == 1:
        return rootnode.untriedMoves[0]
    
    Node.number = 0
    
    time_start = time.time()
    iteration = -1
    deleted = 0
    
    while time.time() - time_start < timemax and iteration < itermax:
        iteration += 1
        
        node = rootnode
        board_copy = copy.deepcopy(rootboard)
        players_copy = copy.deepcopy(rootplayers)
        currentplayer = rootplayernumber
        
        players_lost = {}
        
        if verbose:
            print("\nNouvelle partie")
        
        sep = "\t"
        
        # Select
        while node.untriedMoves == [] and node.childNodes != []:            
            node = node.UTCselectChild()
            pawnNumber, direction, distance = node.move
            players_copy[currentplayer].pawns[pawnNumber].move(board_copy, players_copy[currentplayer], direction, distance)
            currentplayer = (currentplayer + 1) % numberPlayers
            if verbose:
                print(sep + "Enfonce dans le node numero " + str(node.number))
            sep += "\t"
        
        # Expand
        if node.untriedMoves != []:
            if verbose:
                print(sep + "Exploration d'un nouveau node")
            
            n = np.random.randint(len(node.untriedMoves))
            m = node.untriedMoves[n]
            pawnNumber, direction, distance = m
            
            nextplayer = (currentplayer + 1) % numberPlayers
            players_copy[currentplayer].pawns[pawnNumber].move(board_copy, players_copy[currentplayer], direction, distance)
            node = node.addChild(m, copy.deepcopy(board_copy), copy.deepcopy(players_copy), nextplayer)
            
            players_copy = copy.deepcopy(node.players)
            board_copy = copy.deepcopy(node.board)
            
            currentplayer = nextplayer
             
        # Simulate
        if verbose:
            print(sep + "Jeu de la partie")
        
        my_anticipated_score = anticipate_score(model, board_copy, players_copy, rootplayernumber)
        other_anticipated_score = []
        
        for p in range(len(players_copy)):
            if p != rootplayernumber:
                other_anticipated_score.append(anticipate_score(model, board_copy, players_copy, p))
        
        result = my_anticipated_score >= max(other_anticipated_score)

        if verbose:
            print("")
        
        # Rollout
        while node != None:
            node.update(result) # (node.playerNumber in winners)
            if verbose:
                print(sep + "Node number : " + str(node.number))
            sep = sep[:-2]
            node = node.parentNode
            
        
    ordered = sorted(rootnode.childNodes, key=lambda c: c.wins/c.visits, reverse=True)
    m = ordered[0].wins / ordered[0].visits
    bests = []
    k = 1
    while k < len(ordered) and ordered[k].wins / ordered[k].visits == m:
        k += 1
    best = sorted(ordered[:k], key=lambda c: c.visits)[-1]

    return best.move

def ai_monte_carlo_guided(board, players, player_number, itermax, timemax):

    (pawn_number, direction, dist) = UTC(board, players, player_number, itermax=itermax, timemax=timemax)
    
    return direction, dist, pawn_number


def ai_monte_carlo_guided(board, players, player_number, itermax, timemax):

    (pawn_number, direction, dist) = UTC(board, players, player_number, itermax=itermax, timemax=timemax)
    
    return direction, dist, pawn_number
