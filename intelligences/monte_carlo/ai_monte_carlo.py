from Node import *
import random
import time
import copy

def ai_monte_carlo(board, players, player_number, itermax, timemax):

    (pawn_number, direction, dist) = UTC(board, players, player_number, itermax=itermax, timemax=timemax)
    
    return direction, dist, pawn_number

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
            
            # suppression des mouvements peu intéressants
            k = 0
            while k < len(node.childNodes):
                ratio = node.childNodes[k].wins / node.childNodes[k].visits
                if node.childNodes[k].visits > 20 and ratio < 0.5:                  
                    node.childNodes.remove(node.childNodes[k])
                    deleted += 1
                else:
                    k+=1
            
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
            m = random.choice(node.untriedMoves)
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
        
        # on fait jouer jusqu'à ce qu'un seul joueur puisse jouer
        while len(players_lost) < numberPlayers - 1:

            possibles = []
            for p in range(len(players_copy[currentplayer].pawns)):
                players_copy[currentplayer].pawns[p].compute_accessible(board_copy)
                pawnMoves = players_copy[currentplayer].pawns[p].accessibles
                for direction in range(len(pawnMoves)):
                    possibles += [(p, direction, distancek) for distancek in range(1, pawnMoves[direction]+1) if pawnMoves[direction] > 0]
            if possibles == []:
                players_lost[currentplayer] = 1
            else:
                pawnNumber, direction, distance = random.choice(possibles)
                players_copy[currentplayer].pawns[pawnNumber].move(board_copy, players_copy[currentplayer], direction, distance)
                
            currentplayer = (currentplayer + 1) % numberPlayers

        # on fait jouer le joueur suivant dans ses iles
        board_copy.compute_islands()
        for (owners, island_cases) in board_copy.islands:
            if owners == [currentplayer]:
                players_copy[currentplayer].score += sum([board_copy.cases_tab[y][x].score for (x, y) in island_cases])
            
        if verbose:
            print(sep + "Partie terminée")
            
        scores = sorted([(players_copy[k].score, k) for k in range(len(players_copy))], reverse=True)
        m = scores[0][0]
        winners_ex_aequo = sorted([(players_copy[k].owned, k) for (score, k) in scores if score == m], reverse=True)
        m = winners_ex_aequo[0][0]
        winners = [k for (owned, k) in winners_ex_aequo if owned == m]
        
        result = rootplayernumber in winners

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

    # print(time.time() - time_start, sorted([(round(c.wins/c.visits, 3), c.wins, c.visits) for c in rootnode.childNodes], reverse=True)[:5])
    # print(str(iteration) + " simulations en " + str(round(time.time() - time_start, 2)) + "s")
    return best.move
