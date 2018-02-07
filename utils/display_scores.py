import random
import pygame

from const import *

window = pygame.display.set_mode((0, 0))

a = pygame.image.load(path_a)
b = pygame.image.load(path_b)
c = pygame.image.load(path_c)
d = pygame.image.load(path_d)

def display_scores(scores, window):
    """
        Printing the scores on the screen
    """

    font = pygame.font.SysFont("plantagenetcherokee", 20)
    text0 = font.render("Joueur 0", True, (128, 0, 0))
    text1 = font.render("Joueur 1", True, (128, 0, 0))
    text2 = font.render("Joueur 2", True, (128, 0, 0))
    text3 = font.render("Joueur 3", True, (128, 0, 0))

    number_players = len(scores)

    window.blit(text0, (60, 10))
    sc = font.render(str(scores[0]), True, (128, 0, 0))
    window.blit(sc, (60,30))
    window.blit(a, (3,10))  

    window.blit(text1, (695, 10))
    sc = font.render(str(scores[1]), True, (128, 0, 0))
    window.blit(sc, (695,30))
    window.blit(b, (775,10))

    if number_players >= 3:
        window.blit(text2, (60, 600))
        sc = font.render(str(scores[2]), True, (128, 0, 0))
        window.blit(sc , (60, 620))
        window.blit(c, (3, 600))
    if number_players == 4:
        window.blit(text3, (695, 600))
        sc = font.render(str(scores[3]), True, (128, 0, 0))
        window.blit(sc, (695, 620))
        window.blit(d, (775, 600))