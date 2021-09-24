from random import randint
import turtle as t

t.pu()
t.goto(-30, -30)
t.pd()
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.shapesize(0.1, 0.1, 0.1)

number_of_turtles = 2

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    if pool.index(unit) % 2 == 0:
        unit.color('red')
    unit.penup()
    unit.speed(0)
    unit.shapesize(0.3, 0.3, 0.3)
    unit.goto(randint(-30, 30), randint(-30, 30))
    unit.x, unit.y = unit.pos()
    unit.Vx, unit.Vy = 50, 50
    print(unit.x, unit.y)

t = 0
while t < 100:
    dt = 0.05
    for unit in pool:
        unit.penup()
        unit.x, unit.y = unit.x + unit.Vx * dt, unit.y + unit.Vy * dt
        if unit.x <- 30:
            unit.Vx *= -1
        if unit.x > 30:
            unit.Vx *= -1
        if unit.y > 30:
            unit.Vy *= -1
        if unit.y < -30:
            unit.Vy *= -1
        unit.goto(unit.x, unit.y)
    for i in range(number_of_turtles):
        for j in range(i + 1, number_of_turtles):
            if i != j:
                if abs(pool[i].x - pool[j].x) < 11 and abs(pool[i].y - pool[j].y) < 11:
                    print('touched')
                    pool[i].Vx, pool[j].Vx = pool[j].Vx, -1 * pool[i].Vx
                    pool[i].Vy, pool[j].Vy = pool[j].Vy, -1 * pool[i].Vy
    t += dt