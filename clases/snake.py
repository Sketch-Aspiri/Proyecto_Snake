import pygame

CELL_SIZE = 20
GREEN = (0, 200, 0)

class Snake:
    def __init__(self):
        self.body = [[5, 5]]
        self.direction = [1, 0]

    def move(self):
        head = self.body[-1][:]
        head[0] += self.direction[0]
        head[1] += self.direction[1]
        self.body.append(head)
        self.body.pop(0)

    def grow(self):
        self.body.insert(0, self.body[0])

    def change_direction(self, dir):
        if (dir[0] * -1, dir[1] * -1) != tuple(self.direction):
            self.direction = dir

    def collide(self):
        head = self.body[-1]
        return (
            head in self.body[:-1] or
            head[0] < 0 or head[0] >= COLS or
            head[1] < 0 or head[1] >= ROWS
        )

    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, (0, 200, 0), (part[0]*20, part[1]*20, 20, 20))