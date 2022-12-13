import pygame
import random

class Blocks():
    """Luokka, jossa on kaikki eri palikoiden muodot nimetty: I,T,Z,S,L,J ja O."""
    def __init__(self):
        self.I =[[[3,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]],
        [[3,0,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]],
        [[3,0,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]]]

        self.T =[[[3,0,1,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,0,1,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0]],
        [[3,0,0,0,0],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,1,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]]]

        self.Z = [[[3,1,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,1,1,0,0],
        [0,1,0,0,0],
        [0,0,0,0,0]],
        [[3,1,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,1,1,0,0],
        [0,1,0,0,0],
        [0,0,0,0,0]]]

        self.S =[[[3,0,1,1,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,1,0],
        [0,0,0,0,0]],
        [[3,0,1,1,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,1,0],
        [0,0,0,0,0]]]

        self.L = [[[3,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0]],
        [[3,0,0,0,0],
        [0,1,1,1,0],
        [0,1,0,0,0],
        [0,0,0,0,0]],
        [[3,1,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0]]]

        self.J = [[[3,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0]],
        [[3,1,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,0,1,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]],
        [[3,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0]]]

        self.O = [[[3,1,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,1,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,1,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]],
        [[3,1,1,0,0],
        [0,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]]

        
    
    def generate_random_block(self):
        """Tuottaa uuden palikan valitsemalla sen satunnaisesti listasta.
        
        Returns:
            new_block: Palikka, jonka muodot on matriiseina listassa.
        """
        list = [self.I, self.J, self.L, self.S, self.T, self.Z, self.O]
        pick = random.randint(0,6)
        new_block = list[pick]
        return new_block
