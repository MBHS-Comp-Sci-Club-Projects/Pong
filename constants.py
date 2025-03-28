from enum import Enum

WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
WHITE = (255, 255, 255)
FPS = 60

class Dir(Enum):
    Up = True
    Down = False

class Player(Enum):
    First = True
    Second = False

class Vec:
    x: int
    y: int

    def __init__(self, x : int = 0, y: int = 0):
        self.x = x
        self.y = y

def negate(x):
    return x * -1;
