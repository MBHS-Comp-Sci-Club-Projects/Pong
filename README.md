# Pong Game

This is a simple implementation of the classic **Pong** game using **Python** and **Pygame**. The game includes basic features such as player movement, paddle collision, ball physics, and scoring.

## Table of Contents

- [Introduction](#introduction)
- [Gameplay](#gameplay)
- [Setup](#setup)
- [Features](#features)
- [Controls](#controls)
- [License](#license)

## Introduction

Pong is one of the first video games ever created. In this implementation, players control paddles and try to bounce a ball past the opponent's paddle to score points.

## Gameplay

The game consists of two paddles and a ball. The ball moves across the screen, bouncing off the walls and paddles. Players score a point each time the ball passes the opponent’s paddle.

- **Player 1** controls the left paddle.
- **Player 2** controls the right paddle.

The game continues until either player reaches a winning score.

## Setup

To play the game, you need **Python** and the **Pygame** library installed.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pong-game.git
    cd pong-game
    ```

2. Install the required dependencies:

    ```bash
    pip install pygame
    ```

3. Run the game:

    ```bash
    python pong_game.py
    ```

## Features

- **Real-time paddle and ball movement** with smooth animations.
- **Collision detection** for ball and paddles.
- **Scoring system** that increments when the ball passes a player's paddle.
- **Sound effects** when the ball bounces off walls or paddles (optional).

## Controls

- **Player 1 (Left Paddle):**
  - Move Up: `W` key
  - Move Down: `S` key

- **Player 2 (Right Paddle):**
  - Move Up: `Up Arrow` key
  - Move Down: `Down Arrow` key

## License

This project is licensed under the MIT License. Open source and free for everyone to use, modify, etc.