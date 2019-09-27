"""
Rock, Scissors, Paper

Group members: Nathan, Danny, Alex, Faraz, Owen
"""
import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
display_width = 800
display_height = 600
rock = pygame.transform.scale((pygame.image.load('rock.jpg')), (150, 150))
paper = pygame.transform.scale((pygame.image.load('paper.png')), (150, 150))
scissors = pygame.transform.scale((pygame.image.load('scissors.jpg')), (150, 150))
button = pygame.transform.scale((pygame.image.load('playagain.png')), (350, 300))

pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Comic Sans MS', 28)
other_font = pygame.font.SysFont('Comic Sans MS', 16)
screen = pygame.display.set_mode([display_width, display_height])
screen.fill(WHITE)
pygame.display.set_caption("Rock, Scissors, Paper")
clock = pygame.time.Clock()

choices = ["Rock", "Paper", "Scissors"]

computer_score = 0
player_score = 0
page = 0
game = True

title = title_font.render("Rock Paper Scissors", True, (0, 0, 0))
page_1_text = title_font.render("It's a tie!", True, (0, 0, 0))
page_2_text = title_font.render("You lose, paper covers rock!", True, (0, 0, 0))
page_3_text = title_font.render("You win, rock smashes scissors!", True, (0, 0, 0))
page_4_text = title_font.render("You win, paper covers rock!", True, (0, 0, 0))
page_5_text = title_font.render("You lose, scissors cuts paper!", True, (0, 0, 0))
page_6_text = title_font.render("You lose, rock smashes scissors", True, (0, 0, 0))
page_7_text = title_font.render("You win, scissors cuts paper", True, (0, 0, 0))

area_rock = pygame.Rect(50, 300, 150, 150)
area_paper = pygame.Rect(325, 300, 150, 150)
area_scissors = pygame.Rect(625, 300, 150, 150)
area_button = pygame.Rect(250, 50, 350, 300)


def page_0():
    screen.fill(WHITE)
    screen.blit(rock, (50, 300))
    screen.blit(paper, (325, 300))
    screen.blit(scissors, (625, 300))
    screen.blit(title, (250, 50))
    screen.blit(player_score_text, (625, 50))
    screen.blit(computer_score_text, (625, 100))


def page_1():
    screen.fill(WHITE)
    screen.blit(page_1_text, (250, 50))
    screen.blit(button, (250, 50))
    screen.blit(player_score_text, (625, 50))
    screen.blit(computer_score_text, (625, 100))


def page_2():
    screen.fill(WHITE)
    screen.blit(page_2_text, (250, 50))
    screen.blit(button, (250, 50))
    screen.blit(player_score_text, (625, 50))
    screen.blit(computer_score_text, (625, 100))


def page_3():
    screen.fill(WHITE)
    screen.blit(page_3_text, (180, 150))
    screen.blit(button, (200, 150))
    screen.blit(player_score_text, (625, 50))
    screen.blit(computer_score_text, (625, 100))


def page_4():
    screen.fill(WHITE)
    screen.blit(page_4_text, (180, 150))
    screen.blit(button, (200, 150))
    screen.blit(player_score_text, (625, 50))
    screen.blit(computer_score_text, (625, 100))


def page_5():
    screen.fill(WHITE)
    screen.blit(page_5_text, (250, 50))
    screen.blit(button, (250, 50))
    screen.blit(player_score_text, (625, 50))
    screen.blit(computer_score_text, (625, 100))


def page_6():
    screen.fill(WHITE)
    screen.blit(page_6_text, (250, 50))
    screen.blit(button, (250, 50))
    screen.blit(player_score_text, (625, 50))
    screen.blit(computer_score_text, (625, 100))


def page_7():
    screen.fill(WHITE)
    screen.blit(page_7_text, (250, 50))
    screen.blit(button, (250, 50))
    screen.blit(player_score_text, (625, 50))
    screen.blit(computer_score_text, (625, 100))


while game:
    computer_score_text = other_font.render('Computer Score: {}'.format(computer_score), True, (0, 0, 0))
    player_score_text = other_font.render('Player Score: {}'.format(player_score), True, (0, 0, 0))


    computer_choice = choices[randint(0, 2)]
    if page == 0:
        page_0()
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        print(x, y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if area_rock.collidepoint(event.pos):
                if computer_choice == "Rock":
                    page = 1
                    page_1()
                elif computer_choice == "Paper":
                    page = 2
                    page_2()
                    computer_score += 1
                elif computer_choice == "Scissors":
                    page = 3
                    page_3()
                    player_score += 1
            if area_button.collidepoint(event.pos):
                page = 0
            if area_paper.collidepoint(event.pos):
                if computer_choice == "Rock":
                    page = 4
                    page_4()
                    player_score += 1
                elif computer_choice == "Paper":
                    page = 1
                    page_1()
                elif computer_choice == "Scissors":
                    page = 5
                    page_5()
                    computer_score += 1
            if area_button.collidepoint(event.pos):
                page = 0
            if area_scissors.collidepoint(event.pos):
                if computer_choice == "Rock":
                    page = 6
                    page_6()
                    computer_score += 1
                elif computer_choice == "Paper":
                    page = 7
                    page_7()
                    player_score += 1
                elif computer_choice == "Scissors":
                    page = 1
                    page_1()
            if area_button.collidepoint(event.pos):
                page = 0

    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    pygame.display.flip()
    print(page)

pygame.quit()
quit()
