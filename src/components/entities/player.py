import pygame as pg
import math
from ..consts import *

class Player():
    def __init__(self, name, x, y, mapObj) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.range = 120
        self.angle = 0
#        self.walkDir = 0
#        self.strafeDir = 0
        self.mapObj = mapObj
        self.turnDir = 0
        self.rotationSpeed = 2 * ( math.pi / 180 )
        self.speed = 2
        self.hitwall = False

    def draw(self, screen) -> None:
        pg.draw.circle(screen, (244,244,244), (HALF_WIDTH, HALF_HEIGHT), 4)

    def update(self, key_input, mouse_input) -> None:

        self.turnDir = 0
        dx, dy = 0, 0 
#        self.walkDir = 0

        if not self.hitwall:
            if key_input[pg.K_w]:
                dx = 1 * math.cos( self.angle ) * self.speed
                dy = 1 * math.sin( self.angle ) * self.speed
            if key_input[pg.K_s]:
                dx = -1 * math.cos( self.angle ) * self.speed
                dy = -1 * math.sin( self.angle ) * self.speed
    
            # these two do not work properly
            if key_input[pg.K_d]:
                dx = -1 * math.sin( self.angle ) * self.speed
                dy = 1 * math.cos( self.angle ) * self.speed
            if key_input[pg.K_a]:
                dx = 1 * math.sin( self.angle ) * self.speed
                dy = -1 * math.cos( self.angle ) * self.speed

        if mouse_input[0] > 0:
            self.turnDir = 1
        if mouse_input[0] < 0: 
            self.turnDir = -1

        # creating temp variables for checking walls
        _x, _y = self.x + dx, self.y + dy
        if not self.mapObj.is_wall(_x, _y) :
            self.x, self.y = _x, _y

        self.angle += self.turnDir * self.rotationSpeed
