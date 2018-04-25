def init_sum (board) :
    h, w = len(board.cases_tab), len(board.cases_tab[0])
    
    def find_point (x, y, board):
        case = board.cases_tab[y][x]
        if case != 0 and case.state == 1 and case.score == 1 :
            dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]
            def advance(x, y, dx, dy):
                nb = 0
                while 0 <= x+dx < w and 0 <= y+dy < h and board.cases_tab[y+dy][x+dx].state == 1 :
                    nb += board.cases_tab[y+dy][x+dx].score
                    x += dx
                    y += dy
                return (nb)
            nb = 0
            for (dx, dy) in dirs :
                nb += advance(x, y, dx, dy)
            return (nb)
        else :
            return (-1)
    
    def choice_case (board) :
        n = -1
        (xp, yp) = (-1, -1)
        for y in range (h) :
            for x in range (w) :
                n_bis = find_point (x, y, board)
                if n_bis > n :
                    (xp, yp) = (x, y)
                    n = n_bis
        return (xp, yp)
    return(choice_case(board))