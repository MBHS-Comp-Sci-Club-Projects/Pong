import pygame
from constants import *


class Ball:

    def __init__(self):
        self.pos = Vec()
        self.speed = Vec()

        self.pos.x = WIDTH // 2
        self.pos.y = HEIGHT // 2
        self.speed.x = 5
        self.speed.y= 5


    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.pos.x, self.pos.y), BALL_RADIUS)

    def move(self):
        self.pos.y += self.speed.y
        self.pos.x += self.speed.x

    def simulate_physics(self, playerPos1 : Vec, playerPos2 : Vec):

        # Ball collision with top and bottom
        if self.pos.y - BALL_RADIUS <= 0 or self.pos.y + BALL_RADIUS >= HEIGHT:
            self.speed.y = -self.speed.y

        # Ball collision with paddles
        if (self.pos.x - BALL_RADIUS <= PADDLE_WIDTH and
                playerPos1.y < self.pos.y < playerPos1.y + PADDLE_HEIGHT):
            # Collision with the first player's paddle
            self.speed.x = -self.speed.x

        elif (self.pos.x + BALL_RADIUS >= WIDTH - PADDLE_WIDTH and
              playerPos2.y < self.pos.y < playerPos2.y + PADDLE_HEIGHT):
            # Collision with the second player's paddle
            self.speed.x = -self.speed.x


    def reset_ball(self):
        self.pos.x = WIDTH // 2
        self.pos.y = HEIGHT // 2
        self.speed.x = -self.speed.x
        if self.speed.y > 0:
            self.speed.y = 5
        else:
            self.speed.y = -5