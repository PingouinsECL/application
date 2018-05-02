def save_board (board) :
    data = open('data.txt', 'a')
    data.write("__début__")
    data.write("\n")
    for line in board.cases_tab :
        for case in line :
            if case != 0 :
                data.write(str(case.x))
                data.write (",")
                data.write (str(case.y))
                data.write (",")
                data.write (str(case.score))
                data.write ("\n")
    data.write(";")
    data.write("\n")
    data.close()

def save_pos_init (players) :
    data = open('data.txt', 'a')
    for i in range (len(players)) :
        for j in range (len(players[i].pawns)) :
            p = players[i].pawns[j]
            data.write(str(i))
            data.write(",")
            data.write(str(j))
            data.write(",")
            data.write(str(p.x))
            data.write(",")
            data.write(str(p.y))
            data.write("\n")
    data.write(";")
    data.write("\n")
    data.close()

def save_move (player_number, direction, dist, pawn_number) :
    data = open('data.txt', 'a')
    data.write(str(player_number))
    data.write(",")
    data.write(str(direction))
    data.write(",")
    data.write(str(dist))
    data.write(",")
    data.write(str(pawn_number))
    data.write("\n")
    data.close()

def save_scores (scores) :
    data = open('data.txt', 'a')
    data.write(";")
    data.write("\n")
    for i in range (len(scores)) :
        data.write(str(i))
        data.write(",")
        data.write(str(scores[i][0]))
        data.write("\n")
    data.close()

def save_victory (players, winners) :
    data = open('data.txt', 'a')
    for w in winners :
        if players[w].mode == 0 :
            data.write("*")
            data.write("\n")
    data.write("__fin__")
    data.write("\n")
    data.close()