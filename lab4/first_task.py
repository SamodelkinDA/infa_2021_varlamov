import pygame
from pygame.draw import *

pygame.init()

FPS = 15
screen = pygame.display.set_mode((800, 800))
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (217, 217, 217)

rect(screen, GREY, [0, 0, 800, 800], 0)
circle(screen, YELLOW, [400, 400], 250, 0)
line(screen, BLACK, [520, 550], [280, 550], 37)

circle(screen, RED, [280, 330], 35, 0)
circle(screen, RED, [520, 330], 25, 0)
circle(screen, BLACK, [280, 330], 18)
circle(screen, BLACK, [520, 330], 9)

line(screen, BLACK, [150, 170], [1.1 * 303, 1.1 * 304], 12)
line(screen, BLACK, [600, 200], [501 - 20, 20 + 313], 12)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()