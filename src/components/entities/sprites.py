import pygame as pg
from ..consts import *
import math, time

class SpriteObject():
    def __init__(self, player, pos=(10.5, 3.5), scale=0.7, shift=0.27):
        self.player = player
        self.x, self.y = pos
#        self.image = pg.image.load(path).convert_alpha()
#        self.IMAGE_WIDTH = self.image.get_width()
#        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
#        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.angle, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self):
        # getting the scale for the projection
        projection_scale = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        projection_width, projection_height = projection_scale * self.IMAGE_RATIO, projection_scale

        # scaling the image
        image = pg.transform.scale(self.image, (projection_width, projection_height))

        # getting position of the projection by 
        self.sprite_half_width = projection_width // 2
        height_shift = projection_height * self.SPRITE_HEIGHT_SHIFT
        position = (self.screen_x - self.sprite_half_width, HALF_HEIGHT - projection_height // 2 + height_shift)

        return (self.norm_dist, image, position)

    def get_sprite(self):
        # getting the difference position and angle
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.angle = math.atan2(dy, dx)

        delta = self.angle - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / (FOV // NUM_RAYS)
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if ( -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) ) and (self.norm_dist > 0.5):
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()
