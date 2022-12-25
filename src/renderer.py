import pygame
import os

dirname = os.path.dirname(__file__)

class Renderer():
    """Luokka, joka renderöi pelikentän.
    
    Args:
        stage: Pelikenttä.
        stage.lenght: Pelikentän korkeus.
        stage.widght: Pelikentän leveys.
        display: Ruutu jolle kenttä piirretään.
        block1: Palikan väri.
        block2: Vara-palikan väri.
        font: Pelissä käytettävä teksti fontti.
        block3: Jäätyneiden palikoiden väri.
    """
    def __init__(self, stage, display):
        self.stage = stage
        self.stage_lenght = len(self.stage.map)
        self.stage_width = len(self.stage.map[0])
        self.display = display
        self.block1 = None
        self.block2 = None
        self.font = pygame.font.SysFont("arial", 30)
        self.block3 = pygame.image.load(os.path.join(dirname, "assets", "gray.jpg"))
    
    def render_game(self):
        """Renderöi kerralla kentän ja vara-palikan."""
        self.render_stage()
        self.render_spare()
        pygame.display.update()

    def block_color(self):
        """Selvittää palikoiden värit."""
        color1 = self.stage.color1
        color1 = color1 + ".jpg"
        self.block1 = pygame.image.load(os.path.join(dirname, "assets", color1))

        if self.stage.color2 != None:
            color2 = self.stage.color2
            color2 = color2 + ".jpg"
            self.block2 = pygame.image.load(os.path.join(dirname, "assets", color2))

    def render_stage(self):
        """Renderöi pelikentän."""
        self.block_color()
        pygame.draw.rect(self.display,(211,211,211),(188,48,(30*10+4),(30*20+4)),2)
        for y in range(0,self.stage_lenght):
            for x in range(0,self.stage_width):
                if self.stage.map[y][x] == 0:
                    pygame.draw.rect(self.display,(55,55,55),(190+x*30,50+y*30,30,30),1)
                elif self.stage.map[y][x] == 1:
                    self.display.blit(self.block1, (190+x*30,50+y*30))
                elif self.stage.map[y][x] == 2:
                    self.display.blit(self.block3, (190+x*30,50+y*30))
    
    def render_spare(self):
        """Renderöi vara-palikan ruudulle."""
        hold = self.font.render("Hold (x)", True, (255,255,255))
        self.display.blit(hold, (555,20))
        spare = self.stage.block.spare
        pygame.draw.rect(self.display,(211,211,211),(550,60,(30*5),(30*5)),2)
        if spare == []:
            return
        spare = self.stage.block.spare[0]
        for y in range(0,4):
            for x in range(0,5):
                if spare[y][x] == 1:
                    self.display.blit(self.block2, (560+30*x,75+30*y))
    
    def render_info(self, score, max_score, level):
        """Renderöi tekstinä tietoa ruudulle pelistä.
        Args:
            score: Tämän hetkisen pelin pisteet.
            max_score: Peli kertojen suurin pistemäärä.
            level: Pelin nopeus taso.
            """
        note1 = self.font.render(("Score: "+str(score)), True, (255,255,255))
        note2 = self.font.render(("Best score: "+str(max_score)), True, (255,255,255))
        note3 = self.font.render(("Level: "+str(level)), True, (255,255,255))
        self.display.blit(note1, (555,400))
        self.display.blit(note2, (555,450))
        self.display.blit(note3, (555,300))
    
    def game_over(self, option):
        """Pelin päätettyä näytettävien vaihtoehtojen renderöinti.
        Args:
            option: Tämän hetkinen vaitoehto, yes tai no.
            """
        pygame.draw.rect(self.display,(0,0,0),(400,400,600,600))
        if option == "yes":
            color1 = ((255,255,255))
            color2 = ((150,150,150))
        elif option == "no":
            color1 = ((150,150,150))
            color2 = ((255,255,255))
        note1 = self.font.render(("Retry?"), True, (255,255,255))
        note2 = self.font.render(("Yes"), True, (color1))
        note3 = self.font.render(("No"), True, (color2))
        self.display.blit(note1, (450,400))
        self.display.blit(note2, (450,450))
        self.display.blit(note3, (450,500))
        pygame.display.update()
    
        
        




        
