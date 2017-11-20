import random

def init_random(board, players):
    h, w = len(board.cases_tab), len(board.cases_tab)
    all_cases = [[board.cases_tab[k][l] for l in range(w)] for k in range(h)]
    for k in range(h):
        for l in range(w):
            if all_cases[k][l] != 0 :
                all_cases[k][l] = all_cases[k][l].state


    candidates = [(k, l) for k in range(h) for l in range(w) if all_cases[k][l] == 1]

    n = random.randint(0, len(candidates)-1)
    y, x = candidates[n]
    print(x, y)
    return x, y
