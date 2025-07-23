import pygame
import sys
from clases.snake import Snake
from clases.food import Food
from clases.utils import draw_text

# Inicializar pygame
pygame.init()

# Configuración
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carlitos la serpiente - Nivel 1")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

def main():
    snake = Snake(COLS, ROWS)
    food = Food(COLS, ROWS)
    running = True
    foods_eaten = 0
    total_food = 10
    game_over = False
    level_complete = False

    while running:
        clock.tick(10)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
            draw_text(screen, "¡Felicidades!", WHITE, WIDTH, HEIGHT, -20)
            draw_text(screen, "Pasaste el Nivel 1", WHITE, WIDTH, HEIGHT, 20)

        pygame.display.update()

        if game_over or level_complete:
            pygame.time.delay(3000)
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
