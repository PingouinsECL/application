import pygame
from pygame.locals import *

import sys
sys.path.append('../')
sys.path.append('../../')
sys.path.append('classes')
sys.path.append('../classes')
sys.path.append('../../classes')
sys.path.append('intelligences')
sys.path.append('../intelligences')
sys.path.append('../../intelligences')
sys.path.append('init')
sys.path.append('../init')
sys.path.append('../../init')
sys.path.append('random')
sys.path.append('intelligences/random')
sys.path.append('../intelligences/random')
sys.path.append('../../intelligences/random')


from const import *

# sys.path.append('classes')
from button import *
from board import *

# sys.path.append('intelligences')
from select_mode import *

# sys.path.append('init')
from init_players import *
from init_position import *

pygame.init()

window = pygame.display.set_mode((0, 0))

# Loading images
icon = pygame.image.load(path_icon).convert()
background = pygame.image.load(path_background).convert()

logo = pygame.image.load(path_logo).convert()

play = pygame.image.load(path_play).convert()
play_hover = pygame.image.load(path_play_hover).convert()

tuto = pygame.image.load(path_tuto).convert()
tuto_hover = pygame.image.load(path_tuto_hover).convert()

sound = pygame.image.load(path_sound).convert()
mute = pygame.image.load(path_mute).convert()

background_tutorial = pygame.image.load(path_background_tutorial).convert()
back = pygame.image.load(path_back).convert()

# Creating button
but_play = Button(play, play_hover, pos_play)
but_tuto = Button(tuto, tuto_hover, pos_tuto)
but_sound = Button(sound, mute, pos_sound)
but_back = Button(back, back, pos_back)


# Setting window

pygame.display.set_caption(window_title)
pygame.display.set_icon(icon)
window = pygame.display.set_mode((background.get_width(), background.get_height()))


hold = 1
while hold:

    mode_home = 1
    mode_tuto = 0
    mode_game = 0

    init = 0
    play = 0
    number_turn = 0
    table_but = []

    # HOME

    while mode_home:
        pygame.time.Clock().tick(30)

        window.blit(background, pos_background)
        window.blit(logo, pos_logo)

        but_play.show(window, [0, 0])
        but_tuto.show(window, [0, 0])
        but_sound.show(window, [0, 0])

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_home = 0
                mode_game = 0
                mode_tuto = 0
                hold = 0

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                cur = event.pos
                if but_play.hover(cur):
                    mode_home = 0
                    mode_game = 1
                    mode_tuto = 0
                elif but_tuto.hover(cur):
                    mode_home = 0
                    mode_tuto = 1
                    mode_game = 0

            elif event.type == MOUSEMOTION:
                cur = event.pos
                but_play.show(window, cur)
                but_tuto.show(window, cur)
                but_sound.show(window, cur)
                pygame.display.flip()


        # TUTORIAL

        while mode_tuto:

            window.blit(background_tutorial, pos_background_tutorial)
            but_back.show(window, cur)
            pygame.display.flip()

            ## Edition de la page d'aide

            for event in pygame.event.get():

                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    mode_home = 0
                    mode_game = 0
                    mode_tuto = 0
                    hold = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cur = event.pos
                    if but_back.hover(cur):
                        mode_tuto = 0
                        mode_home = 1

        # GAME MODE

        while mode_game:

            #window.blit(background, pos_background)
            #pygame.display.flip()

            if not(init):
                init = 1

                board = Board()
                initial_players = init_players()

                window.blit(background, pos_background)
                table_but = board.display(window)
                pygame.display.flip()

                players = init_position(board, initial_players)

                window.blit(background, pos_background)
                table_but = board.display(window)
                pygame.display.flip()

            if play:

                play = 0

                # number of the current player
                N = number_turn % len(players);

                window.blit(background, pos_background)
                pygame.display.flip()

                print(str(number_turn) + 'e tour \t Tour du joueur numéro ', str(N), '\n')

                # selecting the move
                fail, direction, dist, pawn_number  = select_mode(N, players, board)

                if not(fail):
                    players[N].pawns[pawn_number].move(board, players[N], direction, dist)
                else:
                    print("Le joueur ", N, " a perdu")

                # printing the game after the move
                table_but = board.display(window)
                pygame.display.flip()

                # printing scores
                print("Scores actuels")
                for k in range(len(players)):
                    print('Score de ', str(k), ' :\t', players[k].score)

                number_turn += 1

            for event in pygame.event.get():

                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    mode_home = 0
                    mode_game = 0
                    mode_tuto = 0
                    hold = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    play = 1
