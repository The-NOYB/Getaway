import pygame as pg
from os import listdir, getcwd
from os.path import join
from ..consts import *
from .ray import Ray
from .player import Player

class Renderer():
    def __init__( self, player, mapObj ):
        self.player = player
        self.mapObj = mapObj
        self.rays = []
        self.texture_data = []
        self.objects_to_render = []

        # might just make a separate class outside to do textures we'll see later
        path = join( getcwd(), "components", "resources","textures" )
        # getting the textures
        self.textures = []
        for texture in listdir( path):
            path_to_texture = str(join(path, texture))
            self.textures.append( pg.transform.scale(pg.image.load(path_to_texture), (256,256)).convert() )

    def castAll( self ):
        self.rays = []
        self.texture_data = []
        start_angle = ( self.player.angle - FOV/2 )

        for i in range( NUM_RAYS ):
            ray = Ray( start_angle, self.player, self.mapObj )
            ray.cast()
            self.rays.append( ray )
            line_height = ( 64 / ray.distance ) * WIDTH # half of the screen width divided by tan of half of the fov

            start_angle += FOV/NUM_RAYS
            # getting data for calculation of textures
            self.texture_data.append( (ray.distance, line_height, 1, ray.offset) )

    """
    The drawing of texture requires some basic data such as distance from
    player, and line_height from the rays and what texture to be used 
    and some offset for some particular cases.  
    This data is stored in texture_data and using this data 
    in draw_texture we calculate the texture subsurface/columns 
    which needs to be rendered on screen.
    The column/subsurface data is then stored in objects_to_render which 
    will have distance, wall_column and wall_pos which will be used for 
    finally drawing the textures.
    """

    def calc_texture(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.texture_data):
            distance, line_height, texture, offset = values

            # handling the case where we get right into the wall
            if line_height < HEIGHT:
                # texture is the value of which wall texture to blit and self.textures will have all the available textures
                wall_column = self.textures[texture].subsurface( offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE )
                # scaling the column of the wall
                wall_column = pg.transform.scale( wall_column, (SCALE, line_height) )
                wall_pos = ( ray * SCALE, HALF_HEIGHT - line_height //2 )
            else:
                texture_height = TEXTURE_SIZE * HEIGHT / line_height
                wall_column = self.textures[texture].subsurface( offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2, SCALE, texture_height )
                wall_column = pg.transform.scale( wall_column, (SCALE, HEIGHT) )
                wall_pos = ( ray * SCALE, 0 )
    
            self.objects_to_render.append( (distance, wall_column, wall_pos) )

    def draw( self, screen ):
        self.castAll()
        self.calc_texture()

        sorted_list = sorted(self.objects_to_render, key=lambda t:t[0], reverse=True)
        for distance, image, pos in sorted_list:
                screen.blit(image, pos)

        # this was the code for drawing rects as walls
#        counter = 0
#        for ray in self.rays:
#            # do not touch the code below this ihdk how it works
#            line_height = ( 64 / ray.distance ) * WIDTH # half of the screen width divided by tan of half of the fov
#
#            # where to begin the drawing of walls
#            draw_begin = HEIGHT//2 - line_height//2
#            # where to end the the drawing of walls
#            draw_end = line_height
#
#            pg.draw.rect( screen, ray.color, (counter*RES, draw_begin, RES, draw_end) )
#
#            counter += 1
