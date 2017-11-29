def init_human(board, players, l):

    # asking the players for coordinates
    
    print("Paramétrage du pion numéro ", l, " (aidez-vous du plateau)")
    x = int(input("X ? (2, 4) \n"))
    y = int(input("X ? (2, 2) \n"))

    return x, y
