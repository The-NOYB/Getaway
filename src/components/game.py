import pygame as pg
import sys, time
from .scene import Scene
from .consts import *

class Game():
    def __init__(self):
        pg.init()

        self.running = True
        self.clock = pg.time.Clock()

        # setting window dimensions and the window itself
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.DIMENSIONS = ( self.WIDTH, self.HEIGHT )
        self.window = pg.display.set_mode( self.DIMENSIONS )
        self.font = pg.font.Font(None, 48)

        # setting up the scene selector
        self.scene = Scene( self.window, self.DIMENSIONS, self.font )

    def run(self):
        # main loop for the App
        while self.running:
            self.clock.tick( 120 )
            self.window.fill( (103,23,104) )
            
            self.events() 
            key_input = pg.key.get_pressed()
            self.scene.selector( key_input )

            # getting the fps and blit-ing it one the screen
            fps = "%.2f" % self.clock.get_fps()
            self.window.blit( self.font.render( fps, True, (0,0,0) ), (0, 0) )
            pg.display.update()
 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
