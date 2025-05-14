import pygame as pg
import math, time
from ..consts import *

"""
So far the only thing I could think of is traps
- Red wall, passing through it will kill the player, probably will just activate and de-activate
- Ray gun, will shoot a (slow) projectile at the player if they collide player dies.
- Time Bombs, nothing if activated player will have to do before he runs out of time, needs a gui
"""

#class Enemies():
#    def __init__(self, x, y, player, path) -> None:
#        self.x, self.y = x, y 
#        self.player = player        
#        self.path = path
#        self.image = 0
#
#    def update(self) -> None:
#        dx = self.player.x - self.x
#        dy = self.player.y - self.y
#        self.dx, self.dy = dx, dy
#        self.angle = math.atan2(dy, dx)
#
#        delta =  self.angle - self.player.angle
#        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
#            delta += math.tau
#
#        delta_rays = delta / (FOV / NUM_RAYS)
#        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE
#    
#    def draw(self) -> None:
#        pass
