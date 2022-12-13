import pygame
from blocks import Blocks

class Stage():
    """Luokka jollaa ylläpidetään pelikenttän tilaa.

    Attributes:
        map: Kartoitus kentästä. Kentässä 0 on tyhjä tila, 1 on palikka ja 2 on pysähtynyt palikka.
        
        rotation_b: eli rotation block, jota käytetään palikan sijainnin muistamiseen kentässä,
        ja palikan kääntämiseen.
        
        rotations: Sisältää palikan eri asennot ja tiedon sen hetkisestä asennosta.

     """
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

        self.rotation_b = (0, (0,0))
        self.rotations = []
    
    def add_new_block(self):
        """Lisää uuden palikan kenttään."""
        block = Blocks()
        block = block.generate_random_block()
        for y in range(0,4):
            for x in range(0,5):
                if block[0][y][x] == 3:
                    self.rotation_b = (0,(y, (x+5+3)))
                else:
                    self.map[y][x+3] = block[0][y][x]
        self.rotations = block
    
    def drop_block(self):
        """Tiputtaa palikkaa."""
        for y in range(19,-1,-1):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    if y == 19 or self.map[y+1][x] == 2:
                        self.freeze_block()
                        self.add_new_block()
                        return

        for y in range(19,-1,-1):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    self.map[y][x] = 0
                    self.map[y+1][x] = 1
        self.move_rotation_b("D")
    
    def move_block(self, direction):
        """Liikuttaa palikkaa joko oikealle tai vasemmalle.
        Args:
            direction: Siirron suunta, joko "R" tai "L".
        """
        if direction == "R":
            for y in range(0,20):
                if self.map[y][9] == 1:
                    return
            
            prev = 0
            for row in self.map:
                for x in row:
                    if prev == 1 and x == 2:
                        return
                    prev = x

            for y in range(0,20):
                for x in range(9,-1,-1):
                    if self.map[y][x] == 1:
                        self.map[y][x] = 0
                        self.map[y][x+1] = 1
            self.move_rotation_b("R")

        elif direction == "L":
            for y in range(0,20):
                if self.map[y][0] == 1:
                    return
            
            prev = 0
            for row in self.map:
                for x in row:
                    if prev == 2 and x == 1:
                        return
                    prev = x

            for y in range(0,20):
                for x in range(0,10):
                    if self.map[y][x] == 1:
                        self.map[y][x] = 0
                        self.map[y][x-1] = 1
            self.move_rotation_b("L")          

    def freeze_block(self):
        """Pysäyttää palikan paikoilleen."""
        for y in range(0,20):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    self.map[y][x] = 2
        
    
    def move_rotation_b(self, dir):
        """Liikuttaa kääntämiseen käytettävää palikkaa oikealle, vasemmalle tai alas. 
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


    def rotate_block(self):
        """Kääntää palikkaa."""
        block_y = self.rotation_b[1][0]
        block_x = self.rotation_b[1][1] -5
        move = False
        old = self.rotation_b
        if block_x < 0:
            block_x = 0
            self.rotation_b = (self.rotation_b[0], (self.rotation_b[1][0],0))
            move = True
            dir = "L"    
        if block_x > 5:
            block_x = 5
            self.rotation_b = (self.rotation_b[0], (self.rotation_b[1][0],10))
            move = True
            dir = "R"
        if block_y > 16:
            return
        if self.rotation_b[0]+1 < 4:
            r = self.rotation_b[0]+1
            self.rotation_b = ((self.rotation_b[0]+1), self.rotation_b[1])
        else:
            r = 0
            self.rotation_b = (0, self.rotation_b[1])


        next = self.rotations[r]
        y2 = -1
        x2 = -1

        for y in range(block_y,(block_y+4)):
            y2 = y2+1
            for x in range(block_x,(block_x+5)):
                x2 = x2+1
                if self.map[y][x] == 2 and next[y2][x2] == 1:
                    self.rotation_b = old
                    return
            x2 = -1
        
        for y in range(0,20):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    self.map[y][x] = 0
        
        y2 = -1
        x2 = -1

        for y in range(block_y,(block_y+4)):
            y2 = y2+1
            for x in range(block_x,(block_x+5)):
                x2 = x2+1
                if next[y2][x2] == 3:
                   continue 
                if self.map[y][x] == 2:
                    continue
                self.map[y][x] = next[y2][x2]
            x2 = -1
        
        if move:
            self.move_block(dir)