import pygame
from pygame.draw import *

pygame.init()
FPS = 15
BLUE = (95, 188, 211)
YELLOW = (200, 171, 55)
GREY = (108, 103, 83)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (211, 211, 211)
GREEN = (55, 200, 113)

screen = pygame.display.set_mode((800, 800))

# background:
rect(screen, BLUE, [0, 0 , 800, 800 / 2], 0)
polygon(screen, GREEN, [[0, 800], [0, 400], [800, 400], [800, 800]])

# чтобы много заборов сделать в третьем задании создаю сразу класс для забора:
# lines_in_wall - число полосок в заборе, left_x и start_y задают левый верхний угол забора
class wall:
    def __init__(self, lines_in_wall, length, width, left_x, start_y):
        self.lines = lines_in_wall
        self.leng = length
        self.wid = width
        self.left_x = left_x
        self.start_y = start_y
    def draw(self):
        rect(screen, YELLOW, [self.left_x, self.start_y, self.wid, self.leng])
        rect(screen, LIGHT_GRAY, [self.left_x, self.start_y, self.wid, self.leng], 1)
        for i in range(1, self.lines):
            x = self.left_x + self.wid // self.lines * i
            line(screen, BLACK, [x, self.start_y], [x, self.start_y + self.leng])
        line(screen, BLACK, [self.left_x, self.start_y + self.leng], [self.left_x + self.wid, self.start_y + self.leng])
        pygame.display.update()

wa1 = wall(15, 200, 800, 0, 200)
wa1.draw()

# Dog house:
polygon(screen, YELLOW, [[600, 420], [520, 480], [640, 545]])
polygon(screen, BLACK, [[600, 420], [520, 480], [640, 545]], 1)
polygon(screen, YELLOW, [[600, 420], [640, 545], [640 + 40, 545 - 20], [600 + 40, 420 - 20]])
polygon(screen, BLACK, [[600, 420], [640, 545], [640 + 40, 545 - 20], [600 + 40, 420 - 20]], 1)
polygon(screen, YELLOW, [[520, 480], [520, 480 + 90], [640, 545 + 90], [640, 545]])
polygon(screen, BLACK, [[520, 480], [520, 480 + 90], [640, 545 + 90], [640, 545]], 1)
polygon(screen, YELLOW, [[640, 545], [680, 525], [680, 595], [640, 635]])
polygon(screen, BLACK, [[640, 545], [680, 525], [680, 595], [640, 635]], 1)
circle(screen, BLACK, [575, 555], 25)
# chain:
ellipse(screen, BLACK, [570 - 30 / 1.4, 555 + 17 / 1.4, 25, 15], 1)
circle(screen, BLACK, [536, 586], 10, 1)
circle(screen, GREY, [545, 575], 8)
circle(screen, BLACK, [545, 575], 8, 1)
ellipse(screen, BLACK, [508, 590, 30, 10], 1)
circle(screen, BLACK, [505, 598], 8, 1)
ellipse(screen, BLACK, [462, 593, 40, 15], 1)
circle(screen, BLACK, [455, 599], 10, 1)
ellipse(screen, BLACK, [425, 592, 30, 5], 1)
circle(screen, BLACK, [420, 592], 10, 1)
ellipse(screen, BLACK, [392, 593, 25, 10], 1)
ellipse(screen, BLACK, [372, 598, 25, 10], 1)

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

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()