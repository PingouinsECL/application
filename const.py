import pygame

# HOME MODE

window_title = "Pingouins"

path_icon = "images/icon.png"

path_background = "images/background.jpg"
path_background_alpha = "images/background_alpha.jpg"
pos_background = [0, 0]

path_logo = "images/logo.png"
pos_logo = [164, 50]

path_club_jeu = "images/club.png"
pos_club = [720, 550]

path_play = "images/jouer.png"
path_play_hover = "images/jouer_hover.png"
pos_play = [314, 340]

path_tuto = "images/tuto.png"
path_tuto_hover = "images/tuto_hover.png"
pos_tuto = [314, 440]

path_sound = "images/sound_on.jpg"
path_mute = "images/sound_off.jpg"
pos_sound = [760, 13]

path_hint="images/hint.png"
path_hint_hover="images/hint_highlight.png"
pos_hint = [10, 300]

sound_path = "sounds/background.wav"

# TUTORIAL MODE

path_back = "images/back.png"
pos_back = [0, 0]

path_settings = "images/instructions.png"
pos_settings = [0, 70] # [384, 150]

back_width = 828
back_height = 659

language_fr = pygame.image.load("images/language_fr.png");
language_en = pygame.image.load("images/language_en.png");
language_es = pygame.image.load("images/language_es.png");
language_de = pygame.image.load("images/language_de.png");
language_zh = pygame.image.load("images/language_zh.png");
languages_flags = [language_fr, language_en, language_es, language_de, language_zh]
pos_language = [600, 50]

with open("rules.txt", "r", encoding="utf8") as f:
    cont = f.read()

cont = cont.split("###")
french_rules = cont[0]
english_rules = cont[1]
spanish_rules = cont[2]
german_rules = cont[3]
chinese_rules = cont[4]
languages_rules = [french_rules, english_rules, spanish_rules, german_rules, chinese_rules]

with open("settings.txt", "r", encoding="utf8") as f:
    cont = f.read()

cont = cont.split("###")
french_settings = cont[0]
english_settings = cont[1]
spanish_settings = cont[2]
german_settings = cont[3]
chinese_settings = cont[4]
languages_settings = [french_settings, english_settings, spanish_settings, german_settings, chinese_settings]

# ANIMATIONS

break_path = "sounds/break.wav"
score_path = "sounds/score.wav"

# Player 0
path_player001 = "images/animation/player001.png"
path_player002 = "images/animation/player002.png"
path_player003 = "images/animation/player003.png"

path_player011 = "images/animation/player011.png"
path_player012 = "images/animation/player012.png"
path_player013 = "images/animation/player013.png"

path_player021 = "images/animation/player021.png"
path_player022 = "images/animation/player022.png"
path_player023 = "images/animation/player023.png"

path_player031 = "images/animation/player031.png"
path_player032 = "images/animation/player032.png"
path_player033 = "images/animation/player033.png"

path_player041 = "images/animation/player041.png"
path_player042 = "images/animation/player042.png"
path_player043 = "images/animation/player043.png"

path_player051 = "images/animation/player051.png"
path_player052 = "images/animation/player052.png"
path_player053 = "images/animation/player053.png"


# Player 1
path_player101 = "images/animation/player101.png"
path_player102 = "images/animation/player102.png"
path_player103 = "images/animation/player103.png"

path_player111 = "images/animation/player111.png"
path_player112 = "images/animation/player112.png"
path_player113 = "images/animation/player113.png"

path_player121 = "images/animation/player121.png"
path_player122 = "images/animation/player122.png"
path_player123 = "images/animation/player123.png"

path_player131 = "images/animation/player131.png"
path_player132 = "images/animation/player132.png"
path_player133 = "images/animation/player133.png"

path_player141 = "images/animation/player141.png"
path_player142 = "images/animation/player142.png"
path_player143 = "images/animation/player143.png"

path_player151 = "images/animation/player151.png"
path_player152 = "images/animation/player152.png"
path_player153 = "images/animation/player153.png"

# Player 2
path_player201 = "images/animation/player201.png"
path_player202 = "images/animation/player202.png"
path_player203 = "images/animation/player203.png"

path_player211 = "images/animation/player211.png"
path_player212 = "images/animation/player212.png"
path_player213 = "images/animation/player213.png"

path_player221 = "images/animation/player221.png"
path_player222 = "images/animation/player222.png"
path_player223 = "images/animation/player223.png"

path_player231 = "images/animation/player231.png"
path_player232 = "images/animation/player232.png"
path_player233 = "images/animation/player233.png"

path_player241 = "images/animation/player241.png"
path_player242 = "images/animation/player242.png"
path_player243 = "images/animation/player243.png"

path_player251 = "images/animation/player251.png"
path_player252 = "images/animation/player252.png"
path_player253 = "images/animation/player253.png"

# Player 3
path_player301 = "images/animation/player301.png"
path_player302 = "images/animation/player302.png"
path_player303 = "images/animation/player303.png"

path_player311 = "images/animation/player311.png"
path_player312 = "images/animation/player312.png"
path_player313 = "images/animation/player313.png"

path_player321 = "images/animation/player321.png"
path_player322 = "images/animation/player322.png"
path_player323 = "images/animation/player323.png"

path_player331 = "images/animation/player331.png"
path_player332 = "images/animation/player332.png"
path_player333 = "images/animation/player333.png"

path_player341 = "images/animation/player341.png"
path_player342 = "images/animation/player342.png"
path_player343 = "images/animation/player343.png"

path_player351 = "images/animation/player351.png"
path_player352 = "images/animation/player352.png"
path_player353 = "images/animation/player353.png"

# Player 0
player001 = pygame.image.load(path_player001)
player002 = pygame.image.load(path_player002)
player003 = pygame.image.load(path_player003)

player011 = pygame.image.load(path_player011)
player012 = pygame.image.load(path_player012)
player013 = pygame.image.load(path_player013)

player021 = pygame.image.load(path_player021)
player022 = pygame.image.load(path_player022)
player023 = pygame.image.load(path_player023)

player031 = pygame.image.load(path_player031)
player032 = pygame.image.load(path_player032)
player033 = pygame.image.load(path_player033)

player041 = pygame.image.load(path_player041)
player042 = pygame.image.load(path_player042)
player043 = pygame.image.load(path_player043)

player051 = pygame.image.load(path_player051)
player052 = pygame.image.load(path_player052)
player053 = pygame.image.load(path_player053)


# Player 1
player101 = pygame.image.load(path_player101)
player102 = pygame.image.load(path_player102)
player103 = pygame.image.load(path_player103)

player111 = pygame.image.load(path_player111)
player112 = pygame.image.load(path_player112)
player113 = pygame.image.load(path_player113)

player121 = pygame.image.load(path_player121)
player122 = pygame.image.load(path_player122)
player123 = pygame.image.load(path_player123)

player131 = pygame.image.load(path_player131)
player132 = pygame.image.load(path_player132)
player133 = pygame.image.load(path_player133)

player141 = pygame.image.load(path_player141)
player142 = pygame.image.load(path_player142)
player143 = pygame.image.load(path_player143)

player151 = pygame.image.load(path_player151)
player152 = pygame.image.load(path_player152)
player153 = pygame.image.load(path_player153)


# Player 2
player201 = pygame.image.load(path_player201)
player202 = pygame.image.load(path_player202)
player203 = pygame.image.load(path_player203)

player211 = pygame.image.load(path_player211)
player212 = pygame.image.load(path_player212)
player213 = pygame.image.load(path_player213)

player221 = pygame.image.load(path_player221)
player222 = pygame.image.load(path_player222)
player223 = pygame.image.load(path_player223)

player231 = pygame.image.load(path_player231)
player232 = pygame.image.load(path_player232)
player233 = pygame.image.load(path_player233)

player241 = pygame.image.load(path_player241)
player242 = pygame.image.load(path_player242)
player243 = pygame.image.load(path_player243)

player251 = pygame.image.load(path_player251)
player252 = pygame.image.load(path_player252)
player253 = pygame.image.load(path_player253)



# Player 3
player301 = pygame.image.load(path_player301)
player302 = pygame.image.load(path_player302)
player303 = pygame.image.load(path_player303)

player311 = pygame.image.load(path_player311)
player312 = pygame.image.load(path_player312)
player313 = pygame.image.load(path_player313)

player321 = pygame.image.load(path_player321)
player322 = pygame.image.load(path_player322)
player323 = pygame.image.load(path_player323)

player331 = pygame.image.load(path_player331)
player332 = pygame.image.load(path_player332)
player333 = pygame.image.load(path_player333)

player341 = pygame.image.load(path_player341)
player342 = pygame.image.load(path_player342)
player343 = pygame.image.load(path_player343)

player351 = pygame.image.load(path_player351)
player352 = pygame.image.load(path_player352)
player353 = pygame.image.load(path_player353)

image_player = [player021,player121,player221,player321]

image_player_animation = [[[player001,player002,player003,player002],[player011,player012,player013,player012],[player021,player022,player023,player022],[player031,player032,player033,player032],[player041,player042,player043,player042],[player051,player052,player053,player052]],[[player101,player102,player103,player102],[player111,player112,player113,player112],[player121,player122,player123,player122],[player131,player132,player133,player132],[player141,player142,player143,player142],[player151,player152,player153,player152]],[[player201,player202,player203,player202],[player211,player212,player213,player212],[player221,player222,player223,player222],[player231,player232,player233,player232],[player241,player242,player243,player242],[player251,player252,player253,player252]],[[player301,player302,player303,player302],[player311,player312,player313,player312],[player321,player322,player323,player322],[player331,player332,player333,player332],[player341,player342,player343,player342],[player351,player352,player353,player352]]]


# Slinding images

# Player 0
path_player01 = "images/animation/sliding/player01.png"
path_player02 = "images/animation/sliding/player02.png"
path_player03 = "images/animation/sliding/player03.png"
path_player04 = "images/animation/sliding/player04.png"
path_player05 = "images/animation/sliding/player05.png"
path_player06 = "images/animation/sliding/player06.png"


# Player 1
path_player11 = "images/animation/sliding/player11.png"
path_player12 = "images/animation/sliding/player12.png"
path_player13 = "images/animation/sliding/player13.png"
path_player14 = "images/animation/sliding/player14.png"
path_player15 = "images/animation/sliding/player15.png"
path_player16 = "images/animation/sliding/player16.png"


# Player 2
path_player21 = "images/animation/sliding/player21.png"
path_player22 = "images/animation/sliding/player22.png"
path_player23 = "images/animation/sliding/player23.png"
path_player24 = "images/animation/sliding/player24.png"
path_player25 = "images/animation/sliding/player25.png"
path_player26 = "images/animation/sliding/player26.png"


# Player 3
path_player31 = "images/animation/sliding/player31.png"
path_player32 = "images/animation/sliding/player32.png"
path_player33 = "images/animation/sliding/player33.png"
path_player34 = "images/animation/sliding/player34.png"
path_player35 = "images/animation/sliding/player35.png"
path_player36 = "images/animation/sliding/player36.png"



# Player 0
player01 = pygame.image.load(path_player01)
player02 = pygame.image.load(path_player02)
player03 = pygame.image.load(path_player03)
player04 = pygame.image.load(path_player04)
player05 = pygame.image.load(path_player05)
player06 = pygame.image.load(path_player06)


# Player 1
player11 = pygame.image.load(path_player11)
player12 = pygame.image.load(path_player12)
player13 = pygame.image.load(path_player13)
player14 = pygame.image.load(path_player14)
player15 = pygame.image.load(path_player15)
player16 = pygame.image.load(path_player16)


# Player 2
player21 = pygame.image.load(path_player21)
player22 = pygame.image.load(path_player22)
player23 = pygame.image.load(path_player23)
player24 = pygame.image.load(path_player24)
player25 = pygame.image.load(path_player25)
player26 = pygame.image.load(path_player26)


# Player 3
player31 = pygame.image.load(path_player31)
player32 = pygame.image.load(path_player32)
player33 = pygame.image.load(path_player33)
player34 = pygame.image.load(path_player34)
player35 = pygame.image.load(path_player35)
player36 = pygame.image.load(path_player36)

image_player_animation_sliding= [[player01,player02,player03,player04,player05,player06],[player11,player12,player13,player14,player15,player16],[player21,player22,player23,player24,player25,player26],[player31,player32,player33,player34,player35,player36]]


animation_number_unit = 10
animation_speed = 0.5
proba_sliding = 0.5

offset_x = 20

# TILES

pannel = "images/tile.jpg"
p = pygame.image.load(pannel)

case_height = 100
case_height_margin = 45
case_width = 87

mx = (back_width - 8*case_width)//2
my = (back_height - 5*case_height)//2

# PAWNS

path_one = "images/cases/case1.png"
path_two = "images/cases/case2.png"
path_three = "images/cases/case3.png"

one = pygame.image.load(path_one)
two = pygame.image.load(path_two)
three = pygame.image.load(path_three)

image_number = [one, two, three]

path_one_hint = "images/cases/1_hint.png"
path_two_hint = "images/cases/2_hint.png"
path_three_hint = "images/cases/3_hint.png"

one_hint = pygame.image.load(path_one_hint)
two_hint = pygame.image.load(path_two_hint)
three_hint = pygame.image.load(path_three_hint)

image_number_hint = [one_hint, two_hint, three_hint]

path_one_highlight = "images/cases/1_2.png"
path_two_highlight = "images/cases/2_2.png"
path_three_highlight = "images/cases/3_2.png"

one_highlight = pygame.image.load(path_one_highlight)
two_highlight = pygame.image.load(path_two_highlight)
three_highlight = pygame.image.load(path_three_highlight)

image_number_highlight = [one_highlight, two_highlight, three_highlight]

path_one_P0 = "images/cases/1_P0.png"
path_two_P0 = "images/cases/2_P0.png"
path_three_P0 = "images/cases/3_P0.png"

path_one_P1 = "images/cases/1_P1.png"
path_two_P1 = "images/cases/2_P1.png"
path_three_P1 = "images/cases/3_P1.png"

path_one_P2 = "images/cases/1_P2.png"
path_two_P2 = "images/cases/2_P2.png"
path_three_P2 = "images/cases/3_P2.png"

path_one_P3 = "images/cases/1_P3.png"
path_two_P3 = "images/cases/2_P3.png"
path_three_P3 = "images/cases/3_P3.png"

one_P0 = pygame.image.load(path_one_P0)
two_P0 = pygame.image.load(path_two_P0)
three_P0 = pygame.image.load(path_three_P0)

one_P1 = pygame.image.load(path_one_P1)
two_P1 = pygame.image.load(path_two_P1)
three_P1 = pygame.image.load(path_three_P1)

one_P2 = pygame.image.load(path_one_P2)
two_P2 = pygame.image.load(path_two_P2)
three_P2 = pygame.image.load(path_three_P2)

one_P3 = pygame.image.load(path_one_P3)
two_P3 = pygame.image.load(path_two_P3)
three_P3 = pygame.image.load(path_three_P3)

image_cases_players = [[one_P0, two_P0, three_P0], [one_P1, two_P1, three_P1], [one_P2, two_P2, three_P2], [one_P3, two_P3, three_P3]]

# CHOICE MODE

path_choice0 = "images/rien.png"
path_choice1 = "images/human.png"
path_choice2 = "images/random.png"
path_choice3 = "images/monte_carlo_guided.png"
path_choice4 = "images/impaler.png"
path_choice5 = "images/maxN_time.png"
path_choice_array = [path_choice0, path_choice1, path_choice2, path_choice3, path_choice4, path_choice5]

path_impaler0 = "images/nombre_0.png"
path_impaler1 = "images/nombre_1.png"
path_impaler2 = "images/nombre_2.png"
path_impaler3 = "images/nombre_3.png"
path_impalermax = "images/nombre_max.png"
path_impaler_array = [path_impaler0, path_impaler1, path_impaler2, path_impaler3, path_impalermax]

path_imaplerfa = "images/points_faux.png"
path_imaplervr = "images/points_vrai.png"
path_impaler_points_array = [path_imaplerfa, path_imaplervr]

path_void = "images/void.png"

path_end_choice = "images/play.png"
pos_choice0 = [185, 210]
pos_choice1 = [445, 210]
pos_choice2 = [185, 315]
pos_choice3 = [445, 315]
pos_choice_impaler0 = [85, 210]
pos_choice_impaler1 = [665, 210]
pos_choice_impaler2 = [85, 315]
pos_choice_impaler3 = [665, 315]
pos_choice_impaler_points0 = [85, 110]
pos_choice_impaler_points1 = [665, 110]
pos_choice_impaler_points2 = [85, 415]
pos_choice_impaler_points3 = [665, 415]
pos_end_choice = [315, 435]

# LAST SCREEN

path_back_to_menu = "images/back_to_menu.png"
pos_back_to_menu = [315,560]
