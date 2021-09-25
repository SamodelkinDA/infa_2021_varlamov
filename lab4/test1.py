import pygame
from pygame import transform
from pygame.draw import *

pygame.init()

FPS = 15

BLUE = (95, 188, 211)
YELLOW = (200, 171, 55)
GREY = (108, 103, 83)
WHITE = (254, 254, 254)
BLACK = (0, 0, 0)
LIGHT_GRAY = (211, 211, 211)
GREEN = (55, 200, 113)

clock = pygame.time.Clock()
finished = False

# Dog:
dog_surface = pygame.display.set_mode((800, 800))
dog_surface.set_colorkey((255, 255, 255))
dog_rect = dog_surface.get_rect(center=(0, 0))

#   Body:
ellipse(dog_surface, GREY, [110, 460, 180, 90])
ellipse(dog_surface, GREY, [220, 450, 100, 70])
circle(dog_surface, GREY, [240, 480], 30)
ellipse(dog_surface, GREY, [250, 460, 30, 115])
ellipse(dog_surface, GREY, [218, 560, 50, 20])
circle(dog_surface, GREY, [315, 495], 30)
ellipse(dog_surface, GREY, [305, 470, 30, 115])
ellipse(dog_surface, GREY, [274, 570, 50, 20])
ellipse(dog_surface, GREY, [95, 485, 45, 110])
ellipse(dog_surface, GREY, [65, 580, 60, 20])
ellipse(dog_surface, GREY, [180, 510, 45, 110])
ellipse(dog_surface, GREY, [150, 605, 60, 20])
#    Head:
rect(dog_surface, GREY, [100, 450, 80, 80])
rect(dog_surface, BLACK, [100, 450, 80, 80], 1)
circle(dog_surface, GREY, [100, 460], 12)
circle(dog_surface, BLACK, [100, 460], 12, 1)
circle(dog_surface, GREY, [180, 460], 12)
circle(dog_surface, BLACK, [180, 460], 12, 1)
arc(dog_surface, BLACK, [105, 505, 70, 40], 0.2, 2.7)
polygon(dog_surface, WHITE, [[125, 507], [130, 490], [135, 505]])
polygon(dog_surface, BLACK, [[125, 507], [130, 490], [135, 505]], 1)
polygon(dog_surface, WHITE, [[165, 510], [160, 492], [155, 509]])
polygon(dog_surface, BLACK, [[165, 510], [160, 492], [155, 509]], 1)
ellipse(dog_surface, WHITE, [115 ,475, 20, 10])
ellipse(dog_surface, BLACK, [115 ,475, 20, 10], 1)
circle(dog_surface, BLACK, [125, 480], 5)
circle(dog_surface, BLACK, [125, 480], 5)
ellipse(dog_surface, WHITE, [150 ,475, 20, 10])
ellipse(dog_surface, BLACK, [150 ,475, 20, 10], 1)
circle(dog_surface, BLACK, [160, 480], 5)
circle(dog_surface, BLACK, [160, 480], 5)

dog_1_surface = dog_surface.copy()
dog_1_rect = dog_surface.get_rect(center=(400, 250))

dog_2_surface = pygame.transform.flip(dog_surface.copy(), True, False)
dog_2_rect = dog_surface.get_rect(center=(0, 450))

screen = pygame.display.set_mode((800, 800))
screen.fill(GREEN)

screen.blit(dog_1_surface, dog_1_rect)
screen.blit(dog_2_surface, dog_2_rect)

pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()