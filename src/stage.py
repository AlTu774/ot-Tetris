import pygame
from blocks import Blocks

class Stage():
    def __init__(self):
        self.map = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
    
    def add_new_block(self):
        block = Blocks()
        block = block.generate_random_block()
        for y in range(0,4):
            for x in range(0,5):
                self.map[y][x+3] = block[y][x]
    
    def drop_block(self):
        for y in range(19,-1,-1):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    if y == 19:
                        self.freeze_block()
                        self.add_new_block()
                        return
                    self.map[y][x] = 0
                    self.map[y+1][x] = 1
                    print(y,x)
    
    def freeze_block(self):
        for y in range(0,20):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    self.map[y][x] = 2



    