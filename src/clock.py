import pygame

class Clock():
    """Luokka, joka toimii pelin kellona."""
    def __init__(self):
        self.g_clock = pygame.time.Clock()

    def tick(self, fps):
        """Asettaa pelin framerate:n, eli kuinka monta kertaa pelisilmukka suoritetaan sekunissa.
        
        Args:
            fps: frames per second, suorituksien määrä sekunnissa.
        """
        self.g_clock.tick(fps)
    
    def get_ticks(self):
        """Selvittää sen hetkisen ajan.
        
        Returns:
            pygame.time.get_ticks(): ajan sekunneissa.
        """
        return pygame.time.get_ticks()
    
    def adjust_speed(self, speed):
        if (self.get_ticks() - start_time) > speed:
            stage.drop_block()
            start_time = self.get_ticks()