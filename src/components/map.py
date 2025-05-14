import pygame as pg
from .consts import *

"""
Idea so far is that the class Map will manage the maps and levels
Each Level will consitis of several grids, i.e. a list of grids
Data of each lvl will be stored in a json file
Each grid will have info such as starting position, next_grid/next_lvl properties, enemies
After the condition for one grid is satisfied the player will be teleported to the next grid
Out of all the grid within each lvl only one would have the lvl-ending property
There could be recursive gameplay such as get a key in final grid and come to some previous/early grid to pass the lvl
Level -> Grids -> Info
"""
class Map():
    def __init__(self) -> None:
        self.start = [0, 0]

        self.grid = [
                [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,5,6,5,6,5,6,5,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,5,6,5,6,5,6,5,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,5,6,5,6,5,6,5,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,5,6,5,6,5,6,5,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                ]

    def generate(self) -> None:
        pass

    def is_wall(self, x, y) -> bool:
        return self.grid[int(y // TILESIZE)][int(x // TILESIZE)]
