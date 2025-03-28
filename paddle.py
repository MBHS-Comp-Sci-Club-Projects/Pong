from constants import *
import pygame


class Paddle:

    def __init__(self, which_player : Player):
        self.pos = Vec()

        if which_player == Player.First:
            self.pos.x = 0
        elif which_player == Player.Second:
            self.pos.x = WIDTH - PADDLE_WIDTH

        self.pos.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.y_speed = 10
        self.score = 0

    def move(self, up_or_down : Dir):
        if up_or_down == Dir.Up and self.pos.y > 0:
                self.pos.y -= self.y_speed
        elif up_or_down == Dir.Down and self.pos.y + PADDLE_HEIGHT < HEIGHT:
                self.pos.y += self.y_speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.pos.x, self.pos.y, PADDLE_WIDTH, PADDLE_HEIGHT))

    def add_point(self):
        self.score += 1



