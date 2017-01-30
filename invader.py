import pygame, sys
from pygame.locals import *

pygame.init()

class Invader():

    def __init__(self,x,y):
        self.image = pygame.image.load("rocket_sprite.gif")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen_rect, keypress):

        if keypress[pygame.K_RIGHT]:  # right
            self.rect.x += 15

        elif keypress[pygame.K_LEFT]: # left
            self.rect.x -= 15

        if self.rect.right > screen_rect.right: # right boundary
            self.rect.right = screen_rect.right

        if self.rect.left < screen_rect.left:
            self.rect.left = screen_rect.left
