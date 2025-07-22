import pygame
import sys

# Inicializar pygame
pygame.init()

# Tamaño de pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi primer juego con Pygame")

# Colores
NEGRO = (0, 0, 0)

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica del juego aquí

    # Dibujar
    screen.fill(NEGRO)
    
    # Actualizar pantalla
    pygame.display.flip()

    # FPS
    clock.tick(60)

# Salir
pygame.quit()
sys.exit()
