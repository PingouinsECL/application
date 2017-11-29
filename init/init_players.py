from player import *

def init_players():

    # asking the number of players and their gamemode

    print("Bienvenue dans le jeu Pingouins\n")
    print("Renseignez les paramètres de jeu\n")

    number_players = int(input("Combien de joueurs vont s'affronter?\n"))
    pawns_per_player = 2 + 4 - number_players

    print("\nMode de jeu des différents joueurs\n")
    players = []
    for k in range(number_players):
        mode_player = int(input("Quel est le mode de jeu du joueur " + str(k) + " ? (0 humain, 1 random, 2 max)\n"))
        players.append(Player(mode_player, number_players))

    return players
