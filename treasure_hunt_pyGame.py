import pygame, sys
from pygame.locals import *
import random

WIDTH=800
HEIGHT=600
treasureWindow = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)

WHITE = [255, 255, 255]
YELLOW = [255, 255, 0]
CIRCLE_SIZE = 50
treasureWindow.fill(WHITE)
RANDOM_CIRCLES = 10

# our game object class
class Circle:
    def __init__(self, circle, color, size, speed):
        self.speed = speed
        self.color = color
        self.size = size
        self.pos = image.get_rect().move(0, size)

    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > WIDTH:
            self.pos.left = 0

circles = [
    pygame.draw.circle(treasureWindow, [255,0,0], (random.randint(CIRCLE_SIZE, WIDTH), random.randint(CIRCLE_SIZE, HEIGHT)), CIRCLE_SIZE, 0),
    pygame.draw.circle(treasureWindow, [255,0,0], (random.randint(CIRCLE_SIZE, WIDTH), random.randint(CIRCLE_SIZE, HEIGHT)), CIRCLE_SIZE, 0)
    ]

for x in range(RANDOM_CIRCLES + 1):
        x_pos = random.randint(CIRCLE_SIZE, WIDTH)
        y_pos = random.randint(CIRCLE_SIZE, HEIGHT)
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        circle = pygame.draw.circle(treasureWindow, [r,g,b], (x_pos, y_pos), CIRCLE_SIZE, 0)
        circles.append(circle)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
             ## if mouse is pressed get position of cursor ##
            pos = pygame.mouse.get_pos()

            for circle in circles:  
                if circle.collidepoint(pos):
                    circle = circle.move(40, 20)
                    print("ouch {pos}".format(pos=pos))

    pygame.display.update()
