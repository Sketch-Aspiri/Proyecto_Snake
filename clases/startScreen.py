import pygame
import sys
from clases.utils import draw_text

def show_start_screen(screen, WIDTH, HEIGHT):
    waiting = True
    while waiting:
        screen.fill((0, 0, 0)) 
        draw_text(screen, "🐍 Carlitos la serpiente", (255, 255, 255), WIDTH, HEIGHT, y_offset=-40, size=48)
        draw_text(screen, "Presiona ESPACIO para comenzar", (200, 200, 200), WIDTH, HEIGHT, y_offset=20, size=28)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False