import pygame
import random

CELL_SIZE = 20
RED = (255, 0, 0)

class Enemy:
    def __init__(self, cols, rows, speed_delay):
        self.body = [[random.randint(0, cols - 1), random.randint(0, rows - 1)]]
        self.cols = cols
        self.rows = rows
        self.direction = [0, 0] 
        self.tick_counter = 0
        self.tick_delay = speed_delay

    def update(self, target_pos):
        self.tick_counter += 1
        if self.tick_counter < self.tick_delay:
            return  
        self.tick_counter = 0  
        
        head = self.body[-1]
        dx = target_pos[0] - head[0]
        dy = target_pos[1] - head[1]

        if abs(dx) > abs(dy):
            self.direction = [1 if dx > 0 else -1, 0]
        else:
            self.direction = [0, 1 if dy > 0 else -1]

        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]
        self.body.append(new_head)
        if len(self.body) > 3:
            self.body.pop(0)

    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, RED, (part[0]*CELL_SIZE, part[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def collide_with(self, snake_body):
        return any(part in snake_body for part in self.body)