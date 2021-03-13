from .constants import START_HEIGHT, WIDTH, HEIGHT, WHITE
import pygame


class Player:
    def __init__(self):
        self.jumping = False
        self.jump_count = 10
        self.x1 = 100
        self.x2 = 80
        self.y2 = 50
        self.neg = 1
        self.velocity = 1
        self.player_height = START_HEIGHT
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hitbox = [self.x1, self.player_height, self.x2, self.y2]
        self.allow_velocity = False
        self.allow_jumping = True
        self.idle_bird = pygame.image.load("other_stuff/idle_bird.png").convert_alpha()

    def jump(self):
        self.velocity = 1
        self.player_height -= ((self.jump_count ** 2) * 0.04)
        self.hitbox[1] = self.player_height

        if self.jump_count == 0:
            self.jumping = False
            self.jump_count = 20
            self.allow_velocity = True

        self.hitbox[1] = self.player_height
        self.jump_count -= 1

    def apply_velocity(self):
        if self.allow_velocity:
            self.player_height += (self.velocity ** 2) / 2
            self.velocity += 0.2
            if self.velocity >= 2.5:
                self.allow_jumping = True
        self.hitbox[1] = self.player_height

    def draw_player(self, win):
        #pygame.draw.rect(win, WHITE, self.hitbox)
        self.gameDisplay.blit(self.idle_bird, (self.hitbox[0], self.hitbox[1]))