import turtle as t

t.color('blue')
t.shape('classic')
t.pu()
t.goto(-600, -100)
t.pd()

# ниже я создал функции с командами, которыми можно задать любую цифру

def end():
    t.pu()
    x, y = t.pos()
    t.goto(x + 65, -100)
    t.pd()


def diagonal_right():
    x, y = t.pos()
    t.goto(x + 50, y + 50)

def diagonal_left():
    x, y = t.pos()
    t.goto(x - 50, y - 50)


def horizontal_rigth():
    x, y = t.pos()
    t.goto(x + 50, y)

def horizontal_left():
    x, y = t.pos()
    t.goto(x - 50, y)

def vertical_down():
    x, y = t.pos()
    t.goto(x, y - 50)

def vertical_up():
    x, y = t.pos()
    t.goto(x, y + 50)

def down_space():
    t.pu()
    x, y = t.pos()
    t.goto(x, y - 50)
    t.pd()

def up_space():
    t.pu()
    x, y = t.pos()
    t.goto(x, y + 50)
    t.pd()


zero = (up_space, up_space, horizontal_rigth, vertical_down, vertical_down, horizontal_left, vertical_up, vertical_up, end)
one = (up_space, diagonal_right, vertical_down, vertical_down, end)
two = (up_space, up_space, horizontal_rigth, vertical_down, diagonal_left, horizontal_rigth, end)
three = (up_space, up_space, horizontal_rigth, diagonal_left, horizontal_rigth, diagonal_left, end)
four = (up_space,  up_space, vertical_down, horizontal_rigth, vertical_up, vertical_down, vertical_down, end)
five = (up_space, up_space, horizontal_rigth, horizontal_left, vertical_down, horizontal_rigth, vertical_down, horizontal_left, end)
six = (up_space, vertical_down, horizontal_rigth, vertical_up, horizontal_left, diagonal_right, end)
seven = (up_space, up_space, horizontal_rigth, diagonal_left, vertical_down, end)
eight = (horizontal_rigth, vertical_up, horizontal_left, vertical_down, vertical_up, vertical_up, horizontal_rigth, vertical_down, end)
nine = (diagonal_right, vertical_up, horizontal_left, vertical_down, horizontal_rigth, end)

sp = [one, four, one, seven, zero, zero]

for number in sp:
    for command in number:
        command()

t.done()