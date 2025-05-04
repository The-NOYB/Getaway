import pygame as pg
import time

class Gui():
    def __init__(self, screen, screen_dimensions, fonts) -> None:
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.title_font, self.font = fonts
        self.selected_option = 0

        self.interaction = .25
        self.interaction_time = 0

    def menu(self, key_input, runtime) -> dict:

        centered_pos = ( self.screen.get_width()//2, self.screen.get_height()//2 )

        # displaying the title
        gameName = self.title_font.render( "Getaway", True, (0,0,0) )
        self.screen.blit( gameName, (centered_pos[0] - gameName.get_width()//2, centered_pos[1] * .25) )

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
            pos = int(centered_pos[0] - option.get_width()//2), int(centered_pos[1] * .9 + index * spacing)
            if index == self.selected_option:
                rect_cords =  pos + options_but_rendered[self.selected_option].get_size()
                pg.draw.rect( self.screen, (100,100,100),  rect_cords )
            self.screen.blit(  option, pos)

        # handling the state of the game
        if key_input[pg.K_RETURN]:
            return {"state" : "game", "playerName": "foobar"}
        return "menu"
    
    def player_creation(self, key_input):# -> dict?:
        pass

    def game_ui(self, screen, player) -> None:
        pass

    def pause(self, key_input) -> str:

        # display all the pause options

        # handling the state of the game
        if key_input[pg.K_RETURN]:
            return "game"
        return "pause"
