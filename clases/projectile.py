import pygame

class Projectile:
    def __init__(self, x, y, direction, speed=5, size=10, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.direction = direction 
        self.speed = speed
        self.size = size
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def update(self):
        # Mueve el proyectil en su dirección
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def off_screen(self, width, height):
        return (
            self.x < 0 or self.x > width or
            self.y < 0 or self.y > height
        )

    def collides_with(self, target_rect):
        return self.rect.colliderect(target_rect)