from other_stuff.constants import WIDTH, HEIGHT, BLACK
from other_stuff.player import Player
from other_stuff.objects import Pipe
import pygame
import time

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()

player = Player()
pipe = Pipe()


def reset():
    global pipe_count, score_count, score
    player.__init__()
    pipe.__init__()
    pipe_count = 0
    score_count = 0
    score = "Score: 0"


def main():
    global pipe_count, score_count, score
    run = True
    clock = pygame.time.Clock()
    reset()

    myFont = pygame.font.SysFont("Comic Sans MS", 20)
    myFont2 = pygame.font.SysFont("Comic Sans MS", 50)

    background = pygame.image.load("other_stuff/background.png")

    while run:
        WIN.blit(background, (0,0))
        key = pygame.key.get_pressed()
        clock.tick(FPS)
        pipe_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if player.jumping:
            player.jump()

        elif not player.jumping:
            if player.allow_jumping:
                if key[pygame.K_w]:
                    player.jumping = True
                    player.allow_velocity = False
                    player.allow_jumping = False
                    player.jump()

        if pipe_count == 85:
            pipe.new_pipe()
            pipe_count = 0
            score_count += 1
            if score_count - 2 <= 0:
                score = "Score: 0"
            else:
                score = "Score: " + str(score_count - 2)

        player.apply_velocity()
        player.draw_player(WIN)
        pipe.update_pipe()
        pipe.draw_pipe(WIN)

        def death_screen():
            WIN.fill(BLACK)
            textSurface2 = myFont2.render("YOU DIED!", True, (255, 255, 255))
            WIN.blit(textSurface2, (WIDTH/2-130, HEIGHT/2-50))
            pygame.display.update()
            time.sleep(2)
            reset()

        def check_hit():
            global score_count, score
            for t in pipe.top_array:
                pipe.pipeX1t = t[0]
                pipe.pipeX2t = t[0] + t[2]
                pipe.pipeY1t = t[3]
                if pipe.pipeX1t <= player.x1 + player.x2 <= pipe.pipeX2t and player.player_height <= pipe.pipeY1t:
                    death_screen()

                if pipe.pipeX1t <= player.x1 <= pipe.pipeX2t and player.player_height <= pipe.pipeY1t:
                    death_screen()

            for b in pipe.bot_array:
                pipe.pipeX1b = b[0]
                pipe.pipeX2b = b[0] + b[2]
                pipe.pipeY1b = b[1]
                if pipe.pipeX1b <= player.x1 + player.x2 <= pipe.pipeX2b and player.player_height + player.y2 >= pipe.pipeY1b:
                    death_screen()

                if pipe.pipeX1b <= player.x1 <= pipe.pipeX2b and player.player_height + player.y2 >= pipe.pipeY1b:
                    death_screen()

            if player.player_height >= HEIGHT:
                death_screen()

        textSurface = myFont.render(score, True, (0, 0, 0))
        WIN.blit(textSurface, (5, 5))
        check_hit()

        pygame.display.update()
    pygame.quit()


main()
