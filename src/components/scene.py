import pygame as pg
from .gui import Gui
from .entities.player import Player
from .entities.enemies import Enemies

class Scene():

    def __init__(self, screen, screen_dimensions, font) -> None:
        self.state = "menu"
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.font = font

        self._map = None
        self.gui = Gui( self.screen, self.screen_dimensions, self.font )

    def menu(self, key_input) -> None:
        data = self.gui.menu( key_input )

        if isinstance(data, dict):
            self.state = data["state"]
            self.player = Player( data["playerName"] )

    def game(self, key_input) -> None:
        pass
        
    def pause(self, key_input) -> None:
        self.state = self.gui.pause( key_input )

    def selector(self, key_input) -> None:

        if self.state == "menu":
            self.menu( key_input )
        elif self.state == "game":
            self.game( key_input )
        elif self.state == "pause":
            self.pause( key_input )
