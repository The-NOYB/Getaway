import pygame as pg
from .gui import Gui
from .map import Map
from .consts import *
from .entities.player import Player
#from .entities.enemies import Enemies
from .entities.renderer import Renderer

class Scene():

    def __init__(self, screen, screen_dimensions, font) -> None:
        self.state = "menu"
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.font = font

        self._map = None
        self.gui = Gui( self.screen, self.screen_dimensions, self.font )

    def menu(self, key_input, mouse_input, runtime) -> None:
        data = self.gui.menu( key_input )

        if isinstance(data, dict):
            self.state = data["state"]
            self.mapObj = Map()
            self.player = Player( data["playerName"], 400, 300 , self.mapObj )
            self.renderer = Renderer( self.player, self.mapObj )

    def game(self, key_input, mouse_input, runtime) -> None:
        pg.draw.rect( self.screen, (100,100,100), (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT) )

        self.player.update( key_input, mouse_input, runtime )
        self.renderer.draw( self.screen )
        self.player.draw( self.screen )
        self.gui.game( self.screen )
        
    def pause(self, key_input, mouse_input, runtime) -> None:
        self.state = self.gui.pause( key_input )

    def selector(self, key_input, mouse_input, runtime ) -> None:

        if self.state == "menu":
            self.menu( key_input, mouse_input, runtime )
        elif self.state == "game":
            self.game( key_input, mouse_input, runtime )
        elif self.state == "pause":
            self.pause( key_input, mouse_input, runtime )
