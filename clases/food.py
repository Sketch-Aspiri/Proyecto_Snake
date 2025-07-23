import pygame
import random

CELL_SIZE = 20
RED = (200, 0, 0)

class Food:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.position = [random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def respawn(self, snake_body):
        while True:
            self.position = [random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)]
            if self.position not in snake_body:
                break