import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
window_width = 800
window_height = 600

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the size of each grid cell
cell_size = 20

# Calculate the number of cells in the game grid
grid_width = window_width // cell_size
grid_height = window_height // cell_size

# Set the initial position of the snake
snake_x = grid_width // 2
snake_y = grid_height // 2

# Set the initial velocity of the snake
snake_dx = 1
snake_dy = 0

# Initialize the snake body
snake_body = [(snake_x, snake_y)]
snake_length = 1

# Set the initial position of the food
food_x = random.randint(0, grid_width - 1)
food_y = random.randint(0, grid_height - 1)

# Set the game clock
clock = pygame.time.Clock()

# Set the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dy != 1:
                snake_dx = 0
                snake_dy = -1
            elif event.key == pygame.K_DOWN and snake_dy != -1:
                snake_dx = 0
                snake_dy = 1
            elif event.key == pygame.K_LEFT and snake_dx != 1:
                snake_dx = -1
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx != -1:
                snake_dx = 1
                snake_dy = 0

    # Update snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check for collision with boundaries
    if snake_x < 0 or snake_x >= grid_width or snake_y < 0 or snake_y >= grid_height:
        game_over = True

    # Check for collision with self
    if (snake_x, snake_y) in snake_body[1:]:
        game_over = True

    # Update snake body
    snake_body.insert(0, (snake_x, snake_y))
    if len(snake_body) > snake_length:
        snake_body.pop()

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        food_x = random.randint(0, grid_width - 1)
        food_y = random.randint(0, grid_height - 1)

    # Clear the window
    window.fill(black)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(window, white, (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))

    # Draw the food
    pygame.draw.rect(window, red, (food_x * cell_size, food_y * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(10)

# Quit the game
pygame.quit()
