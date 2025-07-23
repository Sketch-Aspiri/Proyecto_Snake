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
        
def draw_score(screen, text, color, x, y, size=24):
    font = pygame.font.SysFont(None, size)
    message = font.render(text, True, color)
    screen.blit(message, (x, y))
    
def pause_game(screen, width, height):
    paused = True

    # Dibujar pantalla de pausa
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 48)
    message1 = font.render("Juego en pausa", True, (255, 255, 0))
    rect1 = message1.get_rect(center=(width // 2, height // 2 - 20))
    screen.blit(message1, rect1)

    message2 = font.render("Presiona ESPACIO para continuar", True, (255, 255, 0))
    rect2 = message2.get_rect(center=(width // 2, height // 2 + 20))
    screen.blit(message2, rect2)

    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    
def show_game_over_screen(screen, width, height):
    import pygame
    from clases.utils import draw_text

    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        draw_text(screen, "Game Over", (255, 0, 0), width, height, -40, size=50)
        draw_text(screen, "Presiona ESPACIO para volver al menú", (255, 255, 0), width, height, 20, size=30)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


