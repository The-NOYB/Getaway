import pygame as pg
import time, math
from .consts import *

class Gui():
    def __init__(self, screen, screen_dimensions, fonts) -> None:
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.title_font, self.font = fonts
        self.selected_option = 0

        self.interaction = .25
        self.interaction_time = 0

    def menu(self, key_input, runtime) -> dict:

        # displaying the title
        gameName = self.title_font.render( "Getaway", True, (0,0,0) )
        self.screen.blit( gameName, (HALF_WIDTH - gameName.get_width()//2, HALF_HEIGHT * .25) )

        # display other options
        options = ("START", "SETTINGS", "QUIT")
        options_but_rendered = [ self.font.render( option, True, (0,0,0) ) for option in options ]
        spacing = 75

        if key_input[pg.K_DOWN] and (runtime  - self.interaction_time > self.interaction):
            self.selected_option += 1
            if self.selected_option == 3:
                self.selected_option = 0
            self.interaction_time = runtime

        elif key_input[pg.K_UP] and (runtime  - self.interaction_time > self.interaction):
            self.selected_option -= 1 
            if self.selected_option < 0:
                self.selected_option = 2
            self.interaction_time = runtime

        for index, option in enumerate(options_but_rendered):
            pos = int(HALF_WIDTH - option.get_width()//2), int(HALF_HEIGHT * .9 + index * spacing)
            if index == self.selected_option:
                rect_cords =  pos + options_but_rendered[self.selected_option].get_size()
                pg.draw.rect( self.screen, (150,150,0),  rect_cords )
            self.screen.blit(  option, pos)

        # handling the state of the game
        if key_input[pg.K_RETURN] and self.selected_option == 0:
            return {"state" : "game", "playerName": "foobar"}
        elif key_input[pg.K_RETURN] and self.selected_option == 1:
            pass
        elif key_input[pg.K_RETURN] and self.selected_option == 2:
            pg.event.post( pg.event.Event(pg.QUIT, {}) )
        return "menu"
    
    def player_creation(self, key_input):# -> dict?:
        pass

    def game_ui(self, screen, player, runtime) -> None:
        cooldown_calc = math.pi * 2 * (runtime - player.dash_at) / player.dash_cooldown + 1.5708

        if cooldown_calc > math.pi*2.5:
            pg.draw.arc(screen, (93,125,145), (WIDTH-80,50,60,60), 1.5708, math.pi*2.5, 10)
            pg.draw.circle(screen, (200,200,200), (WIDTH-50, 80), 20)
        else:
            pg.draw.circle(screen, (100,100,100), (WIDTH-50, 80), 29)
            pg.draw.arc(screen, (93,125,145), (WIDTH-80,50,60,60), 1.5708, cooldown_calc, 10)
            pg.draw.circle(screen, (200,200,200), (WIDTH-50, 80), 20)

    def pause(self, key_input, mouse_input, runtime, previous_screen) -> str:

        self.screen.blit( previous_screen, (0,0) )
        # display all the pause options
        options = ("RESUME", "SETTINGS", "QUIT")
        options_but_rendered = [ self.font.render( option, True, (0,0,0) ) for option in options ]
        spacing = 75

        if key_input[pg.K_DOWN] and (runtime  - self.interaction_time > self.interaction):
            self.selected_option += 1
            if self.selected_option == 3:
                self.selected_option = 0
            self.interaction_time = runtime

        elif key_input[pg.K_UP] and (runtime  - self.interaction_time > self.interaction):
            self.selected_option -= 1 
            if self.selected_option < 0:
                self.selected_option = 2
            self.interaction_time = runtime

        for index, option in enumerate(options_but_rendered):
            pos = int(HALF_WIDTH - option.get_width()//2), int(HALF_HEIGHT * .9 + index * spacing)
            if index == self.selected_option:
                rect_cords =  pos + options_but_rendered[self.selected_option].get_size()
                pg.draw.rect( self.screen, (150,150,0),  rect_cords )
            self.screen.blit(  option, pos)

        # handling the state of the game
        if key_input[pg.K_RETURN] and self.selected_option == 0:
            return "game"
        elif key_input[pg.K_RETURN] and self.selected_option == 1:
            pass
        elif key_input[pg.K_RETURN] and self.selected_option == 2:
            pg.event.post( pg.event.Event(pg.QUIT, {}) )
        return "pause"
