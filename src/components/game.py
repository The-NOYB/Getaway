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
        self.font = pg.font.Font(None, 48)

        # setting up the scene selector
        self.scene = Scene( self.window, self.DIMENSIONS, self.font )

    def run(self) -> None:
        # main loop for the App
        while self.running:
            self.clock.tick( 120 )
            self.window.fill( (103,23,104) )
            
            self.events() 

            mouse_pos_x = pg.mouse.get_pos()[0]
            if  mouse_pos_x <= 10 or mouse_pos_x >= WIDTH-10: # setting the mouse_pos_x to center of screen if it is near edge
                pg.mouse.set_pos( (HALF_WIDTH, HALF_HEIGHT) )
            mouse_input = pg.mouse.get_rel() + pg.mouse.get_pressed()

            key_input = pg.key.get_pressed()
            self.scene.selector( key_input, mouse_input )

            # getting the fps and blit-ing it one the screen
            fps = "%.2f" % self.clock.get_fps()
            self.window.blit( self.font.render( fps, True, (0,0,0) ), (0, 0) )
            pg.display.update()
 
    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
