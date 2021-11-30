import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption('Hello world!')

basicFont = pygame.font.SysFont(None, 48)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

text = basicFont.render('hello world!', True, WHITE, BLUE)
textRect = text.get_rect()

textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(GREEN)
windowSurface.blit(text, textRect)

pygame.draw.circle(windowSurface, BLUE, (300, 500), 50, 0)


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()