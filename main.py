# IMPORTS
import pygame
import sys
from pygame.locals import *
import invader

pygame.init()
###################
# IMAGE SIZE AND FPS
width = 800
height = 600
fps = 30
fpsClock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((width, height))
#################

# OTHER VARIABLES
pygame.display.set_caption('space invaders!')
white = (225, 225, 225)  # The colour white
invader_sprite = pygame.image.load("rocket_sprite.gif")
invader_sprite= pygame.transform.scale(invader_sprite,(90,90))
invader_lenght = 100

invader_position_x = 400
invader_position_y = 490
right_boundary = width - invader_lenght

keypress = ""
my_invader = invader.Invader(
    invader_position_x, right_boundary, keypress)  # Initialise Invader

while True:  # main game loop
    DISPLAY.fill(white)
    DISPLAY.blit(invader_sprite, (invader_position_x, invader_position_y))
    keypress = pygame.key.get_pressed()  # finds what key the user is pressing

    invader_position_x = my_invader.invader_move(
        keypress, right_boundary, invader_position_x)  # Get position X

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # print(event)
    pygame.display.update()
    fpsClock.tick(fps)
