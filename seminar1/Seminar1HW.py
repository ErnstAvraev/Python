# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

week_day = int(input("Введите цифру дня недели: "))
if week_day%6 == 0 or week_day%7 == 0:
    print("Выходной")
else:
    print("Нет")

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def checkPredicate(x,y,z):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result

dotX = int(input("Input dot X: "))
dotY = int(input("Input dot Y: "))
dotZ = int(input("input dot Z: "))

if checkPredicate(dotX,dotY,dotZ) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def checkCoordinates(x,y):
    if x > 0 and y > 0:
        text = 1
    elif x < 0 and y > 0:
        text = 2
    elif x < 0 and y < 0:
        text = 3
    elif x > 0 and y < 0:
        text = 4
    print(f"Точка находится в {text} четверти плоскости")

coordX= int(input("Input coordinate X: "))
coordY = int(input("Input coordinate Y: "))
checkCoordinates(coordX,coordY)

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти: "))
if quarter==1:
    print("Диапазон х от 1 до +бесконечности")
    print("Диапазон у от 1 до +бесконечности")
if quarter==2:
    print("Диапазон х от -1 до -бесконечности")
    print("Диапазон у от 0 до +бесконечности")
if quarter==3:
    print("Диапазон х от -1 до -бесконечности")
    print("Диапазон у от -1 до -бесконечности")
if quarter==4:
    print("Диапазон х от 1 до +бесконечности")
    print("Диапазон у от -1 до -бесконечности")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")