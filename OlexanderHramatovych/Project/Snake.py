import pygame
import random

# initilization
pygame.init()

# display 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)

# snake and food size
BLOCK_SIZE = 20

# Spees of the snake
SPEED = 20

# initilize the main screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# message on display
def message(msg, color):
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(msg, True, color)
    screen.blit(text, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

# main function
def gameLoop():
    # cordinations of snake
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # the first length of snake and the list of its cordinates
    snake_length = 1
    snake_list = []

    # first cordinates of food
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    game_over = False
    game_close = False

     
    move_x = 0
    move_y = 0

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            message("You Lost! Press Q to quit or C to Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                game_over = True
                game_close = False
            if keys[pygame.K_c]:
                game_close = False  # Exit the game_close loop
                gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and y >= 0:
            move_y = -BLOCK_SIZE
            move_x = 0
        elif keys[pygame.K_DOWN] and y <= SCREEN_HEIGHT:
            move_y = BLOCK_SIZE
            move_x = 0
        elif keys[pygame.K_RIGHT] and x <= SCREEN_WIDTH:
            move_y = 0
            move_x = BLOCK_SIZE
        elif keys[pygame.K_LEFT] and x > 0:
            move_y = 0
            move_x = -BLOCK_SIZE
        


        x += move_x
        y += move_y

        # Chdck wheter the snake is facing the borders
        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_close = True

        # Creating the new food if the previos is itten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        # Deleting the segment of snake if it is higher than length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check whether snake is breaking breaking itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Drawing the snake
        for segment in snake_list:
            pygame.draw.rect(screen, BLUE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()
    quit()

gameLoop()