import pygame

def draw_text(screen, text, color, width, height, y_offset=0, size=36):
    font = pygame.font.SysFont(None, size)
    message = font.render(text, True, color)
    rect = message.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(message, rect)