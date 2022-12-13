import pygame

class GameLoop():
    """Luokka, joka lukee pelaajan syötteen ja joko tekee muutoksia pelikenttään tai lopetetaan peli.
    
    Attributes:
    stage: Luokka saa pelikentän johon muutokset tehdään."""
    def __init__(self, stage):
        self.stage = stage

    def events(self):
        """Käy läpi pelaajaan syötteen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.stage.move_block("R")
                if event.key == pygame.K_LEFT:
                    self.stage.move_block("L")
                if event.key == pygame.K_UP:
                    self.stage.rotate_block()
                