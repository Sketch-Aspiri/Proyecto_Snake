import pygame
import sys
from clases.snake import Snake
from clases.food import Food
from clases.startScreen import show_start_screen
from clases.utils import draw_text, draw_score, pause_game, wait_for_next_level, show_game_over_screen
from clases.enemy import Enemy

# Inicializar pygame
pygame.init()

# Configuración
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

def handle_movement(snake, keys):
    if keys[pygame.K_UP]:
        snake.change_direction([0, -1])
    elif keys[pygame.K_DOWN]:
        snake.change_direction([0, 1])
    elif keys[pygame.K_LEFT]:
        snake.change_direction([-1, 0])
    elif keys[pygame.K_RIGHT]:
        snake.change_direction([1, 0])
        
def update_snake(snake, food, foods_eaten, cols, rows):
    new_head = snake.body[-1][:]
    new_head[0] += snake.direction[0]
    new_head[1] += snake.direction[1]

    if new_head in snake.body or new_head[0] < 0 or new_head[0] >= cols or new_head[1] < 0 or new_head[1] >= rows:
        return False, foods_eaten  # Game over
    else:
        if new_head == food.position:
            snake.body.append(new_head)
            food.respawn(snake.body)
            foods_eaten += 1
        else:
            snake.body.append(new_head)
            snake.body.pop(0)
        return True, foods_eaten
    
def handle_enemy(enemy, snake, active, enemy_data, foods_eaten):
    if enemy_data.get("active") and not active and foods_eaten >= enemy_data.get("appear_at", 0):
        active = True

    if active:
        enemy.update(snake.body[-1])
        if enemy.collide_with([snake.body[-1]]):
            return active, True  # Game over
    return active, False

def main(level_data):
    pygame.display.set_caption(f"Carlitos la serpiente - {level_data['nombre']}")
    snake = Snake(COLS, ROWS)
    food = Food(COLS, ROWS)
    enemy_data = level_data.get("enemy", {})
    enemy = Enemy(COLS, ROWS, speed_delay=enemy_data.get("speed_delay", 0))
    enemy_active = False
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

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not paused:
                    paused = True
                    pause_game(screen, WIDTH, HEIGHT)
                    paused = False

        # Movimiento
        keys = pygame.key.get_pressed()
        handle_movement(snake, keys)

        # Lógica de juego
        if not game_over and not level_complete:
            alive, foods_eaten = update_snake(snake, food, foods_eaten, COLS, ROWS)
            if not alive:
                game_over = True
            else:
                if foods_eaten >= total_food:
                    level_complete = True

                enemy_active, enemy_hit = handle_enemy(enemy, snake, enemy_active, enemy_data, foods_eaten)
                if enemy_hit:
                    game_over = True

        # Dibujar
        snake.draw(screen)
        food.draw(screen)
        if enemy_active:
            enemy.draw(screen)

        if level_complete:
            draw_text(screen, message, WHITE, WIDTH, HEIGHT, y_offset=-20)

        pygame.display.update()

        if game_over:
            show_game_over_screen(screen, WIDTH, HEIGHT)
            return "menu"
        elif level_complete:
            pygame.time.delay(1000)
            wait_for_next_level(screen, WIDTH, HEIGHT)
            running = False

    return "next" if level_complete else "game_over"


if __name__ == "__main__":
    from clases.levels import levels

    while True:
        show_start_screen(screen, WIDTH, HEIGHT)
        for nivel in levels:
            resultado = main(nivel)
            if resultado == "menu":
                break
            elif resultado != "next":
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    from clases.levels import levels

    while True:
        show_start_screen(screen, WIDTH, HEIGHT)
        for nivel in levels:
            resultado = main(nivel)
            if resultado == "menu":
                break 
            elif resultado != "next":
                pygame.quit()
                sys.exit()
