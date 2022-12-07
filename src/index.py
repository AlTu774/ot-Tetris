import pygame
from stage import Stage
from clock import Clock
from renderer import Renderer
from game_loop import GameLoop

def main():
    display = pygame.display.set_mode((900,700))

    pygame.init()

    stage = Stage()
    running = True
    clock = Clock()
    clock.g_clock.tick(60)
    renderer = Renderer(stage, display)
    stage.add_new_block()
    start_time = 0
    game_loop = GameLoop(stage)

    while running:
        game_loop.events()    
        
        if (clock.get_ticks() - start_time) > 600:
            stage.drop_block()
            start_time = clock.get_ticks()
        
        display.fill((0,0,0))
        renderer.render_stage()
        
    pygame.quit()

if __name__ == "__main__":
    main()