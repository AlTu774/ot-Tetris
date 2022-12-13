import pygame

class Renderer():
    """Luokka, joka renderöi pelikentän.
    
    Args:
        stage = Pelikenttä
        stage.lenght = Pelikentän korkeus
        stage.widght = Pelikentän leveys
        block = palikan Surface alue
        display = Ruutu jolle kenttä piirretään
    """
    def __init__(self, stage, display):
        self.stage = stage
        self.stage_lenght = len(self.stage.map)
        self.stage_width = len(self.stage.map[0])
        self.block = pygame.Surface((30,30))
        self.display = display

    def render_stage(self):
        """Renderöi ruudelle pelikentän"""
        for y in range(0,self.stage_lenght):
            for x in range(0,self.stage_width):
                if self.stage.map[y][x] == 0:
                    pygame.draw.rect(self.display,(255,255,255),(190+x*30,50+y*30,30,30),1)
                elif self.stage.map[y][x] == 1:
                    pygame.draw.rect(self.display,(250,250,250),(190+x*30,50+y*30,30,30))
                elif self.stage.map[y][x] == 2:
                    pygame.draw.rect(self.display,(50,50,50),(190+x*30,50+y*30,30,30))
                    
        pygame.display.update()           

