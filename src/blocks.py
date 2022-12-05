import pygame
import random

class Blocks():
    def __init__(self):
        self.I =[[0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]]

        self.T =[[0,0,1,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

        self.Z = [[0,1,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

        self.S =[[0,0,1,1,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

        self.L = [[0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0]]

        self.J = [[0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0]]
    
    def generate_random_block(self):
        list = [self.I, self.J, self.L, self.S, self.T, self.Z]
        pick = random.randint(0,5)
        new_block = list[pick]
        return new_block
