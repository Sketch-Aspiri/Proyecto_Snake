import pygame
import sys
from clases.snake import Snake
from clases.food import Food
from clases.startScreen import show_start_screen
from clases.utils import draw_text, draw_score, pause_game


# Inicializar pygame
pygame.init()

# Configuración
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carlitos la serpiente")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

def main(level_data):
    pygame.display.set_caption(f"Carlitos la serpiente - {level_data['nombre']}")
    snake = Snake(COLS, ROWS)
    food = Food(COLS, ROWS)
    running = True
    foods_eaten = 0
    total_food = level_data["total_food"]
    speed = level_data["speed"]
    message = level_data["mensaje"]
    game_over = False
    level_complete = False

    paused = False
    while running:
        clock.tick(speed)  
        screen.fill(BLACK)
        draw_score(screen, f"🍎 {foods_eaten}/{total_food}", WHITE, 10, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not paused:
                        paused = True
                        pause_game(screen, WIDTH, HEIGHT)
                        paused = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.change_direction([0, -1])
        elif keys[pygame.K_DOWN]:
            snake.change_direction([0, 1])
        elif keys[pygame.K_LEFT]:
            snake.change_direction([-1, 0])
        elif keys[pygame.K_RIGHT]:
            snake.change_direction([1, 0])

        if not game_over and not level_complete:
            # Calcular nueva cabeza
            new_head = snake.body[-1][:]
            new_head[0] += snake.direction[0]
            new_head[1] += snake.direction[1]

            # Verificar colisión antes de mover
            if (
                new_head in snake.body or
                new_head[0] < 0 or new_head[0] >= COLS or
                new_head[1] < 0 or new_head[1] >= ROWS
            ):
                game_over = True
            else:
                # Verificar si comerá
                if new_head == food.position:
                    snake.body.append(new_head)  # crece sin eliminar cola
                    food.respawn(snake.body)
                    foods_eaten += 1
                else:
                    # Movimiento normal
                    snake.body.append(new_head)
                    snake.body.pop(0)

                if foods_eaten >= total_food:
                    level_complete = True



        snake.draw(screen)
        food.draw(screen)

        if game_over:
            draw_text(screen, "Game Over", RED, WIDTH, HEIGHT)
        elif level_complete:
            draw_text(screen, message, WHITE, WIDTH, HEIGHT, y_offset=-20)
            pygame.display.update()
            from clases.utils import wait_for_next_level
            wait_for_next_level(screen, WIDTH, HEIGHT)

        pygame.display.update()

        if game_over:
            pygame.time.delay(3000)
            running = False
        elif level_complete:
            pygame.time.delay(1000)
            wait_for_next_level(screen, WIDTH, HEIGHT)
            running = False

    return "next" if level_complete else "game_over"

if __name__ == "__main__":
    show_start_screen(screen, WIDTH, HEIGHT)
    from clases.leves import levels
    
    for nivel in levels:
        resultado = main(nivel)
        if resultado != "next":
            break
