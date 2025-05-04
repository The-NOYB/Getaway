import pygame as pg
import sys, time
from .scene import Scene
from .consts import *

class Game():
    def __init__(self) -> None:
        pg.init()

        pg.mouse.set_visible(False)
        self.running = True
        self.clock = pg.time.Clock()

        # setting window dimensions and the window itself
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.DIMENSIONS = ( self.WIDTH, self.HEIGHT )
        self.window = pg.display.set_mode( self.DIMENSIONS )
        self.fonts = pg.font.Font(None, 102), pg.font.Font(None, 48)

        # setting up the scene selector
        self.scene = Scene( self.window, self.DIMENSIONS, self.fonts )
        self.runtime = 0

    def run(self) -> None:
        # main loop for the App
        while self.running:
            self.clock.tick( 120 )
            self.runtime = time.time()
            self.window.fill( (103,23,104) )
            
            self.events() 

            mouse_pos_x = pg.mouse.get_pos()[0]
            if  mouse_pos_x < 50 or mouse_pos_x > WIDTH-50: # setting the mouse_pos_x to center of screen if it is near edge
                pg.mouse.set_pos( (HALF_WIDTH, HALF_HEIGHT) )
            mouse_input = pg.mouse.get_rel() + pg.mouse.get_pressed()

            key_input = pg.key.get_pressed()
            self.scene.selector( key_input, mouse_input, self.runtime )

            self.show_fps()
            pg.display.update()
 
    def show_fps(self) -> None:
        # getting the fps and blit-ing it one the screen
        fps = "%.2f" % ( 1 / ( time.time() - self.runtime ) )
        self.window.blit( self.fonts[1].render( fps, True, (0,0,0) ), (0, 0) )

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
