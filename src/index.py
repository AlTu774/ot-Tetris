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
    speeds = [100, 600, 500, 450, 400, 350, 300, 250, 200, 150, 100]
    speed_level = (1,0)
    score = 0
    max_score = 0
    pygame.display.set_caption("Tetris")

    while running:

        game_loop.events()

        if game_loop.drop == True:
            speed = speeds[0]
        if game_loop.drop == False:
            speed = speeds[speed_level[0]]

        if (clock.get_ticks() - start_time) > speed:
            new_score = stage.drop_block()
            if new_score != None:
                score += new_score
            
            if (score - speed_level[1] > 100):
                if speed_level[0] < 10:
                    old = speed_level
                    speed_level = (old[0]+1,old[1]+100)

            start_time = clock.get_ticks()
        
        display.fill((0,0,0))
        renderer.render_info(score, max_score, speed_level[0])
        renderer.render_game()

        if stage.game_over:
            enterkey = False
            option = "yes"
            if score > max_score:
                max_score = score
            while True:
                renderer.game_over(option)
                input = game_loop.game_over()
                if input == "yes":
                    option = "yes"
                elif input == "no":
                    option = "no"
                elif input == True:
                    enterkey = True
                if option == "yes" and enterkey == True:
                    stage.game_over = False
                    break
                if option == "no" and enterkey == True:
                    running = False
                    break
            speed_level = (1,0)
            score = 0
            stage.retry()


    pygame.quit()

if __name__ == "__main__":
    main()