import pygame
from clases.projectile import Projectile

class Turret:
    def __init__(self, x, y, shoot_interval=60):
        self.x = x
        self.y = y
        self.size = 20
        self.color = (0, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.projectiles = []
        self.shoot_interval = shoot_interval
        self.shoot_timer = 0

    def update(self):
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.shoot()
            self.shoot_timer = 0

        for projectile in self.projectiles:
            projectile.update()

        # Eliminar los proyectiles fuera de pantalla
        self.projectiles = [
            p for p in self.projectiles if not p.off_screen(600, 400)
        ]

    def shoot(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # derecha, izquierda, abajo, arriba
        for dir in directions:
            p = Projectile(self.x + self.size // 2, self.y + self.size // 2, dir)
            self.projectiles.append(p)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        for p in self.projectiles:
            p.draw(screen)

    def check_collision(self, snake_head_rect):
        for p in self.projectiles:
            if p.collides_with(snake_head_rect):
                return True
        return False
