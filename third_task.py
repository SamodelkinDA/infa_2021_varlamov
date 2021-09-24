import turtle as t

t.color('blue')
t.shape('classic')
t.pu()
t.goto(-600, -100)
t.pd()

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

# считываю текстовую информацию из файла, затем при помощи словаря вызываю нужные функции

dic_of_functions = {'end': end, 'diagonal_right': diagonal_right, 'diagonal_left': diagonal_left,
    'horizontal_rigth': horizontal_rigth, 'horizontal_left': horizontal_left, 'vertical_down': vertical_down,
    'vertical_up': vertical_up, 'down_space': down_space, 'up_space': up_space, 'end': end
}

f = open('movements.txt', mode='rt', encoding='utf-8')
total_lines_in_f = len(f.readlines())
f.seek(0)
for _ in range(total_lines_in_f):
    commands = f.readline().strip().split(', ')
    for command in commands:
        print(command)
        dic_of_functions[command]()

t.done()