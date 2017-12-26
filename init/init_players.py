from player import *

def init_players():

    # asking the number of players and their gamemode

    print("Bienvenue dans le jeu Pingouins\n")
    print("###\tRenseignez les paramètres de jeu\t###\n")

    number_players = int(input("Combien de joueurs vont s'affronter?\n"))
    pawns_per_player = 2 + 4 - number_players

    print("\n###\t Mode de jeu des différents joueurs\t###\n")
    players = []
    for k in range(number_players):
        mode_player = int(input("Quel est le mode de jeu du joueur " + str(k) + " ? (0 humain, 1 random)\n"))
        players.append(Player(mode_player, pawns_per_player))

    return players
