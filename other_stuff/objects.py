from .constants import WIDTH, HEIGHT, GREEN
from .player import Player
import random
import pygame

player = Player()


class Pipe:
    def __init__(self):
        self.top_array = []
        self.bot_array = []
        self.new_pipe()

        # Temporary variables for check_hit()
        self.pipeX1 = 0
        self.pipeX2 = 0
        self.pipeY1 = 0
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        self.top_pipe = pygame.image.load('other_stuff/pipe_top.png').convert_alpha()
        self.bot_pipe = pygame.image.load('other_stuff/pipe_bot.png').convert_alpha()

    def new_pipe(self):
        self.x1 = WIDTH
        self.y1 = 0
        self.x2 = 80
        self.y2 = random.randint(0, 350)

        self.bottomY2 = self.y2 + 200

        self.hitbox_top = [self.x1, self.y1, self.x2, self.y2]
        self.hitbox_bot = [self.x1, self.bottomY2, self.x2, 400]

        self.top_array.append(self.hitbox_top)
        self.bot_array.append(self.hitbox_bot)

    def update_pipe(self):
        for j in range(len(self.top_array)-1):
            self.top_array[j][0] -= 5
            self.bot_array[j][0] -= 5

        if self.top_array[0][0] <= -80:
            del self.top_array[0]
            del self.bot_array[0]

    def draw_pipe(self, win):
        for t in self.top_array:
            #pygame.draw.rect(win, GREEN, t)
            self.gameDisplay.blit(self.top_pipe, (t[0], t[3] - 350))

        for b in self.bot_array:
            #pygame.draw.rect(win, GREEN, b)
            self.gameDisplay.blit(self.bot_pipe, (b[0], b[1]))
