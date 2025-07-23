import pygame
import sys

def draw_text(screen, text, color, width, height, y_offset=0, size=36):
    font = pygame.font.SysFont(None, size)
    message = font.render(text, True, color)
    rect = message.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(message, rect)
    
def wait_for_next_level(screen, width, height):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

        draw_text(screen, "Presiona ESPACIO para continuar", (180, 180, 180), width, height, y_offset=40, size=24)
        pygame.display.update()