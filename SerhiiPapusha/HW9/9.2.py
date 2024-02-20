import pygame

FPS = 60

WIDTH_DISPLAY = 700
HEIGHT_DISPLAY = 500

COLOR_BLACK = (0, 3, 8)
COLOR_WHITE = (247, 248, 250)
COLOR_RED = (171, 5, 5)
COLOR_BLUE = (4, 43, 107)

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 60
HEIGHT_RECTANGLE = 50
# RECTANGLE_SIZE = [55, 50, 80, 55]
DELTA_STEP = 5

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption('My first ever game')
done = True
clock = pygame.time.Clock()

while done:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and COORD_X > DELTA_STEP:
        COORD_X = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X < (WIDTH_DISPLAY - (WIDTH_RECTANGLE + DELTA_STEP)):
        COORD_X = COORD_X + DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y > DELTA_STEP:
        COORD_Y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y < (HEIGHT_DISPLAY - (HEIGHT_RECTANGLE + DELTA_STEP)):
        COORD_Y = COORD_Y + DELTA_STEP

    gameDisplay.fill(COLOR_BLACK)

    pygame.draw.rect(gameDisplay, COLOR_RED, [COORD_X, 
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
