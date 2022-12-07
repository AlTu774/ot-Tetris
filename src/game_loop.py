import pygame
from stage import Stage

class GameLoop():
    def __init__(self, stage):
        self.stage = stage

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.stage.move_block("R")
                if event.key == pygame.K_LEFT:
                    self.stage.move_block("L")