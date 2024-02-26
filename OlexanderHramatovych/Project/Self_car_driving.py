import pygame
import sys
import random
pygame.init()

FPS = 60

BLACK_COLOUR = (0,0,0)
WHITE_COLOUR = (255,255,255)
GREEN_COLOUR = (124,252,0)
RED_COLOUR = (255,0,0)

HEIGHT_DISPLAY = 800
WIDTH_DISPLAY = 1000
FINISH = ("FINISH")
display_of_game = pygame.display.set_mode((HEIGHT_DISPLAY,WIDTH_DISPLAY))

def draw_text(text, font_size, color, x, y, screen):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    display_of_game.blit(text_surface, text_rect)




pygame.display.set_caption("Self car driving")

run = True
clock = pygame.time.Clock()

font = pygame.font.Font(None, 35)


while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()
        clock.tick(FPS)
    

    pygame.draw.rect(display_of_game,WHITE_COLOUR,[45,50,50,850])
    pygame.draw.rect(display_of_game,WHITE_COLOUR,[50,50,500,55])
    pygame.draw.rect(display_of_game,WHITE_COLOUR,[500,50,60,700])
    pygame.draw.rect(display_of_game,WHITE_COLOUR,[250,750,310,20])
    pygame.draw.rect(display_of_game,WHITE_COLOUR,[150,600,150,300])

    draw_text(FINISH, 60, GREEN_COLOUR,225,700,display_of_game)

    pygame.draw.rect(display_of_game,RED_COLOUR,[48,850,10,10])



