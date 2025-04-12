import pygame as pg
import math
from ..consts import *

class Player():
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.range = 120
        self.angle = 0
        self.walkDir = 0
        self.turnDir = 0
        self.rotationSpeed = 2 * ( math.pi / 180 )
        self.speed = 2

    def draw(self, screen) -> None:
        pg.draw.circle(screen, (244,244,244), (HALF_WIDTH, HALF_HEIGHT), 4)

    def update(self, key_input, mouse_input) -> None:
    
        self.turnDir = 0
        self.walkDir = 0

        if key_input[pg.K_w]:
            self.walkDir = 1
        if key_input[pg.K_s]:
            self.walkDir = -1

        # these two do not work properly
        if key_input[pg.K_d]:
            self.y += 1
        if key_input[pg.K_a]:
            self.y -= 1

        if mouse_input[0] > 0:
            self.turnDir = 1
        if mouse_input[0] < 0: 
            self.turnDir = -1

        self.angle += self.turnDir * self.rotationSpeed

        self.x += self.walkDir * math.cos( self.angle ) * self.speed
        self.y += self.walkDir * math.sin( self.angle ) * self.speed
