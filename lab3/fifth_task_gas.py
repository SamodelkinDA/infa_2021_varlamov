from random import randint
import turtle as t

t.pu()
t.goto(-300, -300)
t.pd()
t.forward(600)
t.left(90)
t.forward(600)
t.left(90)
t.forward(600)
t.left(90)
t.forward(600)
t.shapesize(0.1, 0.1, 0.1)

number_of_turtles = 30

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.shapesize(0.5, 0.5, 0.5)
    unit.goto(randint(-300, 300), randint(-300, 300))
    unit.x, unit.y = unit.pos()
    unit.Vx, unit.Vy = randint(-90, 90), randint(-30, 30)
    print(unit.x, unit.y)

t = 0
dt = 0.1
while t < 100:
    for unit in pool:
        unit.x, unit.y = unit.x + unit.Vx * dt, unit.y + unit.Vy * dt
        if unit.x < -300 or unit.x > 300:
            unit.Vx *= -1
        if unit.y > 300 or unit.y < -300:
            unit.Vy *= -1
        unit.goto(unit.x, unit.y)
    i = 0
    for i in range(number_of_turtles):
        j = i + 1
        for j in range(i + 1, number_of_turtles):
            if abs(pool[i].x - pool[j].x) < 11 and abs(pool[i].y - pool[j].y) < 11:
                r1 = abs(pool[i].x - pool[j].x)
                r2 = abs(pool[i].y - pool[j].y)
                pool[i].Vx, pool[j].Vx = pool[j].Vx, -1 * pool[i].Vx 
                pool[i].Vy, pool[j].Vy = pool[j].Vy, -1 * pool[i].Vy
    t += dt