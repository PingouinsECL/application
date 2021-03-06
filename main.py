# Loading libraries

import pygame
from pygame.locals import *

from pygame.mixer import *
from pygame.mixer_music import * 

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
background_alpha = pygame.image.load(path_background_alpha).convert()

logo = pygame.image.load(path_logo)
club = pygame.image.load(path_club_jeu)

play = pygame.image.load(path_play).convert()
play_hover = pygame.image.load(path_play_hover).convert()

tuto = pygame.image.load(path_tuto).convert()
tuto_hover = pygame.image.load(path_tuto_hover).convert()

sound = pygame.image.load(path_sound).convert()
mute = pygame.image.load(path_mute).convert()

back = pygame.image.load(path_back)
settings = pygame.image.load(path_settings)

choices = [pygame.image.load(path_choice).convert() for path_choice in path_choice_array]
choices_impaler = [pygame.image.load(path_impaler).convert() for path_impaler in path_impaler_array]
choices_impaler_points = [pygame.image.load(path_impaler).convert() for path_impaler in path_impaler_points_array]
void = pygame.image.load(path_void).convert()

end_choice = pygame.image.load(path_end_choice).convert()
back_to_menu = pygame.image.load(path_back_to_menu).convert()
configuration = [0]*4
configuration_impaler = [0]*4
configuration_impaler_points = [0]*4

# Creating buttons
but_play = Button(play, play_hover, pos_play, 0)
but_tuto = Button(tuto, tuto_hover, pos_tuto, 0)
but_sound = Button(sound, mute, pos_sound, 0)
but_back = Button(back, back, pos_back, 0)
but_settings = Button(settings, settings, pos_settings, 0)
but_language = Button(language_fr, language_fr, pos_language, 0)
language = 0

but_choice0 = Button(choices[0], choices[0], pos_choice0, 0)
but_choice1 = Button(choices[0], choices[0], pos_choice1, 0)
but_choice2 = Button(choices[0], choices[0], pos_choice2, 0)
but_choice3 = Button(choices[0], choices[0], pos_choice3, 0)
but_choice_impaler0 = Button(void, void, pos_choice_impaler0, 0)
but_choice_impaler1 = Button(void, void, pos_choice_impaler1, 0)
but_choice_impaler2 = Button(void, void, pos_choice_impaler2, 0)
but_choice_impaler3 = Button(void, void, pos_choice_impaler3, 0)
but_choice_impaler_points0 = Button(void, void, pos_choice_impaler_points0, 0)
but_choice_impaler_points1 = Button(void, void, pos_choice_impaler_points1, 0)
but_choice_impaler_points2 = Button(void, void, pos_choice_impaler_points2, 0)
but_choice_impaler_points3 = Button(void, void, pos_choice_impaler_points3, 0)
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

sound_on = 1

pygame.font.init()

pygame.mixer.music.load(sound_path)
pygame.mixer.music.play()

def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, _ = surface.get_size()
    max_width -= 50
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 1, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

while hold:

    # refreshing speed
    pygame.time.Clock().tick(50)

    # mode selectors
    mode_home = 1
    mode_tuto = 0
    mode_settings = 0

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

        # creating cursor if not exists
        if not('cursor' in locals() or 'cursor' in globals()):
            cursor = [0, 0]

        if not(pygame.mixer.music.get_busy()):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

        # displaying background
        window.blit(background, pos_background)
        window.blit(logo, pos_logo)
        window.blit(club, pos_club)
        
        # displaying buttons        
        but_play.show(window, cursor)
        but_tuto.show(window, cursor)
        but_sound.show(window, cursor)

        pygame.display.flip()

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
                elif but_sound.hover(cursor):
                    sound_on = 1 - sound_on
                    if not(sound_on):
                        pygame.mixer.music.set_volume(0)
                    else:
                        pygame.mixer.music.set_volume(1)

            elif event.type == MOUSEMOTION:
                cursor = event.pos

    # TUTORIAL
    """
        EXPLAINING THE RULES
    """

    while mode_tuto:

        if not(pygame.mixer.music.get_busy()):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

        # displaying background and button
        window.blit(background, pos_background)
        window.blit(logo, (pos_logo[0],pos_logo[1]+400))
        but_back.show(window, (0, 0))
    
        window.blit(one, (220, 40))
        window.blit(player023, (500, 50))
        

        # listening for events
        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                mode_home = 0
                hold = 0

            if event.type == MOUSEBUTTONDOWN:
                cursor = event.pos
                if but_back.hover(cursor):
                    mode_tuto = 0
                    mode_home = 1
                elif but_language.hover(cursor):
                    language += 1
                    language %= len(languages_flags)
                    but_language.modify_image(languages_flags[language])

            if language == len(languages_flags) - 1:
                font = pygame.font.Font("fonts/zh.otf", 20)
            else:
                font = pygame.font.Font("fonts/other.otf", 20)
            but_language.show(window, pos_language)
            blit_text(window, languages_rules[language], (50, 150), font)
            pygame.display.flip()

    # CHOICE MODE
    """
        FIRST STEP IN LAUNCHING A GAME TO SELECT PLAYERS' MODE
    """

    while mode_choice:

        if not(pygame.mixer.music.get_busy()):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

        if mode_settings:
            window.blit(background_alpha, pos_background)
            but_settings.show(window, pos_settings)
            but_language.show(window, pos_language)
            but_back.show(window, pos_back)

            if language == len(languages_flags) - 1:
                font = pygame.font.Font("fonts/zh.otf", 15)
            else:
                font = pygame.font.Font("fonts/other.otf", 15)
            blit_text(window, languages_settings[language], (50, 150), font, color=pygame.Color('black'))

            pygame.display.flip()

        else:
        # displaying background and buttons
            window.blit(background, pos_background)
            window.blit(logo, pos_logo)

            but_settings.show(window, pos_settings)
            but_back.show(window, pos_back)

            but_choice0.show(window, pos_choice0)
            but_choice1.show(window, pos_choice1)
            but_choice2.show(window, pos_choice2)
            but_choice3.show(window, pos_choice3)
            but_choice_impaler0.show(window, pos_choice_impaler0)
            but_choice_impaler1.show(window, pos_choice_impaler1)
            but_choice_impaler2.show(window, pos_choice_impaler2)
            but_choice_impaler3.show(window, pos_choice_impaler3)
            but_choice_impaler_points0.show(window, pos_choice_impaler_points3)
            but_choice_impaler_points1.show(window, pos_choice_impaler_points3)
            but_choice_impaler_points2.show(window, pos_choice_impaler_points3)
            but_choice_impaler_points3.show(window, pos_choice_impaler_points3)
            
            but_end_choice.show(window, pos_end_choice)
            pygame.display.flip()
        
        for event in pygame.event.get():
            window.blit(background, pos_background)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                cur = event.pos
                if but_choice0.hover(cur):
                    configuration[0] = (configuration[0] + 1) % len(choices)
                    but_choice0.modify_image(choices[configuration[0]])
                    if configuration[0] == 4 :
                        but_choice_impaler0.modify_image(choices_impaler[configuration_impaler[0]])
                        but_choice_impaler_points0.modify_image(choices_impaler_points[configuration_impaler_points[0]])
                    if configuration[0] != 4 :
                        but_choice_impaler0.modify_image(void)
                        but_choice_impaler_points0.modify_image(void)
                elif but_choice1.hover(cur):
                    configuration[1] = (configuration[1] + 1) % len(choices)
                    but_choice1.modify_image(choices[configuration[1]])
                    if configuration[1] == 4 :
                        but_choice_impaler1.modify_image(choices_impaler[configuration_impaler[1]])
                        but_choice_impaler_points1.modify_image(choices_impaler_points[configuration_impaler_points[1]])
                    if configuration[1] != 4 :
                        but_choice_impaler1.modify_image(void)
                        but_choice_impaler_points1.modify_image(void)
                elif but_choice2.hover(cur):
                    configuration[2] = (configuration[2] + 1) % len(choices)
                    but_choice2.modify_image(choices[configuration[2]])
                    if configuration[2] == 4 :
                        but_choice_impaler2.modify_image(choices_impaler[configuration_impaler[2]])
                        but_choice_impaler_points2.modify_image(choices_impaler_points[configuration_impaler_points[2]])
                    if configuration[2] != 4 :
                        but_choice_impaler2.modify_image(void)
                        but_choice_impaler_points2.modify_image(void)
                elif but_choice3.hover(cur):
                    configuration[3] = (configuration[3] + 1) % len(choices)
                    but_choice3.modify_image(choices[configuration[3]])
                    if configuration[3] == 4 :
                        but_choice_impaler3.modify_image(choices_impaler[configuration_impaler[3]])
                        but_choice_impaler_points3.modify_image(choices_impaler_points[configuration_impaler_points[3]])
                    if configuration[3] != 4 :
                        but_choice_impaler3.modify_image(void)
                        but_choice_impaler_points3.modify_image(void)
                
                elif but_settings.hover(cur):
                    mode_settings = 1-mode_settings
                
                elif but_back.hover(cur):
                    mode_choice = 0
                    mode_settings = 0
                    mode_home = 1
                
                elif but_language.hover(cur):
                    language += 1
                    language %= len(languages_flags)
                    but_language.modify_image(languages_flags[language])
                        
                if configuration[0] == 4 and but_choice_impaler0.hover(cur) :
                    configuration_impaler[0] = (configuration_impaler[0] + 1) % len(choices_impaler)
                    but_choice_impaler0.modify_image(choices_impaler[configuration_impaler[0]])
                elif configuration[0] != 4 :
                    configuration_impaler[0] = 4
                if configuration[1] == 4 and but_choice_impaler1.hover(cur) :
                    configuration_impaler[1] = (configuration_impaler[1] + 1) % len(choices_impaler)
                    but_choice_impaler1.modify_image(choices_impaler[configuration_impaler[1]])
                elif configuration[1] != 4 :
                    configuration_impaler[1] = 4
                if configuration[2] == 4 and but_choice_impaler2.hover(cur) :
                    configuration_impaler[2] = (configuration_impaler[2] + 1) % len(choices_impaler)
                    but_choice_impaler2.modify_image(choices_impaler[configuration_impaler[2]])
                elif configuration[2] != 4 :
                    configuration_impaler[2] = 4
                if configuration[3] == 4 and but_choice_impaler3.hover(cur) :
                    configuration_impaler[3] = (configuration_impaler[3] + 1) % len(choices_impaler)
                    but_choice_impaler3.modify_image(choices_impaler[configuration_impaler[3]])
                elif configuration[3] != 4 :
                    configuration_impaler[3] = 4
                
                if configuration[0] == 4 and but_choice_impaler_points0.hover(cur) :
                    configuration_impaler_points[0] = (configuration_impaler_points[0] + 1) % len(choices_impaler_points)
                    but_choice_impaler_points0.modify_image(choices_impaler_points[configuration_impaler_points[0]])
                elif configuration[0] != 4 :
                    configuration_impaler_points[0] = 0
                if configuration[1] == 4 and but_choice_impaler_points1.hover(cur) :
                    configuration_impaler_points[1] = (configuration_impaler_points[1] + 1) % len(choices_impaler_points)
                    but_choice_impaler_points1.modify_image(choices_impaler_points[configuration_impaler_points[1]])
                elif configuration[1] != 4 :
                    configuration_impaler_points[1] = 0
                if configuration[2] == 4 and but_choice_impaler_points2.hover(cur) :
                    configuration_impaler_points[2] = (configuration_impaler_points[2] + 1) % len(choices_impaler_points)
                    but_choice_impaler_points2.modify_image(choices_impaler_points[configuration_impaler_points[2]])
                elif configuration[2] != 4 :
                    configuration_impaler_points[2] = 0
                if configuration[3] == 4 and but_choice_impaler_points3.hover(cur) :
                    configuration_impaler_points[3] = (configuration_impaler_points[3] + 1) % len(choices_impaler_points)
                    but_choice_impaler_points3.modify_image(choices_impaler_points[configuration_impaler_points[3]])
                elif configuration[3] != 4 :
                    configuration_impaler_points[3] = 0
                
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

        if not(pygame.mixer.music.get_busy()):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

        # creation of the players and the board
        board = Board()
        players = []
        number_players = 0

        for mode in configuration:
            number_players += (mode > 0)

        pawns_per_player = 2 + 4 - number_players
        
        adversary_numbers = []
        points = []
        for mode in range(len(configuration)) :
            if configuration[mode] > 0:
                mode_player = configuration[mode] - 1
                players.append(Player(mode_player, pawns_per_player))
                if configuration[mode] == 4 :
                    adversary_numbers.append(configuration_impaler[mode])
                    points.append(configuration_impaler_points[mode]==1)
                else :
                    adversary_numbers.append(None)
                    points.append(None)
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

        if not(pygame.mixer.music.get_busy()):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

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
            fail, pawns, (direction, dist, pawn_number) = select_mode(board, players, table_button, player_number, players_lost, window, background, pos_background, adversary_numbers, points)

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

                pygame.mixer.Sound(score_path).play()

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
                pygame.mixer.Sound(break_path).play()
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

        if not(pygame.mixer.music.get_busy()):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

        # refreshing the window
        if show_scores:
            show_scores = 0

            window.blit(background, pos_background)
            board.display_end(window)
            scores = [players[k].score for k in range(len(players))]
            for i in range (len(players)) :
                for j in range (len(players[i].pawns)) :
                    scores[i] += board.cases_tab[players[i].pawns[j].y][players[i].pawns[j].x].score
            display_scores(scores, window)
            pygame.display.flip()

            scores = [(j, i) for (i,j) in enumerate(scores)]
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
            window.blit(text, ((w - text.get_width()) //2 , 20))
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
