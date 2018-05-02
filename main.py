# Loading libraries

import pygame
from pygame.locals import *
import numpy as np

import sys
from time import time, sleep
import json

# Adding folders to path

sys.path.append('../')
sys.path.append('../../')
sys.path.append('classes')
sys.path.append('../classes')
sys.path.append('../../classes')

sys.path.append('utils')
sys.path.append('../utils')
sys.path.append('../../utils')

sys.path.append('intelligences')
sys.path.append('../intelligences')
sys.path.append('../../intelligences')

active_modes = json.load(open('intelligences/config.json'))['active']
for mode in active_modes:
    sys.path.append(mode)
    sys.path.append('intelligences/' + mode)
    sys.path.append('../intelligences/' + mode)
    sys.path.append('../../intelligences/' + mode)

# Importing files

from const import *

from button import *
from board import *
from player import *

from select_mode import *
from max_island import *

from init_position import *
from display_scores import *

from add_data import *

# Initialising window
pygame.init()

window = pygame.display.set_mode((0, 0))

# Loading images
icon = pygame.image.load(path_icon).convert()
background = pygame.image.load(path_background).convert()
logo = pygame.image.load(path_logo)
club = pygame.image.load(path_club_jeu)

play = pygame.image.load(path_play).convert()
play_hover = pygame.image.load(path_play_hover).convert()

tuto = pygame.image.load(path_tuto).convert()
tuto_hover = pygame.image.load(path_tuto_hover).convert()

sound = pygame.image.load(path_sound).convert()
mute = pygame.image.load(path_mute).convert()

background_tutorial = pygame.image.load(path_background_tutorial).convert()
back = pygame.image.load(path_back).convert()

choices = [pygame.image.load(path_choice).convert() for path_choice in path_choice_array]
choices_impaler = [pygame.image.load(path_impaler).convert() for path_impaler in path_impaler_array]
void = pygame.image.load(path_void).convert()

end_choice = pygame.image.load(path_end_choice).convert()
back_to_menu = pygame.image.load(path_back_to_menu).convert()
configuration = [0]*4
configuration_impaler = [0]*4

# Creating buttons
but_play = Button(play, play_hover, pos_play, 0)
but_tuto = Button(tuto, tuto_hover, pos_tuto, 0)
but_sound = Button(sound, mute, pos_sound, 0)
but_back = Button(back, back, pos_back, 0)

but_choice0 = Button(choices[0], choices[0], pos_choice0, 0)
but_choice1 = Button(choices[0], choices[0], pos_choice1, 0)
but_choice2 = Button(choices[0], choices[0], pos_choice2, 0)
but_choice3 = Button(choices[0], choices[0], pos_choice3, 0)
but_choice_impaler0 = Button(void, void, pos_choice_impaler0, 0)
but_choice_impaler1 = Button(void, void, pos_choice_impaler1, 0)
but_choice_impaler2 = Button(void, void, pos_choice_impaler2, 0)
but_choice_impaler3 = Button(void, void, pos_choice_impaler3, 0)
but_end_choice = Button(end_choice, end_choice, pos_end_choice, 0)
but_back_to_menu = Button(back_to_menu, back_to_menu, pos_back_to_menu, 0)

# Setting window
pygame.display.set_caption(window_title)
pygame.display.set_icon(icon)
window = pygame.display.set_mode((background.get_width(), background.get_height()))

# Setting holding variables
hold = 1
show_scores = 1

tstart = 0
tend = 0

while hold:

    # refreshing speed
    pygame.time.Clock().tick(50)

    # mode selectors
    mode_home = 1
    mode_tuto = 0

    mode_choice = 0
    mode_init = 0
    mode_game = 0

    mode_results = 0
    mode_restart = 0

    # game infos

    init = 0
    play = 0
    number_turn = 0
    table_button = []
    players_lost = [0, 0, 0, 0]

    # HOME
    """
        DECIDE TO PLAY GAME OR TUTORIAL
    """

    while mode_home:

        # displaying background
        window.blit(background, pos_background)
        window.blit(logo, pos_logo)
        window.blit(club, pos_club)

        # creating cursor if not exists
        if not('cursor' in locals() or 'cursor' in globals()):
            cursor = [0, 0]

        # listening for events

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_home = 0
                hold = 0

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                cursor = event.pos
                if but_play.hover(cursor):
                    mode_home = 0
                    mode_choice = 1
                elif but_tuto.hover(cursor):
                    mode_home = 0
                    mode_tuto = 1

            elif event.type == MOUSEMOTION:
                cursor = event.pos

        # displaying buttons
        but_play.show(window, cursor)
        but_tuto.show(window, cursor)
        but_sound.show(window, cursor)
        pygame.display.flip()

    # TUTORIAL
    """
        EXPLAINING THE RULES
    """

    while mode_tuto:

        # displaying background and button
        window.blit(background_tutorial, pos_background_tutorial)
        window.blit(logo, (pos_logo[0],pos_logo[1]+400))
        pygame.display.flip()

        # listening for events
        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_home = 0
                hold = 0

            if event.type == MOUSEBUTTONDOWN and event.pos[0]<=60 and event.pos[1]<=60:
                cursor = event.pos
                if but_back.hover(cursor):
                    mode_tuto = 0
                    mode_home = 1

    # CHOICE MODE
    """
        FIRST STEP IN LAUNCHING A GAME TO SELECT PLAYERS' MODE
    """

    while mode_choice:
        # displaying background and buttons
        window.blit(background, pos_background)
        window.blit(logo, pos_logo)
        but_choice0.show(window, pos_choice0)
        but_choice1.show(window, pos_choice1)
        but_choice2.show(window, pos_choice2)
        but_choice3.show(window, pos_choice3)
        but_choice_impaler0.show(window, pos_choice_impaler0)
        but_choice_impaler1.show(window, pos_choice_impaler1)
        but_choice_impaler2.show(window, pos_choice_impaler2)
        but_choice_impaler3.show(window, pos_choice_impaler3)
        but_end_choice.show(window, pos_end_choice)
        pygame.display.flip()
        
        for event in pygame.event.get():
            window.blit(background, pos_background)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                cur = event.pos
                if but_choice0.hover(cur):
                    configuration[0] = (configuration[0] + 1) % len(choices)
                    but_choice0.modify_image(choices[configuration[0]])
                    if configuration[0] == 5 :
                        but_choice_impaler0.modify_image(choices_impaler[configuration_impaler[0]])
                    if configuration[0] != 5 :
                        but_choice_impaler0.modify_image(void)
                if but_choice1.hover(cur):
                    configuration[1] = (configuration[1] + 1) % len(choices)
                    but_choice1.modify_image(choices[configuration[1]])
                    if configuration[1] == 5 :
                        but_choice_impaler1.modify_image(choices_impaler[configuration_impaler[1]])
                    if configuration[1] != 5 :
                        but_choice_impaler1.modify_image(void)
                if but_choice2.hover(cur):
                    configuration[2] = (configuration[2] + 1) % len(choices)
                    but_choice2.modify_image(choices[configuration[2]])
                    if configuration[2] == 5 :
                        but_choice_impaler2.modify_image(choices_impaler[configuration_impaler[2]])
                    if configuration[2] != 5 :
                        but_choice_impaler2.modify_image(void)
                if but_choice3.hover(cur):
                    configuration[3] = (configuration[3] + 1) % len(choices)
                    but_choice3.modify_image(choices[configuration[3]])
                    if configuration[3] == 5 :
                        but_choice_impaler3.modify_image(choices_impaler[configuration_impaler[3]])
                    if configuration[3] != 5 :
                        but_choice_impaler3.modify_image(void)
                        
                if configuration[0] == 5 and but_choice_impaler0.hover(cur) :
                    configuration_impaler[0] = (configuration_impaler[0] + 1) % len(choices_impaler)
                    but_choice_impaler0.modify_image(choices_impaler[configuration_impaler[0]])
                if configuration[1] == 5 and but_choice_impaler1.hover(cur) :
                    configuration_impaler[1] = (configuration_impaler[1] + 1) % len(choices_impaler)
                    but_choice_impaler1.modify_image(choices_impaler[configuration_impaler[1]])
                if configuration[2] == 5 and but_choice_impaler2.hover(cur) :
                    configuration_impaler[2] = (configuration_impaler[2] + 1) % len(choices_impaler)
                    but_choice_impaler2.modify_image(choices_impaler[configuration_impaler[2]])
                if configuration[3] == 5 and but_choice_impaler3.hover(cur) :
                    configuration_impaler[3] = (configuration_impaler[3] + 1) % len(choices_impaler)
                    but_choice_impaler3.modify_image(choices_impaler[configuration_impaler[3]])
                if but_end_choice.hover(cur):
                    mode_choice = 0
                    mode_init = 1

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_choice = 0
                hold = 0

    # INIT MODE
    """
        SECOND STEP IN PREPARING THE GAME : PLACING THE PAWNS ON THE BOARD
    """
    while mode_init:

        # creation of the players and the board
        board = Board()
        players = []
        number_players = 0

        for mode in configuration:
            number_players += (mode > 0)

        pawns_per_player = 2 + 4 - number_players
        
        adversary_numbers = []
        for mode in range(len(configuration)) :
            if configuration[mode] > 0:
                mode_player = configuration[mode] - 1
                players.append(Player(mode_player, pawns_per_player))
                if configuration[mode] == 5 :
                    adversary_numbers.append(configuration_impaler[mode])
                else :
                    adversary_numbers.append(1)
        initial_players = players

        # printing the board
        window.blit(background, pos_background)
        table_button = board.display(window)
        pygame.display.flip()

        # positioning the pawns
        players = init_position(board, initial_players, table_button, window, background, pos_background)

        save_board (board)
        save_pos_init (players)
        mode_init = 0
        mode_game = 1


    # GAME MODE
    """
        CORE OF THE GAME
    """

    while mode_game:

        # number of the current player
        player_number = number_turn % number_players

        # refreshing the window
        scores = [players[k].score for k in range(len(players))]
        
        window.blit(background, pos_background)

        # printing the board
        table_button = board.display(window)
        
        # printing the scores
        display_scores(scores, window)
        
        pygame.display.flip()

        # computing islands and removing unaccessible cases
        update_islands(board, players, False)

        # selecting the move if pawns left
        if players_lost[player_number] != 1:
            fail, pawns, (direction, dist, pawn_number) = select_mode(board, players, table_button, player_number, players_lost, window, background, pos_background, adversary_numbers)

            # if a move was found
            if not(fail):
                players[player_number].pawns = pawns
                x_init, y_init = players[player_number].pawns[pawn_number].x, players[player_number].pawns[pawn_number].y

                # Starting coordinates

                if y_init % 2 == 0:
                    x_init_anim = int(x_init / 2)
                else:
                    x_init_anim = int((x_init + 1) / 2 - 1) + 1 / 2

                y_init_anim = y_init

                # New coordinates

                dirs = [[1, -1], [2, 0], [1, 1], [-1, 1], [-2, 0], [-1, -1]]
                dx, dy = dirs[direction]

                x_end = x_init + dx * dist
                y_end = y_init + dy * dist

                if y_end % 2 == 0:
                    x_end = int(x_end / 2)
                else:
                    x_end = int((x_end + 1) / 2 - 1) + 1 / 2
                
                # Animation

                animation_number = animation_number_unit * dist
                
                p=np.random.binomial(1,proba_sliding)

                for i in range(animation_number + 1):

                    # Static printings 
                    window.blit(background, pos_background)

                    scores = [players[k].score for k in range(len(players))]
                    display_scores(scores, window)

                    table_but = board.display(window, l_init=x_init, k_init=y_init)
                    

                    # Dynamic printings
                    alpha = i / animation_number
                    xcur = (1-alpha) * x_init_anim + alpha * x_end
                    xcur *= case_width
                    xcur += mx
                    xcur = int(xcur)

                    ycur = (1-alpha) * y_init_anim + alpha * y_end 
                    ycur *= case_height - case_height_margin
                    ycur += my
                    ycur = int(ycur)

                    if p == 1 :
                        window.blit(image_player_animation_sliding[player_number][direction], (xcur+offset_x, ycur))
                        
                    else :
                        window.blit(image_player_animation[player_number][direction][i%4], (xcur+offset_x, ycur))
                    pygame.display.flip()
                    time.sleep(0.05)
                    
                
                players[player_number].pawns[pawn_number].move(board, players[player_number], direction, dist)
                board.cases_tab[y_init][x_init].change_state(2)
                # finally completing the move
                for z in range (1,9):
                    window.blit(background, pos_background)
                    table_but = board.display(window, l_init=x_init, k_init=y_init,z=z)
                    display_scores(scores, window)
                    pygame.display.flip()
                    time.sleep(0.05)
                
                board.cases_tab[y_init][x_init].change_state(0)
                board.cases_tab[y_init][x_init].change_owner(player_number)

            # if no move was found
            else:
                players_lost[player_number] = 1

        # stopping the game if no player can move anymore
        if sum(players_lost) == len(players):
            mode_game = 0
            mode_results = 1

        number_turn += 1

        # listening for events

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_game = 0
                hold = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                play = 1


    # RESULTS

    while mode_results:

        # refreshing the window
        if show_scores:
            show_scores = 0

            window.blit(background, pos_background)
            board.display_end(window)
            scores = [players[k].score for k in range(len(players))]
            display_scores(scores, window)
            pygame.display.flip()

            scores = [[players[k].score, k] for k in range(len(players))]
            for i in range (len(players)) :
                for j in range (len(players[i].pawns)) :
                    scores[i][0] += board.cases_tab[players[i].pawns[j].y][players[i].pawns[j].x].score
            save_scores (scores)

            scores = sorted(scores, reverse=True)
            max_score = scores[0][0]
            winners_ex_aequo = sorted([(players[k].owned, k) for (score, k) in scores if score == max_score], reverse=True)
            max_owned = winners_ex_aequo[0][0]
            winners = [k for (owned, k) in winners_ex_aequo if owned == max_owned]
            save_victory(players, winners)

            phrase = (", ").join([str(winner) for winner in winners])

            if len(winners) > 1:
                phrase = "Victoire des joueurs " + phrase
            else:
                phrase = "Victoire du joueur " + phrase

            font = pygame.font.SysFont("plantagenetcherokee", 72)
            text = font.render(phrase, True, (128, 0, 0))

            # score = 'Score : ' + str(max_score)
            # sc = font.render(score, True, (128,0,0))

            w, h = pygame.display.get_surface().get_size()
            window.blit(text, ((w - text.get_width()) //2 , 0))
            # window.blit(sc, ((w - text.get_width()) //2 +50 , (h - text.get_height()) // 2+70))
            pygame.display.flip()

        but_back_to_menu.show(window, pos_back_to_menu)
        pygame.display.flip()

        # listening for events

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_results = 0
                hold = 0
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                cur = event.pos
                if but_back_to_menu.hover(cur):
                    mode_results = 0
                    mode_restart = 1

    # MODE RESTART

    while mode_restart:
        # mode selector
        mode_home = 1
        mode_tuto = 0

        mode_choice = 0
        mode_init = 0
        mode_game = 0

        mode_results = 0
        mode_restart = 0
        hold = 1

        # game infos
        init = 0
        play = 0
        number_turn = 0
        table_button = []
        players_lost = [0, 0, 0, 0]

        Player.number_player = 0

        show_scores = 1

        tstart = 0
        tend = 0
