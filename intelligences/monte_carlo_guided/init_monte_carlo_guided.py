import random

def init_monte_carlo(board):
    h, w = len(board.cases_tab), len(board.cases_tab[0])
    candidates = []

    # selecting candidate (score 1, accessible)

    for k in range(h):
        for l in range(w):
            case = board.cases_tab[k][l]
            if case != 0 and case.state == 1 and case.score == 1:
                candidates.append((k, l))

    # selecting random case
    n = random.randint(0, len(candidates)-1)
    y, x = candidates[n]
    return x, y
