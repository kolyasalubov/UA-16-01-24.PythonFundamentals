import pygame
import random

FPS = 60

WIDTH_DISPLAY = 1280
HEIGHT_DISPLAY = 720

COORD_X = 50
COORD_Y = 50

WIDTH_FISH = 120
HEIGHT_FISH = 100
FISH_INCREASE_STEP = 20

WIDTH_FOOD = 50
HEIGHT_FOOD = 90

DELTA_STEP = 20

END_SCORE = 10

pygame.font.init()

SCORE_FONT_SIZE = 40
GAME_OVER_FONT_SIZE = 120

SCORE_POSITION_X = 20
SCORE_POSITION_Y = 20

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

SCORE_FONT = pygame.font.SysFont("Arial", SCORE_FONT_SIZE)
GAME_OVER_FONT = pygame.font.SysFont("Arial", GAME_OVER_FONT_SIZE)


pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("Final Project Mykhailo Tsviklinskyi")

background_image = pygame.image.load("MykhailoTsviklinskyi/FinalProject/aquarium.jpeg")
background_image_scale = pygame.transform.scale(background_image, (WIDTH_DISPLAY, HEIGHT_DISPLAY))

fish = pygame.image.load("MykhailoTsviklinskyi/FinalProject/angry_fish.png")
fish_scale = pygame.transform.scale(fish, (WIDTH_FISH, HEIGHT_FISH))

dead_fish = pygame.image.load("MykhailoTsviklinskyi/FinalProject/dead_fish.png")
dead_fish_scale = pygame.transform.scale(fish, (WIDTH_FISH, HEIGHT_FISH))

food_1 = pygame.image.load("MykhailoTsviklinskyi/FinalProject/food1.png")
food_1_scale = pygame.transform.scale(food_1, (WIDTH_FOOD, HEIGHT_FOOD))

food_2 = pygame.image.load("MykhailoTsviklinskyi/FinalProject/food2.png")
food_2_scale = pygame.transform.scale(food_2, (WIDTH_FOOD, HEIGHT_FOOD))

food_3 = pygame.image.load("MykhailoTsviklinskyi/FinalProject/food3.png")
food_3_scale = pygame.transform.scale(food_3, (WIDTH_FOOD, HEIGHT_FOOD))

food_4 = pygame.image.load("MykhailoTsviklinskyi/FinalProject/food4.png")
food_4_scale = pygame.transform.scale(food_4, (WIDTH_FOOD, HEIGHT_FOOD))

food_list = [food_1_scale, food_2_scale, food_3_scale, food_4_scale]
random_food = random.choice(food_list)

fish_position = [COORD_X, COORD_Y]

food_position = [random.randrange(WIDTH_FISH // 2, WIDTH_DISPLAY - WIDTH_FISH // 2 - DELTA_STEP),
                 random.randrange(HEIGHT_FISH // 2, HEIGHT_DISPLAY - HEIGHT_FISH // 2 - DELTA_STEP)]

score = 0


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    if score < END_SCORE:
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_LEFT] and COORD_X > DELTA_STEP:
            fish_position[0] = COORD_X - DELTA_STEP
            COORD_X -= DELTA_STEP
        if keys[pygame.K_RIGHT] and COORD_X < WIDTH_DISPLAY - WIDTH_FISH - DELTA_STEP:
            fish_position[0] = COORD_X + DELTA_STEP
            COORD_X += DELTA_STEP
        if keys[pygame.K_UP] and COORD_Y > DELTA_STEP:
            fish_position[1] = COORD_Y - DELTA_STEP
            COORD_Y -= DELTA_STEP
        if keys[pygame.K_DOWN] and COORD_Y < HEIGHT_DISPLAY - HEIGHT_FISH - DELTA_STEP:
            fish_position[1] = COORD_Y + DELTA_STEP
            COORD_Y += DELTA_STEP


    if fish_position[0] + WIDTH_FISH / 2 in range(food_position[0] - DELTA_STEP, food_position[0] + WIDTH_FISH // 2) and fish_position[1] + HEIGHT_FISH / 2 in range(food_position[1] - DELTA_STEP, food_position[1] + HEIGHT_FISH // 2):
        score += 1
        WIDTH_FISH += FISH_INCREASE_STEP
        HEIGHT_FISH += FISH_INCREASE_STEP
        fish_scale = pygame.transform.scale(fish, (WIDTH_FISH, HEIGHT_FISH))
        food_position = [random.randrange(WIDTH_FISH // 2, WIDTH_DISPLAY - WIDTH_FISH // 2 - DELTA_STEP),
                         random.randrange(HEIGHT_FISH // 2, HEIGHT_DISPLAY - HEIGHT_FISH // 2 - DELTA_STEP)]
        random_food = random.choice(food_list)
        
    gameDisplay.blit(background_image_scale, (0, 0))

    gameDisplay.blit(fish_scale, fish_position)
        
    gameDisplay.blit(random_food, food_position)

    if score < END_SCORE:
        score_text = SCORE_FONT.render(f"SCORE: {score}", True, BLACK_COLOR)
        gameDisplay.blit(score_text, (SCORE_POSITION_X, SCORE_POSITION_Y))
    else:
        gameDisplay.fill(BLACK_COLOR)
        dead_fish_scale = pygame.transform.scale(dead_fish, (WIDTH_FISH, HEIGHT_FISH))
        gameDisplay.blit(dead_fish_scale, fish_position)
        game_over_text = GAME_OVER_FONT.render("GAME OVER", True, RED_COLOR)
        gameDisplay.blit(game_over_text, (WIDTH_DISPLAY//4, HEIGHT_DISPLAY//3))


    pygame.display.update()
    clock.tick(FPS)
