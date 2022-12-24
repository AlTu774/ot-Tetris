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
        self.block = Blocks()
    
    def add_new_block(self):
        """Lisää uuden palikan kenttään."""
        block = self.block.generate_random_block()
        for y in range(0,4):
            for x in range(0,5):
                if block[0][y][x] == 3:
                    self.block.rotation_b = (0,(y, (x+5+3)))
                else:
                    self.map[y][x+3] = block[0][y][x]
        self.block.rotations = block
    
    def switch_block(self):
        if self.block.spare == []:
            self.block.spare = self.block.rotations
            self.clear_stage(self.map)
            self.add_new_block()

        else:
            old_block = self.block.rotations
            new_block = self.block.spare
            rotationb = self.block.rotation_b
            if self.block.rotation_b[1][1] > 10:
                rotationb = (self.block.rotation_b[0], (self.block.rotation_b[1][0],10))
            if self.block.rotation_b[1][0] > 16:
                return
            error = self.error_check(rotationb[1],new_block[0])
            if error:
                return
            
            self.block.spare = old_block
            self.block.rotations = new_block
            self.block.rotation_b = rotationb
            self.clear_stage(self.map)
            self.insert_block(self.block.rotation_b[1],self.block.rotations[0])
            if rotationb[1][1] == 10:
                self.move_block("R")


    
    def insert_block(self,rotation_b,block):
        move = False
        y2 = -1
        x2 = -1
        yb = rotation_b[0]
        xb = rotation_b[1]-5
        if xb < 0:
            xb = 0
            move = True
        for y in range(yb,(yb+4)):
            y2 += 1
            for x in range(xb,xb+5):
                x2 += 1
                if self.map[y][x] == 2:
                    continue
                if block[y2][x2] == 3:
                    continue
                self.map[y][x] = block[y2][x2]
            x2 = -1
            
        if move:
            self.move_block("L")

            
    
    def drop_block(self):
        """Tiputtaa palikkaa."""
        for y in range(19,-1,-1):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    if y == 19 or self.map[y+1][x] == 2:
                        score = self.freeze_block()
                        self.add_new_block()
                        return score

        for y in range(19,-1,-1):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    self.map[y][x] = 0
                    self.map[y+1][x] = 1
        self.block.move_rotation_b("D")
    
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
            self.block.move_rotation_b("R")

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
            self.block.move_rotation_b("L")          

    def freeze_block(self):
        """Pysäyttää palikan paikoilleen."""
        for y in range(0,20):
            for x in range(0,10):
                if self.map[y][x] == 1:
                    self.map[y][x] = 2
        return self.check_rows()
    
    def check_rows(self):
        score = 1
        for y in range(19,0,-1):
            while self.map[y] == [2,2,2,2,2,2,2,2,2,2]:
                score += 10
                for y2 in range(y,1,-1):
                    prev = self.map[y2-1][:]
                    self.map[y2] = prev
        return score
    
    def clear_stage(self,map1):
        for y in range(0,20):
            for x in range(0,10):
                if map1[y][x] == 1:
                    map1[y][x] = 0
        return
        
    def rotate_block(self):
        """Kääntää palikkaa."""
        block_y = self.block.rotation_b[1][0]
        block_x = self.block.rotation_b[1][1] -5
        move = False
        old = self.block.rotation_b
        if block_x < 0:
            block_x = 0
            self.block.rotation_b = (self.block.rotation_b[0], (self.block.rotation_b[1][0],0))
            move = True
            dir = "L"    
        if block_x > 5:
            block_x = 5
            self.block.rotation_b = (self.block.rotation_b[0], (self.block.rotation_b[1][0],10))
            move = True
            dir = "R"
        if block_y > 16:
            self.block.rotation_b = old
            return
        if self.block.rotation_b[0]+1 < 4:
            r = self.block.rotation_b[0]+1
            self.block.rotation_b = ((self.block.rotation_b[0]+1), self.block.rotation_b[1])
        else:
            r = 0
            self.block.rotation_b = (0, self.block.rotation_b[1])


        next = self.block.rotations[r]
        error = self.error_check(self.block.rotation_b[1],next)
        if error:
            self.block.rotation_b = old
            return
        
        self.clear_stage(self.map)
        self.insert_block(self.block.rotation_b[1], next)

        if move:
            self.move_block(dir)

    def error_check(self,rotation_b,block):
        check_map = []
        over = 0
        for row in self.map:
            check_map.append(row[:])
        self.clear_stage(check_map)

        y2 = -1
        x2 = -1
        if rotation_b[1] == 0:
            rotation_b = (rotation_b[0], 5)
        if rotation_b[1]-5 < 0:
            over = -(rotation_b[1] - 5)
        for y in range(0,4):
            for x in range(0,over):
                if block[y][x] == 1:
                    return True

        for y in range(rotation_b[0],(rotation_b[0]+4)):
            y2 = y2+1
            for x in range(rotation_b[1]-5+over,(rotation_b[1])):
                x2 = x2+1
                if check_map[y][x] == 2 and block[y2][x2] == 1:
                    return True
            x2 = -1
        return False
        
