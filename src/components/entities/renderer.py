import pygame as pg
from ..consts import *
from .ray import Ray
from .player import Player

class Renderer():
    def __init__( self, player, mapGrid ):
        self.player = player
        self.mapGrid = mapGrid
        self.rays = []

    def castAll( self ):
        self.rays = []
        start_angle = ( self.player.angle - FOV/2 )

        for i in range( NUM_RAYS ):
            ray = Ray( start_angle, self.player, self.mapGrid )
            ray.cast()
            self.rays.append( ray )

            start_angle += FOV/NUM_RAYS

    def draw( self, screen ):
        self.castAll()

        counter = 0
        for ray in self.rays:
            # do not touch the code below this ihdk how it works
            line_height = ( 64 / ray.distance ) * 480 # half of the screen width divided by tan of half of the fov

            # where to begin the drawing of walls
            draw_begin = HEIGHT//2 - line_height//2
            # where to end the the drawing of walls
            draw_end = line_height

            pg.draw.rect( screen, ray.color, (counter*RES, draw_begin, RES, draw_end) )

            counter += 1
