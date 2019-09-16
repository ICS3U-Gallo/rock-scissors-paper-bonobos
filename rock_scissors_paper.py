"""
Rock, Scissors, Paper

Group members: Nathan, Danny, 
"""
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
display_width = 800
display_height = 600

rock = pygame.transform.scale((pygame.image.load('rock.jpg')), (150, 150))
paper = pygame.transform.scale((pygame.image.load('paper.png')), (150, 150))
scissors = pygame.transform.scale((pygame.image.load('scissors.jpg')), (150, 150))

pygame.init()
screen = pygame.display.set_mode([display_width, display_height])
screen.fill(WHITE)
pygame.display.set_caption("Rock, Scissors, Paper")
clock = pygame.time.Clock()

game = True


def draw():
    screen.blit(rock, (50, 300))
    screen.blit(paper, (325, 300))
    screen.blit(scissors, (625, 300))


while game:
    for event in pygame.event.get():
        draw()
        x, y = pygame.mouse.get_pos()
        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()
pygame.quit()
quit()
