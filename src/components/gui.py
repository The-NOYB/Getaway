import pygame as pg

class Gui():
    def __init__(self, screen, screen_dimensions, font) -> None:
        self.screen = screen
        self.screen_dimensions = screen_dimensions
        self.font = font

    def menu(self, key_input) -> dict:

        # displaying the title
        gameName = self.font.render( "Dhoom", True, (0,0,0) )
        centered_pos = [ (self.screen_dimensions[x] - gameName.get_size()[x])//2 for x in range(2) ]
        self.screen.blit(gameName, centered_pos)

        # display other options

        # handling the state of the game
        if key_input[pg.K_RETURN]:
            return {"state" : "game", "playerName": "foobar"}
        return "menu"
    
    def player_creation(self, key_input):# -> dict?:
        pass

    def pause(self, key_input) -> str:

        # display all the pause options

        # handling the state of the game
        if key_input[pg.K_RETURN]:
            return "game"
        return "pause"
