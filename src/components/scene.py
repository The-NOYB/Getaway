import pygame as pg
from .gui import Gui
from .map import Map
from .consts import *
from .entities.player import Player
from .entities.sprites import SpriteObject 
from .entities.renderer import Renderer

class Scene():

    def __init__(self, screen, screen_dimensions, fonts) -> None:
        self.state = "menu"
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.title_font, self.font = fonts

        self.mapObj = None
        self.gui = Gui( self.screen, self.screen_dimensions, fonts)
        self.cached_screen = None

    def menu(self, key_input, mouse_input, runtime) -> None:
        data = self.gui.menu( key_input, runtime)

        if isinstance(data, dict):
            self.state = data["state"]
            self.mapObj = Map()
            self.player = Player( data["playerName"], 400, 300 , self.mapObj )
            self.sprite = SpriteObject(self.player)
            self.renderer = Renderer( self.player, self.mapObj )

    def game(self, key_input, mouse_input, runtime) -> None:
        pg.draw.rect( self.screen, (100,100,100), (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT) )

        self.player.update( key_input, mouse_input, runtime )
        self.renderer.draw( self.screen )
        self.player.draw( self.screen )

        # below cuz i want the cached_screen to have all the stuff on window
        if key_input[pg.K_ESCAPE]:
            self.cached_screen = pg.transform.box_blur( self.screen.copy(), 10 )
            self.state = "pause"
        
    def pause(self, key_input, mouse_input, runtime, previous_screen) -> None:
        self.state = self.gui.pause( key_input, mouse_input, runtime, previous_screen )

    def selector(self, key_input, mouse_input, runtime ) -> None:

        if self.state == "menu":
            self.menu( key_input, mouse_input, runtime )
        elif self.state == "game":
            self.game( key_input, mouse_input, runtime )
            self.gui.game_ui( self.screen, self.player, runtime )
        elif self.state == "pause":
            self.pause( key_input, mouse_input, runtime, self.cached_screen )
