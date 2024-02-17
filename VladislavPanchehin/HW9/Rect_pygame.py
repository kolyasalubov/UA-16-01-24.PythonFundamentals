import pygame
import os


FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)


pygame.init()

# download music file
music_file = "play.mp3"
pygame.mixer.music.load(music_file)

# play_music
pygame.mixer.music.play()


gameDisplay = pygame.display.set_mode(
    (WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

# font standart use
font = pygame.font.Font(None, 35)
# create text surface
text_surface = font.render("Vladislav is GOOD MAN :)",
                           True, (255, 255, 255))  # text color white
#
text_activate = text_surface.get_rect(center=(250, 250))


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and COORD_X > DELTA_STEP:
        COORD_X = COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X < WIDTH_DISPLAY - WIDTH_RECTANGLE - DELTA_STEP:
        COORD_X = COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y > DELTA_STEP:
        COORD_Y = COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y < HEIGHT_DISPLAY - HEIGHT_RECTANGLE - DELTA_STEP:
        COORD_Y = COORD_Y+DELTA_STEP

    gameDisplay.fill(BLACK_COLOR)
    # draw text
    gameDisplay.blit(text_surface, text_activate)

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X,
                                              COORD_Y,
                                              WIDTH_RECTANGLE,
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)

# stop music
pygame.mixer.music.stop()
pygame.quit()