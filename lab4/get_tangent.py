x1, y1 = 600, 200   #точка на прямой
x0, y0 = 520, 330   #центр окружности
r = 25

x2, y2 = 0, 0

for x in range(800):
    for y in range(800):
        if abs((x - x0) ** 2 + (y - y0) ** 2 - r ** 2) < 50:
            if abs((x - x0) * (x - x1) + (y - y0) * (y - y1)) < 50:
                print(x, y)

tanx = (x1 - x) / (y1 - y)
print(20 * tanx)