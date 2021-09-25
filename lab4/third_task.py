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
LIGHT_GRAY = (211, 211, 211)

# background:
rect(screen, BLUE, [0, 0 , 800, 800 / 2], 0)
polygon(screen, GREEN, [[0, 800], [0, 400], [800, 400], [800, 800]])

# чтобы много заборов сделать в третьем задании создаю сразу класс для забора:
class wall:
    def __init__(self, lines_in_wall, length, width, left_x, start_y, ):
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

wa0 = wall(15, 300, 700, 100, 50)
wa0.draw()
wa2 = wall(15, 400, 500, 0, 100)
wa2.draw()
wa1 = wall(15, 300, 300, 0, 250)
wa1.draw()
# wa3 = wall(15, )
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

class Dog:
    def __init__(self):
        pass
pygame.mouse.get_pos()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()