# Loading libraries

import pygame
from pygame.locals import *

import sys

# Adding folders to path

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

sys.path.append('human')
sys.path.append('intelligences/human')
sys.path.append('../intelligences/human')
sys.path.append('../../intelligences/human')


sys.path.append('max')
sys.path.append('intelligences/max')
sys.path.append('../intelligences/max')
sys.path.append('../../intelligences/max')

# Importing files

from const import *

from button import *
from board import *
from player import *

from select_mode import *

from init_position import *

# Initialising window
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

choice0 = pygame.image.load(path_choice0).convert()
choice1 = pygame.image.load(path_choice1).convert()
choice2 = pygame.image.load(path_choice2).convert()
choice3 = pygame.image.load(path_choice3).convert()
end_choice = pygame.image.load(path_end_choice).convert()
choices = [choice0,choice1,choice2, choice3]
configuration = [0]*4

# Creating buttons
but_play = Button(play, play_hover, pos_play, 0)
but_tuto = Button(tuto, tuto_hover, pos_tuto, 0)
but_sound = Button(sound, mute, pos_sound, 0)
but_back = Button(back, back, pos_back, 0)

but_choice0 = Button(choice0, choice0, pos_choice0,0)
but_choice1 = Button(choice0, choice0, pos_choice1,0)
but_choice2 = Button(choice0, choice0, pos_choice2,0)
but_choice3 = Button(choice0, choice0, pos_choice3,0)
but_end_choice = Button(end_choice, end_choice, pos_end_choice,0)

# Setting window
pygame.display.set_caption(window_title)
pygame.display.set_icon(icon)
window = pygame.display.set_mode((background.get_width(), background.get_height()))

# Setting holding variables
hold = 1
show_scores = 1

while hold:

    mode_home = 1
    mode_tuto = 0
    mode_game = 0
    mode_results = 0
    mode_choice = 0

    init = 0
    play = 0
    number_turn = 0
    table_button = []
    players_lost = {}

    # HOME

    while mode_home:
        # refreshing speed

        pygame.time.Clock().tick(30)

        # displaying screen

        window.blit(background, pos_background)
        window.blit(logo, pos_logo)

        if not('cursor' in locals() or 'cursor' in globals()):
            cursor = [0, 0]

        but_play.show(window, cursor)
        but_tuto.show(window, cursor)
        but_sound.show(window, cursor)

        pygame.display.flip()

        # listening for events

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_home = 0
                mode_tuto = 0
                mode_game = 0
                mode_results = 0
                mode_choice = 0
                hold = 0

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                cursor = event.pos
                if but_play.hover(cursor):
                    mode_home = 0
                    mode_tuto = 0
                    mode_game = 0
                    mode_results = 0
                    mode_choice = 1
                elif but_tuto.hover(cursor):
                    mode_home = 0
                    mode_tuto = 1
                    mode_game = 0
                    mode_results = 0
                    mode_choice = 0

            elif event.type == MOUSEMOTION:
                cursor = event.pos

        but_play.show(window, cursor)
        but_tuto.show(window, cursor)
        but_sound.show(window, cursor)
        pygame.display.flip()


        # TUTORIAL

        while mode_tuto:

            # cleaning the window

            window.blit(background_tutorial, pos_background_tutorial)
            but_back.show(window, cursor)
            pygame.display.flip()

            # printing the tutorial

            # listening for events

            for event in pygame.event.get():

                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    mode_home = 0
                    mode_tuto = 0
                    mode_game = 0
                    mode_results = 0
                    mode_choice = 0
                    hold = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cursor = event.pos
                    if but_back.hover(cursor):
                        mode_tuto = 0
                        mode_home = 1

        # CHOICE MODE 
        
        while mode_choice:
            
            window.blit(background, pos_background)
            
            but_choice0.show(window, pos_choice0)
            but_choice1.show(window, pos_choice1)     
            but_choice2.show(window, pos_choice2)
            but_choice3.show(window, pos_choice3)      
            but_end_choice.show(window, pos_end_choice)
            pygame.display.flip()
            players = []
            
            for event in pygame.event.get():
            
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cur = event.pos
                    if but_choice0.hover(cur):
                        configuration[0] += 1
                        configuration[0] = configuration[0]%len(choices)
                        but_choice0.modify_image(choices[configuration[0]])
                    if but_choice1.hover(cur):
                        configuration[1] += 1
                        configuration[1] = configuration[1]%len(choices)
                        but_choice1.modify_image(choices[configuration[1]])
                    if but_choice2.hover(cur):
                        configuration[2] += 1
                        configuration[2] = configuration[2]%len(choices)
                        but_choice2.modify_image(choices[configuration[2]])
                    if but_choice3.hover(cur):
                        configuration[3] += 1
                        configuration[3] = configuration[3]%len(choices)
                        but_choice3.modify_image(choices[configuration[3]])                   
                    if but_end_choice.hover(cur):
                        mode_choice = 0        
                        mode_home = 0
                        mode_tuto = 0
                        mode_game = 1
                        mode_results = 0
                        hold = 0
                
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    mode_home = 0
                    mode_tuto = 0
                    mode_game = 0
                    mode_results = 0
                    hold = 0

        # GAME MODE

        while mode_game:

            # initialisation step

            if not(init):
                init = 1

                # creation of the players and the Board

                board = Board()
                players = []
                number_players=0
                
                for element in configuration:
                    if element != 0:
                        number_players += 1
                
                pawns_per_player = 2 + 4 - number_players
                
                for i in range(4):    
                    if configuration[i] == 1:
                        mode_player = 0
                        players.append(Player(mode_player, pawns_per_player))

                    elif configuration[i] == 2:
                        mode_player = 1
                        players.append(Player(mode_player, pawns_per_player))

                    elif configuration[i] == 3:
                        mode_player = 2
                        players.append(Player(mode_player, pawns_per_player))
                initial_players = players

                # printing the board

                window.blit(background, pos_background)
                table_button = board.display(window)
                pygame.display.flip()

                players = init_position(board, initial_players, table_button, window, background, pos_background)
                players_number = len(players)

                window.blit(background, pos_background)
                table_button = board.display(window)
                pygame.display.flip()

                print("Le jeu peut commencer !\n")

            # player's play

            # if play:

            # play = 0

            # number of the current player
            player_number = number_turn % len(players)

            # refreshing the window

            window.blit(background, pos_background)
            table_but = board.display(window)
            pygame.display.flip()

            print(str(number_turn) + 'e tour \t Tour du joueur numéro ' + str(player_number) + '\n')

            # selecting the move if pawns left
            if not(player_number in players_lost):
                fail, pawns, (direction, dist, pawn_number) = select_mode(board, players, table_button, player_number)

                # if a move was found
                if not(fail):
                    players[player_number].pawns = pawns
                    players[player_number].pawns[pawn_number].move(board, players[player_number], direction, dist)
                else:
                    print("Le joueur " + str(player_number) + " ne peut plus jouer")
                    players_lost[player_number] = 1
            else:
                print("Le tour du joueur " + str(player_number) + " a été passé car il ne pouvait pas jouer")

            # printing the game after the move
            window.blit(background, pos_background)
            table_but = board.display(window)
            pygame.display.flip()

            # printing scores
            print("Scores actuels")
            for k in range(len(players)):
                print('Score de ' + str(k) + ' :\t' + str(players[k].score))
            
            # stopping the play if no player can move
            if len(players_lost) == len(players):
                mode_game = 0
                mode_results = 1

            number_turn += 1

            # listening for events

            for event in pygame.event.get():

                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    mode_home = 0
                    mode_game = 0
                    mode_tuto = 0
                    hold = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    play = 1
        # RESULTS

        while mode_results:

            # refreshing the window

            window.blit(background, pos_background)
            window.blit(logo, pos_logo)

            scores = [players[k].score for k in range(len(players))]
            m = max(scores)
            i = []
            k = 0
            while k < len(players):
                if scores[k] == m:
                    i.append(k)
                k += 1

            if show_scores:
                show_scores = 0
                for k in range(len(i)):
                    print("Le joueur " + str(i[k]) + " a gagné avec " + str(m) + " points")

            # listening for events

            for event in pygame.event.get():

                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    mode_home = 0
                    mode_game = 0
                    mode_tuto = 0
                    mode_results = 0
                    mode_choice = 0
                    hold = 0
