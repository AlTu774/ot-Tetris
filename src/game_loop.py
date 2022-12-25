import pygame

class GameLoop():
    """Luokka, joka lukee pelaajan syötteen ja joko tekee muutoksia pelikenttään tai lopetetaan peli.
    
    Attributes:
    stage: Luokka saa pelikentän johon muutokset tehdään."""
    def __init__(self, stage):
        self.stage = stage
        self.drop = False

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
                if event.key == pygame.K_DOWN:
                    self.drop = True
                if event.key == pygame.K_x:
                    self.stage.switch_block()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.drop = False
    
    def game_over(self):
        """Game over -näytössä tehtävät valinnat."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    return "no"
                if event.key == pygame.K_UP:
                    return "yes"
                if event.key == pygame.K_RETURN:
                    return True