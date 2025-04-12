import pygame as pg
from .consts import *

class Map():
    def __init__(self) -> None:
        self.start = [3, 0]
        self.grid = [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                [1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                ]

    def generate(self) -> None:
        pass
