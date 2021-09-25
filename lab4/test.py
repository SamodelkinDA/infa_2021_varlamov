import pygame
from pygame import transform
from pygame.draw import *

pygame.init()

FPS = 15
screen = pygame.display.set_mode((800, 800))
screen.set_colorkey((255, 255, 255))

BLUE = (95, 188, 211)
YELLOW = (200, 171, 55)
GREY = (108, 103, 83)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (211, 211, 211)
GREEN = (55, 200, 113)

clock = pygame.time.Clock()
finished = False

# Dog:
#   Body:
ellipse(screen, GREY, [110, 460, 180, 90])
ellipse(screen, GREY, [220, 450, 100, 70])
circle(screen, GREY, [240, 480], 30)
ellipse(screen, GREY, [250, 460, 30, 115])
ellipse(screen, GREY, [218, 560, 50, 20])
circle(screen, GREY, [315, 495], 30)
ellipse(screen, GREY, [305, 470, 30, 115])
ellipse(screen, GREY, [274, 570, 50, 20])
ellipse(screen, GREY, [95, 485, 45, 110])
ellipse(screen, GREY, [65, 580, 60, 20])
ellipse(screen, GREY, [180, 510, 45, 110])
ellipse(screen, GREY, [150, 605, 60, 20])
#    Head:
rect(screen, GREY, [100, 450, 80, 80])
rect(screen, BLACK, [100, 450, 80, 80], 1)
circle(screen, GREY, [100, 460], 12)
circle(screen, BLACK, [100, 460], 12, 1)
circle(screen, GREY, [180, 460], 12)
circle(screen, BLACK, [180, 460], 12, 1)
arc(screen, BLACK, [105, 505, 70, 40], 0.2, 2.7)
polygon(screen, WHITE, [[125, 507], [130, 490], [135, 505]])
polygon(screen, BLACK, [[125, 507], [130, 490], [135, 505]], 1)
polygon(screen, WHITE, [[165, 510], [160, 492], [155, 509]])
polygon(screen, BLACK, [[165, 510], [160, 492], [155, 509]], 1)
ellipse(screen, WHITE, [115 ,475, 20, 10])
ellipse(screen, BLACK, [115 ,475, 20, 10], 1)
circle(screen, BLACK, [125, 480], 5)
circle(screen, BLACK, [125, 480], 5)
ellipse(screen, WHITE, [150 ,475, 20, 10])
ellipse(screen, BLACK, [150 ,475, 20, 10], 1)
circle(screen, BLACK, [160, 480], 5)
circle(screen, BLACK, [160, 480], 5)

pygame.image.save(screen, "circle.png")

circle_surface = pygame.image.load("circle.png").convert()
circle_surface.set_colorkey(BLACK)
circle_rect = circle_surface.get_rect(center=(10, 10))
circle_surface = pygame.transform.flip(circle_surface, False, True)
screen.blit(circle_surface, circle_rect)


pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()