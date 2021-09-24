import turtle as tur
from random import randint

ws = tur.Screen()
tur.speed(0)
tur.shape('classic')
for _ in range(1000):
    i = randint(0, 3)
    if i == 1:
        tur.forward(randint(1, 100))
    if i == 2:
        tur.backward(randint(1, 100))
    if i == 3:
        tur.left(randint(1, 180))
    else:
        tur.right(randint(1, 180))