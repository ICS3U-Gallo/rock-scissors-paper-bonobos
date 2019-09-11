"""
Rock, Scissors, Paper

Group members: Nathan, Danny, 
"""
import pygame
import random

BLACK = (0,0,0)
WHITE = (255, 255, 255)
display_width = 800
display_height = 600
pygame.init()
screen = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption("Rock, Scissors, Paper")
clock = pygame.time.Clock()
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

pygame.quit()
quit()
