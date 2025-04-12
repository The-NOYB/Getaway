import pygame as pg
from .consts import *

class Map():
    def __init__(self) -> None:
        self.map = { "1": 
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1]
                    }
        self.start = [3, 0]

    def generate(self) -> None:
        pass
    
    def C(self):
        pass
