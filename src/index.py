import pygame
from stage import Stage
from clock import Clock
from renderer import Renderer

def main():
    display = pygame.display.set_mode((500,700))

    pygame.init()

    stage = Stage()
    running = True
    clock = Clock()
    clock.g_clock.tick(60)
    renderer = Renderer(stage, display)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        renderer.render_stage()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()