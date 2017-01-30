import pygame, sys
from pygame.locals import *

pygame.init()

class Invader():

    def __init__(self,invader_position_x,right_boundary,keypress):

        self.invader_position_x= invader_position_x
        self.right_boundary=right_boundary
        self.keypress= keypress

    def invader_move(self,keypress,right_boundary,invader_position_x):#Moves the invader
        if self.invader_position_x> right_boundary:#Right boundary
            invader_position_x=right_boundary-5

        if self.invader_position_x<0:#Left boundary
            invader_position_x= 5

        if keypress[K_RIGHT]:# right
            self.invader_position_x = invader_position_x+ 5

        if keypress[K_LEFT]:# left
            self.invader_position_x =invader_position_x- 5

        return self.invader_position_x
