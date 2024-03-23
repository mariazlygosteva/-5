import math

xc = float(input("Введите координату x центра окружности: "))
yc = float(input("Введите координату y центра окружности: "))
r = float(input("Введите радиус окружности: "))
x = float(input("Введите координату x точки: "))
y = float(input("Введите координату y точки: "))

distance = math.sqrt((x - xc)*2 + (y - yc)*2)

if distance < r:
    print("Точка находится внутри окружности")
elif distance == r:
    print("Точка лежит на окружности")
else:
    print("Точка располагается за пределами окружности")