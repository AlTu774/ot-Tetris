import pygame
import random

class Blocks():
    """Luokka, jossa on kaikki eri palikoiden muodot nimetty: I,T,Z,S,L,J ja O.
    Attributes:
            spare: Lista joka sisältää vara palikan.

            rotation_b: Eli rotation block, jota käytetään palikan sijainnin muistamiseen kentässä,
            ja palikan kääntämiseen.
        
            rotations: Sisältää palikan eri asennot ja tiedon sen hetkisestä asennosta.

            spare: Vara-palikan lista.
            """
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
        [[3,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
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
        [[3,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,1,0],
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

        self.spare = []
        self.rotation_b = (0, (0,0))
        self.rotations = []        
    
    def generate_random_block(self):
        """Tuottaa uuden palikan valitsemalla sen satunnaisesti listasta.
        Returns:
            new_block: Palikka, jonka muodot on matriiseina listassa.
        """
        list = [(self.I, "cyan"), (self.J, "blue"), (self.L, "orange"), (self.S, "green"), (self.T, "purple"), (self.Z, "red"), (self.O, "yellow")]
        pick = random.randint(0,6)
        new_block = list[pick]
        return new_block

    def move_rotation_b(self, dir):
        """Liikuttaa kääntämiseen käytettävää tilaa oikealle, vasemmalle tai alas. 
        Args:
            dir: Siirron suunta, joko "R", "L" tai "D".
        """
        if dir == "D":
            old = self.rotation_b
            self.rotation_b = (old[0], ((old[1][0]+1),old[1][1]))
            return
        
        if dir == "L":
            x = -1
        elif dir == "R":
            x = 1

        old = self.rotation_b
        self.rotation_b = (old[0], (old[1][0],(old[1][1]+x)))
