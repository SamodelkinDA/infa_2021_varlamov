import turtle as tr

tr.pu()
tr.goto(-300, 0)
tr.pd()
tr.shape('circle')
tr.turtlesize(0.4, 0.4, 0.4)
t = 0
y = 10
k = 0   # маркер на пролет через y = 0
Vy_0 = 40
while 1:
    dt = 0.1
    ay = -9.8
    Vx = 30
    dx = Vx * dt
    Vy = Vy_0 + ay * t
    if y < -0.01 and k == 0:
        Vy_0 = 40
        t = 0
    
    dy = Vy * dt
    x, y = tr.pos()
    tr.goto(x + dx, y + dy)
    t += dt