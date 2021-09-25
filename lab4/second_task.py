import pygame
from pygame.draw import *

pygame.init()
FPS = 15
screen = pygame.display.set_mode((800, 800))
BLUE = (95, 188, 211)
YELLOW = (200, 171, 55)
GREY = (108, 103, 83)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (55, 200, 113)
numb_of_lines = 15

# background:
rect(screen, BLUE, [0, 0 , 800, 800 / 2], 0)
polygon(screen, GREEN, [[0, 800], [0, 400], [800, 400], [800, 800]])

# чтобы много заборов сделать в третьем задании создаю сразу класс для забора:
class wall:
    def __init__(self, lines_in_wall, length, width, left_x, start_y):
        self.lines = lines_in_wall
        self.leng = length
        self.wid = width
        self.left_x = left_x
        self.start_y = start_y
    def draw(self):
        rect(screen, YELLOW, [self.left_x, self.start_y, self.wid, self.leng])
        for i in range(1, self.lines):
            x = self.left_x + self.wid // self.lines * i
            line(screen, BLACK, [x, self.start_y], [x, self.start_y + self.leng])
        line(screen, BLACK, [self.left_x, self.start_y + self.leng], [self.left_x + self.wid, self.start_y + self.leng])
        pygame.display.update()

wa1 = wall(15, 300, 800, 0, 200)
wa1.draw()

#Dog house:
polygon(screen, YELLOW, [[600, 420], [520, 480], [640, 545]])
polygon(screen, BLACK, [[600, 420], [520, 480], [640, 545]], 1)
polygon(screen, YELLOW, [[600, 420], [640, 545], [640 + 40, 545 - 20], [600 + 40, 420 - 20]])
polygon(screen, BLACK, [[600, 420], [640, 545], [640 + 40, 545 - 20], [600 + 40, 420 - 20]], 1)
polygon(screen, YELLOW, [[520, 480], [520, 480 + 90], [640, 545 + 90], [640, 545]])
polygon(screen, BLACK, [[520, 480], [520, 480 + 90], [640, 545 + 90], [640, 545]], 1)
polygon(screen, YELLOW, [[640, 545], [680, 525], [680, 595], [640, 635]])
polygon(screen, BLACK, [[640, 545], [680, 525], [680, 595], [640, 635]], 1)
circle(screen, BLACK, [575, 555], 25)
#chain:
ellipse(screen, BLACK, [575 - 30 / 1.4, 555 + 17 / 1.4, 25, 15], 1)
circle(screen, GREY, [550, 575], 8)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()