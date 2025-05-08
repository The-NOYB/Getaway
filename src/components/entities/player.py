import pygame as pg
import math, time
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
        self.moving = True
        self.mapObj = mapObj
        self.turnDir = 0
        self.rotationSpeed = 2.1 * ( math.pi / 180 )
        self.speed = 2
        self.hitwall = False

        # length != distance continues the dash
        self.dash_length = 225
        self.dash_distance = 0
        self.dash_speed = 9
        self.has_dashed = False
        self.dash_at = 0
        self.dash_cooldown = 4 # 4 seconds
        self.dash_dir = ""

    def draw(self, screen) -> None:
        pg.draw.circle(screen, (244,244,244), (HALF_WIDTH, HALF_HEIGHT), 4)

    def update(self, key_input, mouse_input, runtime) -> None:

        self.turnDir = 0
        dx, dy = 0, 0 

        dash_able_time = (runtime - self.dash_at > self.dash_cooldown)
        dash_able_condition = (self.dash_length != self.dash_distance)

        # if space is pressed while time and conditions for dash is satisfied and then dash
        if not self.hitwall and key_input[pg.K_SPACE] and dash_able_time and dash_able_condition:
            self.has_dashed = True
            self.dash_distance = 0
            self.dash_at = time.time()
            if key_input[pg.K_w]:
                self.dash_dir = "front"
            elif key_input[pg.K_s]:
                self.dash_dir = "back"
            elif key_input[pg.K_a]:
                self.dash_dir = "left"
            elif key_input[pg.K_d]:
                self.dash_dir = "right"
        # if dash is True but conditions are false then stop dashing and reset variables
        elif self.has_dashed and (not dash_able_condition) and (not dash_able_time):
            self.has_dashed = False
            self.dash_distance = 0

        if not self.hitwall:
            # player needs to hold direction key till the end of the dash to complete dash
            if self.has_dashed and self.dash_dir == "front":
                self.dash_distance += self.dash_speed
                dx = 1 * math.cos( self.angle ) * self.dash_speed
                dy = 1 * math.sin( self.angle ) * self.dash_speed
            elif self.has_dashed and self.dash_dir == "back":
                self.dash_distance += self.dash_speed
                dx = -1 * math.cos( self.angle ) * self.dash_speed
                dy = -1 * math.sin( self.angle ) * self.dash_speed
            elif key_input[pg.K_w]:
                dx = 1 * math.cos( self.angle ) * self.speed
                dy = 1 * math.sin( self.angle ) * self.speed
                self.moving = True
            elif key_input[pg.K_s]:
                dx = -1 * math.cos( self.angle ) * self.speed
                dy = -1 * math.sin( self.angle ) * self.speed
                self.moving = True
            else:
                self.moving = False
    
            # these two do
            if self.has_dashed and self.dash_dir == "right":
                self.dash_distance += self.dash_speed
                dx = -1 * math.sin( self.angle ) * self.dash_speed
                dy = 1 * math.cos( self.angle ) * self.dash_speed
            elif self.has_dashed and self.dash_dir == "left":
                self.dash_distance += self.dash_speed
                dx = 1 * math.sin( self.angle ) * self.dash_speed
                dy = -1 * math.cos( self.angle ) * self.dash_speed
            elif key_input[pg.K_d]:
                dx = -1 * math.sin( self.angle ) * self.speed
                dy = 1 * math.cos( self.angle ) * self.speed
                self.moving = True
            elif key_input[pg.K_a]:
                dx = 1 * math.sin( self.angle ) * self.speed
                dy = -1 * math.cos( self.angle ) * self.speed
                self.moving = True
            else:
                self.moving = False

        if mouse_input[0] > 0:
            self.turnDir = 1
        if mouse_input[0] < 0: 
            self.turnDir = -1

        # creating temp variables for checking walls
        _x, _y = self.x + dx, self.y + dy
        if _x < (WIDTH - 1.1 * TILESIZE) and _y < (HEIGHT - 1.1 * TILESIZE) and _x > TILESIZE * 1.1  and _y > TILESIZE * 1.1:
            if self.has_dashed:
                if not self.mapObj.is_wall(self.x, _y) :
                    self.y = _y
                else:
                    self.reduce_dash( "y", _y )
                    self.dash_distance = self.dash_length

                if not self.mapObj.is_wall(_x, self.y) :
                    self.x = _x
                else:
                    self.reduce_dash( "x", _x )
                    self.dash_distance = self.dash_length

            if not self.mapObj.is_wall(self.x, _y) :
                self.y = _y
            if not self.mapObj.is_wall(_x, self.y) :
                self.x = _x

        self.angle += self.turnDir * self.rotationSpeed

    def reduce_dash(self, comp, val):
        if comp == "y" and self.y - val > 0:
            constant = 1.1
        elif comp == "y" and self.y - val < 0:
            constant = -1.1
        elif comp == "x" and self.x - val > 0:
            constant = 1.1
        elif comp == "x" and self.x - val < 0:
            constant = -1.1

        while  (True):
            val += constant

            if comp == "y" and not self.mapObj.is_wall(self.x, val):
                self.y = val
                break
            elif comp == "x" and not self.mapObj.is_wall(val, self.y):
                self.x = val
                break
