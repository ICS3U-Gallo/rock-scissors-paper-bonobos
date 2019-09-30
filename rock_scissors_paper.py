import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
display_width = 800
display_height = 600

classic_game_mode = pygame.image.load('Images/classicgamemode.png')
best_of_game_mode = pygame.image.load('Images/bestofgamemode.png')
best_of_3 = pygame.image.load('Images/bestof3.png')
best_of_5 = pygame.image.load('Images/bestof5.png')
best_of_7 = pygame.image.load('Images/bestof7.png')
home_button = pygame.image.load('Images/homebutton.png')
rock = pygame.image.load('Images/rock.jpg')
paper = pygame.image.load('Images/paper.png')
scissors = pygame.image.load('Images/scissors.jpg')
play_again_button = pygame.image.load('Images/playagain.png')
computer_icon = pygame.image.load('Images/computericon.png')
player_icon = pygame.image.load('Images/playericon.png')
computer_wins_msg = pygame.image.load('Images/computerwinsmsg.jpg')
you_win_msg = pygame.image.load('Images/youwinmsg.jpg')

classic_game_mode = pygame.transform.scale(classic_game_mode, (300, 300))
best_of_game_mode = pygame.transform.scale(best_of_game_mode, (300, 300))
best_of_3 = pygame.transform.scale(best_of_3, (200, 200))
best_of_5 = pygame.transform.scale(best_of_5, (200, 200))
best_of_7 = pygame.transform.scale(best_of_7, (200, 200))
rock = pygame.transform.scale(rock, (150, 150))
paper = pygame.transform.scale(paper, (150, 150))
scissors = pygame.transform.scale(scissors, (150, 150))
play_again_button = pygame.transform.scale(play_again_button, (125, 50))
home_button = pygame.transform.scale(home_button, (75, 75))

computer_icon = pygame.transform.scale(computer_icon, (75, 75))
player_icon = pygame.transform.scale(player_icon, (75, 75))

computer_wins_msg = pygame.transform.scale(computer_wins_msg, (450, 400))
you_win_msg = pygame.transform.scale(you_win_msg, (450, 400))

pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Adobe Garamond Pro Bold', 50)
score_font = pygame.font.SysFont('Consolas', 60)
screen = pygame.display.set_mode([display_width, display_height])
screen.fill(WHITE)
pygame.display.set_caption("Rock, Scissors, Paper!")

choices = ["Rock", "Paper", "Scissors"]

computer_score = 0
player_score = 0
page = 0
game = True

welcome_msg = title_font.render("Welcome to rock, paper, scissors!", True, (43, 114, 255))
choose_game_mode_msg = title_font.render("Choose a game mode.", True, (85, 133, 230))
choose_how_many_rounds = title_font.render("Choose the number of rounds", True, (43, 114, 255))
title = title_font.render("Rock, Paper, or Scissors?", True, (43, 114, 255))
page_1_text = title_font.render("It's a tie!", True, (0, 0, 0))
page_2_text = title_font.render("You lose! Paper covers rock!", True, (255, 0, 0))
page_3_text = title_font.render("You win! Rock smashes scissors!", True, (0, 255, 0))
page_4_text = title_font.render("You win! Paper covers rock!", True, (0, 255, 0))
page_5_text = title_font.render("You lose! Scissors cuts paper!", True, (255, 0, 0))
page_6_text = title_font.render("You lose! Rock smashes scissors!", True, (255, 0, 0))
page_7_text = title_font.render("You win! Scissors cuts paper!", True, (0, 255, 0))

area_classic_game_mode = pygame.Rect(50, 250, 300, 300)
area_best_of_game_mode = pygame.Rect(450, 250, 300, 300)
area_best_of_3 = pygame.Rect(25, 300, 200, 200)
area_best_of_5 = pygame.Rect(300, 300, 200, 200)
area_best_of_7 = pygame.Rect(600, 300, 200, 200)

area_rock = pygame.Rect(50, 200, 150, 150)
area_paper = pygame.Rect(325, 200, 150, 150)
area_scissors = pygame.Rect(625, 200, 150, 150)
area_play_again_button = pygame.Rect(335, 450, 150, 75)
area_home_button = pygame.Rect(720, 520, 75, 75)

page_text = [title, page_1_text, page_2_text, page_3_text, page_4_text, page_5_text, page_6_text, page_7_text]


def page_template(page_number):
    screen.fill(WHITE)
    screen.blit(page_text[page_number], (150, 50))
    screen.blit(play_again_button, (335, 450))
    screen.blit(player_icon, (275, 520))
    screen.blit(computer_icon, (450, 520))
    screen.blit(score, (350, 530))
    screen.blit(home_button, (720, 520))


def classic_mode_page():
    screen.fill(WHITE)
    screen.blit(rock, (50, 200))
    screen.blit(paper, (325, 200))
    screen.blit(scissors, (625, 200))
    screen.blit(title, (200, 50))
    screen.blit(player_icon, (275, 520))
    screen.blit(computer_icon, (450, 520))
    screen.blit(score, (350, 530))
    screen.blit(home_button, (720, 520))


def best_of_mode_page():
    screen.fill(WHITE)
    screen.blit(choose_how_many_rounds, (145, 50))
    screen.blit(best_of_3, (25, 300))
    screen.blit(best_of_5, (300, 300))
    screen.blit(best_of_7, (600, 300))


def home_page():
    screen.fill(WHITE)
    screen.blit(welcome_msg, (145, 50))
    screen.blit(choose_game_mode_msg, (220, 90))
    screen.blit(classic_game_mode, (50, 250))
    screen.blit(best_of_game_mode, (450, 250))


def you_win_page():
    screen.fill(WHITE)
    screen.blit(you_win_msg, (175, 50))
    screen.blit(play_again_button, (335, 450))


def computer_wins_page():
    screen.fill(WHITE)
    screen.blit(computer_wins_msg, (175, 50))
    screen.blit(play_again_button, (335, 450))

next_step = 0
max_score = 100

while game:
    computer_choice = choices[randint(0, 2)]
    if next_step == 0:
        home_page()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if area_classic_game_mode.collidepoint(event.pos):
                    next_step = 1
                    page = 0
                if area_best_of_game_mode.collidepoint(event.pos):
                    next_step = 2

    if next_step == 2:
        best_of_mode_page()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if area_best_of_3.collidepoint(event.pos):
                    next_step = 1
                    max_score = 2
                elif area_best_of_5.collidepoint(event.pos):
                    next_step = 1
                    max_score = 3
                elif area_best_of_7.collidepoint(event.pos):
                    next_step = 1
                    max_score = 5

    elif next_step == 1:
        score = score_font.render('{}:{}'.format(player_score, computer_score), True, (0, 0, 0))
        if page == 0:
            classic_mode_page()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if page == 0:
                    if area_rock.collidepoint(event.pos):
                        if computer_choice == "Rock":
                            page = 1
                            page_template(1)
                        elif computer_choice == "Paper":
                            page = 2
                            page_template(2)
                            computer_score += 1
                        elif computer_choice == "Scissors":
                            page = 3
                            page_template(3)
                            player_score += 1

                    if area_paper.collidepoint(event.pos):
                        if computer_choice == "Rock":
                            page = 4
                            page_template(4)
                            player_score += 1
                        elif computer_choice == "Paper":
                            page = 1
                            page_template(1)
                        elif computer_choice == "Scissors":
                            page = 5
                            page_template(5)
                            computer_score += 1

                    if area_scissors.collidepoint(event.pos):
                        if computer_choice == "Rock":
                            page = 6
                            page_template(6)
                            computer_score += 1
                        elif computer_choice == "Paper":
                            page = 7
                            page_template(7)
                            player_score += 1
                        elif computer_choice == "Scissors":
                            page = 1
                            page_template(1)

                if area_play_again_button.collidepoint(event.pos):
                    page = 0
                if area_home_button.collidepoint(event.pos):
                    next_step = 0
                    player_score = 0
                    computer_score = 0
                    max_score = 100

    if max_score == player_score:
        you_win_page()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if area_play_again_button.collidepoint(event.pos):
                    next_step = 0
                    player_score = 0
                    computer_score = 0
                    max_score = 100
    elif max_score == computer_score:
        computer_wins_page()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if area_play_again_button.collidepoint(event.pos):
                    next_step = 0
                    player_score = 0
                    computer_score = 0
                    max_score = 100

    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    pygame.display.flip()

pygame.quit()
quit()
