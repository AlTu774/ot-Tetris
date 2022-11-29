import pygame

class Clock():
    def __init__(self):
        self.g_clock = pygame.time.Clock()

    def tick(self, fps):
        self.g_clock.tick(fps)
    
    def get_ticks(self):
        return pygame.time.get_ticks()