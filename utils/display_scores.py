import random
import pygame

from const import *

window = pygame.display.set_mode((0, 0))

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

    window.blit(p, (3,3))
    window.blit(text0, (65, 10))
    sc = font.render(str(scores[0]), True, (128, 0, 0))
    window.blit(sc, (100,40))
    window.blit(image_player[0], (10,15))

    if number_players >= 2:
        window.blit(p, (675,3))
        window.blit(text1, (682, 10))
        sc = font.render(str(scores[1]), True, (128, 0, 0))
        window.blit(sc, (717,40))
        window.blit(image_player[1], (765,15))

    if number_players >= 3:
        window.blit(p, (3,588))
        window.blit(text2, (65, 595))
        sc = font.render(str(scores[2]), True, (128, 0, 0))
        window.blit(sc , (100, 623))
        window.blit(image_player[2], (10, 600))
        
    if number_players == 4:
        window.blit(p, (675,588))
        window.blit(text3, (682, 595))
        sc = font.render(str(scores[3]), True, (128, 0, 0))
        window.blit(sc, (717, 623))
        window.blit(image_player[3], (765, 600))
