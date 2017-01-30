# IMPORTS
import pygame
import sys
from pygame.locals import *
import invader

# pygame.init()
# ###################
# # IMAGE SIZE AND FPS
# width = 800
# height = 600
# white = (225, 225, 225)  # The colour white
# fps = 30
# fpsClock = pygame.time.Clock()
# DISPLAY = pygame.display.set_mode((width, height))
# #################
#
# # OTHER VARIABLES
# pygame.display.set_caption('space invaders!')
#
# invader_sprite = pygame.image.load("rocket_sprite.gif")
# invader_sprite= pygame.transform.scale(invader_sprite,(90,90))
# invader_lenght = 100
#
# invader_position_x = 400
# invader_position_y = 490
# right_boundary = width - invader_lenght
#
# keypress = ""
# my_invader = invader.Invader(
#     invader_position_x, right_boundary, keypress)  # Initialise Invader
#
# while True:  # main game loop
#     DISPLAY.fill(white)
#     DISPLAY.blit(invader_sprite, (invader_position_x, invader_position_y))
#     keypress = pygame.key.get_pressed()  # finds what key the user is pressing
#
#     invader_position_x = my_invader.invader_move(
#         keypress, right_boundary, invader_position_x)  # Get position X
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     # print(event)
#     pygame.display.update()
#     fpsClock.tick(fps)





# --- constants ---

WIDTH = 800
HEIGHT = 600
FPS = 30

WHITE = (225, 225, 225)

# --- classes ---


# - init -

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption('Rocket invaders!')

# - objects -

my_invader = invader.Invader(400, 560)

# - mainloop -

fps_clock = pygame.time.Clock()

while True: # main game loop

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keypress = pygame.key.get_pressed()

    # - updates -

    my_invader.update(screen_rect, keypress)

    # - draws -

    screen.fill(WHITE)
    my_invader.draw(screen)
    pygame.display.update()

    # - FPS -

    fps_clock.tick(FPS)
