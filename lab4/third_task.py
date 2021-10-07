import pygame
from pygame.draw import *

FPS = 15
BLUE = (95, 188, 211)
YELLOW = (200, 171, 55)
GREY = (108, 103, 83)
WHITE = (254, 254, 254)
BLACK = (0, 0, 0)
GREEN = (55, 200, 113)
LIGHT_GRAY = (211, 211, 211)

# чтобы много заборов сделать в третьем задании создаю сразу класс для забора:
# lines_in_wall - число полосок в заборе, left_x и start_y задают левый верхний угол забора
# where - это Surface, где будет находится стена.
class wall:
    def __init__(self, where, lines_in_wall, length, width, left_x, start_y):
        self.where = where
        self.lines = lines_in_wall
        self.leng = length
        self.wid = width
        self.left_x = left_x
        self.start_y = start_y
    def draw(self):
        rect(self.where, YELLOW, [self.left_x, self.start_y, self.wid, self.leng])
        rect(self.where, LIGHT_GRAY, [self.left_x, self.start_y, self.wid, self.leng], 1)
        for i in range(1, self.lines):
            x = self.left_x + self.wid // self.lines * i
            line(self.where, BLACK, [x, self.start_y], [x, self.start_y + self.leng])
        line(self.where, BLACK, [self.left_x, self.start_y + self.leng], [self.left_x + self.wid, self.start_y + self.leng])

class Dog:
    def __init__(self, where, lines_in_wall, length, width, left_x, start_y):
        self.where = where
        self.lines = lines_in_wall
        self.leng = length
        self.wid = width
        self.left_x = left_x
        self.start_y = start_y

    def draw(self):
        rect(self.where, YELLOW, [self.left_x, self.start_y, self.wid, self.leng])
        rect(self.where, LIGHT_GRAY, [self.left_x, self.start_y, self.wid, self.leng], 1)
        for i in range(1, self.lines):
            x = self.left_x + self.wid // self.lines * i
            line(self.where, BLACK, [x, self.start_y], [x, self.start_y + self.leng])
        line(self.where, BLACK, [self.left_x, self.start_y + self.leng], [self.left_x + self.wid, self.start_y + self.leng])

# далее все Surface'ы создаются через .copy(), чтобы избежать рисования на основном дисплее, то есть
# мы при создании нужного нам Surface, который мы потом будем blit'ить с основным Surface
# делаем так, чтобы при создании до блита ничего на дисплее не рисовалось. Также для всех Surface'ов
# мы сразу создаем объекты get_rect, чтобы быть готовыми их blit'ить.

def draw_dog_head():
    dog_head_surf = pygame.Surface((800, 800), pygame.SRCALPHA)
    dog_head_surf.fill((0, 0, 0, 0))
    rect(dog_head_surf, GREY, [100, 450, 80, 80])
    rect(dog_head_surf, BLACK, [100, 450, 80, 80], 1)
    circle(dog_head_surf, GREY, [100, 460], 12)
    circle(dog_head_surf, BLACK, [100, 460], 12, 1)
    circle(dog_head_surf, GREY, [180, 460], 12)
    circle(dog_head_surf, BLACK, [180, 460], 12, 1)
    arc(dog_head_surf, BLACK, [105, 505, 70, 40], 0.2, 2.7)
    polygon(dog_head_surf, WHITE, [[125, 507], [130, 490], [135, 505]])
    polygon(dog_head_surf, BLACK, [[125, 507], [130, 490], [135, 505]], 1)
    polygon(dog_head_surf, WHITE, [[165, 510], [160, 492], [155, 509]])
    polygon(dog_head_surf, BLACK, [[165, 510], [160, 492], [155, 509]], 1)
    ellipse(dog_head_surf, WHITE, [115 ,475, 20, 10])
    ellipse(dog_head_surf, BLACK, [115 ,475, 20, 10], 1)
    circle(dog_head_surf, BLACK, [125, 480], 5)
    circle(dog_head_surf, BLACK, [125, 480], 5)
    ellipse(dog_head_surf, WHITE, [150 ,475, 20, 10])
    ellipse(dog_head_surf, BLACK, [150 ,475, 20, 10], 1)
    circle(dog_head_surf, BLACK, [160, 480], 5)
    circle(dog_head_surf, BLACK, [160, 480], 5)
    return dog_head_surf


def draw_dog():
    dog_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
    dog_surface.fill((0, 0, 0, 0))
    dog_rect = dog_surface.get_rect(center=(0, 0))
    #   Body:
    massiv_ellipses = ([110, 460, 180, 90], [220, 450, 100, 70], [210, 450, 60, 60], [250, 460, 30, 115],
                      [218, 560, 50, 20], [285, 465, 60, 60], [305, 470, 30, 115], [274, 570, 50, 20],
                      [95, 485, 45, 110], [65, 580, 60, 20], [180, 510, 45, 110], [150, 605, 60, 20]
                      )
    for i in massiv_ellipses:
        ellipse(dog_surface, GREY, i)
    #    Head:
    dog_surface.blit(draw_dog_head(), (0, 0))
    return dog_surface

def draw_picture():
    pass

def draw_chain():
    chain_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
    chain_surface.fill((0, 0, 0, 0))
    chain_rect = chain_surface.get_rect(center=(400, 400))
    circle(chain_surface, GREY, [545, 575], 8)
    massiv_ellipses = ([549, 543, 25, 15], [526, 576, 20, 20], [537, 567, 16, 16], [508, 590, 30, 10],
                      [497, 590, 16, 16], [462, 593, 40, 15], [445, 589, 20, 20], [425, 592, 30, 5], 
                      [410, 582, 20, 20], [392, 593, 25, 10], [372, 598, 25, 10]
                      )
    for i in massiv_ellipses:
        ellipse(chain_surface, BLACK, i, 1)
    return (chain_surface, chain_rect)


# Walls:
wall_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
wall_surface.fill((0, 0, 0, 0))
wall_rect = wall_surface.get_rect(center=(400, 400))
massive_wall = ((300, 700, 100, 50), (400, 500, 0, 100), (300, 300, 0, 250), (200, 400, 400, 350))
for i in massive_wall:
    wall(wall_surface, 15, *i).draw()

# Dog:

dog_surface = draw_dog()

# Здесь мы меняем конфигурации всех собак
# методы pygame.transform возвращают нам новый измененный указанным образом Surface

dog_surfaces = []
dog_rects = []
koordinates = ((400, 400), (0, 550), (500, 380), (1200, 500))
dog_surfaces.append(dog_surface.copy())
dog_surfaces.append(pygame.transform.flip(dog_surface.copy(), True, False))
dog_surfaces.append(pygame.transform.flip(dog_surface.copy(), True, False))
dog_surfaces.append(pygame.transform.scale2x(dog_surface.copy()))
for i, j in zip(range(4), koordinates):
    dog_rects.append(dog_surfaces[i].get_rect(center=j))
    
#Dog house:
house_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
house_surface.fill((0, 0, 0, 0))
house_rect = house_surface.get_rect(center=(400, 400))
massive_house = (
    [[600, 420], [520, 480], [640, 545]],
    [[600, 420], [640, 545], [680, 525], [640, 400]],
    [[520, 480], [520, 570], [640, 635], [640, 545]],
    [[640, 545], [680, 525], [680, 595], [640, 635]]
)
for i in massive_house:
    polygon(house_surface, YELLOW, i)
    polygon(house_surface, BLACK, i, 1)
circle(house_surface, BLACK, [575, 555], 25)



# Экран и фон
screen = pygame.display.set_mode((800, 800))
rect(screen, BLUE, [0, 0 , 800, 800 / 2], 0)
rect(screen, GREEN, [0, 400 , 800, 800 / 2], 0)


# Здесь происходит отрисовка всего на дисплее, мы blit'им наши Surface'ы в указанной для них rect области
# в один общий Surface. Удобство заключается в том, что мы можем спокойно выбрать порядок отрисовки, а не двигать
# огромные куски кода, чтобы указать порядок.

screen.blit(wall_surface, wall_rect)
for i in range(3):
    screen.blit(dog_surfaces[i], dog_rects[i])
screen.blit(house_surface, house_rect)
screen.blit(*draw_chain())
screen.blit(dog_surfaces[3], dog_rects[3])

pygame.init()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    #wall.update()
    #pygame.display.flip()

pygame.quit()