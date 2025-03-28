import pygame

from paddle import Paddle
from ball import Ball
from constants import *

# Initialize pygame
pygame.init()


def draw_score(font, screen, score1 : int, score2 : int):
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

def main():
    player1 = Paddle(Player.First)
    player2 = Paddle(Player.Second)
    ball = Ball()

    # Fonts
    font = pygame.font.SysFont("Arial", 30)

    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    # Game Clock
    clock = pygame.time.Clock()

    running = True

    # Game Loop
    while running:
        screen.fill((0, 0, 0))  # Clear screen

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle Paddle Movement for
        # key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] == True:
            player1.move(Dir.Up)
        elif keys[pygame.K_s] == True:
            player1.move(Dir.Down)

        if keys[pygame.K_UP] == True:
            player2.move(Dir.Up)
        elif keys[pygame.K_DOWN] == True:
            player2.move(Dir.Down)

        # Handle Ball Movement and Physics
        ball.move()

        ball.simulate_physics(player1.pos, player2.pos)

        # Draw paddles, ball, and score
        player1.draw(screen) # Player 1 paddle
        player2.draw(screen)  # Player 2 paddle

        ball.draw(screen)  # Ball

        draw_score(font, screen, player1.score, player2.score)  # Score display

        # Update the display
        pygame.display.flip()

        # Maintain frame rate
        clock.tick(FPS)

        # Ball out of bounds
        if ball.pos.x - BALL_RADIUS <= 0:
            player2.add_point()
            ball.reset_ball()
        elif ball.pos.x + BALL_RADIUS >= WIDTH:
            player1.add_point()
            ball.reset_ball()

    pygame.quit()


if __name__ == "__main__":
    main()
