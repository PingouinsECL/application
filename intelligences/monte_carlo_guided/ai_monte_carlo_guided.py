from Node import *
import random
import time
import copy
import tensorflow as tf
import numpy as np
import os

sess = tf.InteractiveSession()
saver = tf.train.import_meta_graph("/home/moby/ECL/PE/BUILDING/intelligences/monte_carlo_guided/model.meta")
saver.restore(sess, os.getcwd() + "/intelligences/monte_carlo_guided/final")
graph = tf.get_default_graph()

X = graph.get_tensor_by_name('inputs/X:0')
Yp = graph.get_tensor_by_name('resnet/prediction/Relu:0')

def make_input(players, board, number_player):
    number_players = len(players)
    number_pawns = 6 - number_players
    
    data = np.zeros((8, 15, 5))
    
    # ajout du score des cases si accessibles, 0 sinon
    for k in range(len(board.cases_tab)):
        for l in range(len(board.cases_tab[0])):
            if board.cases_tab[k][l] != 0:
                case = board.cases_tab[k][l]
                if case.state == 1:
                    data[k, l, 1+case.score] = 1
                    
    for number_pawn in range(number_pawns):
        pawn = players[number_player].pawns[number_pawn]
        x, y = pawn.x, pawn.y
        data[y, x, 0] = 1
    
    for number_pawn in range(number_pawns):
        pawn = players[1-number_player].pawns[number_pawn]
        x, y = pawn.x, pawn.y
        data[y, x, 1] = 1
    
    return data

def compute_output(inputs):    
    if type(inputs) != list:
        inputs = [inputs]
        
    return sess.run(Yp, feed_dict={X:inputs})

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
            
            inputs = []
            for (pawnNumber, direction, distance) in node.untriedMoves:
                players_copy_copy = copy.deepcopy(players_copy)
                board_copy_copy = copy.deepcopy(board_copy)
                
                players_copy_copy[currentplayer].pawns[pawnNumber].move(board_copy_copy, players_copy_copy[currentplayer], direction, distance)
                inputs.append(make_input(players_copy_copy, board_copy_copy, currentplayer))
            
            probas = compute_output(inputs)
            
            max_proba = 0
            m = None
            i = 0
            while i < len(node.untriedMoves):
                if probas[i] >= max_proba:
                    m = node.untriedMoves[i]
                    max_proba = probas[i]
                i += 1
            
            pawnNumber, direction, distance = m
            
            nextplayer = (currentplayer + 1) % numberPlayers
            players_copy[currentplayer].pawns[pawnNumber].move(board_copy, players_copy[currentplayer], direction, distance)
            node = node.addChild(m, copy.deepcopy(board_copy), copy.deepcopy(players_copy), nextplayer)
            
            players_copy = copy.deepcopy(node.players)
            board_copy = copy.deepcopy(node.board)
            
            currentplayer = nextplayer
        
        # Rollout
        if verbose:
            print(sep + "Jeu de la partie")

        result = compute_output(make_input(players_copy, board_copy, rootplayernumber)) > 0.5

        if verbose:
            print("")
        
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
