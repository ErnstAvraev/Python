# # Задайте список из нескольких чисел. Напишите программу,
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# arStr = input().split()
# arrInt = []
# for i in arStr:
#     arrInt.append(int(i))
# sum = 0
# for i in range(len(arrInt)):
#     if i % 2 != 0:
#         sum = sum + arrInt[i]
#     else:
#         continue
# print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний
# и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# arr = list(map(int, input("Введите числа через пробел:\n").split()))

# if len(arr) % 2 != 0:
#      a = len(arr)//2 + 1
# else:
#      a = len(arr)//2

# newArr = []
# for i in range(a):
#      newI = arr[i]*arr[len(arr)-i-1]
#      newArr.append(newI)

# print(newArr)


# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# newLst = []

# for i in lst:
#      if i%1 != 0:
#           newLst.append(round(i%1, 4))

# max = newLst[0]
# min = newLst[0]

# for i in newLst:
#      if i > max:
#           max = i
#      elif i < min:
#           min = i
# print(round(max - min, 4))

# new_lst = [round(i%1, 4) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# Напишите программу, которая будет преобразовывать десятичное
# число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# s = " "
# n = int(input("Input a number to convert to binary: \n"))
# while n != 0:
#     s = str(n % 2)+s
#     n //= 2
# print(s)

# Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
     if n in [1,2]:
          return 1
     else:
          return fib(n-1)+fib(n-2)

def negaFib(n):
     return ((-1)**(n+1))*fib(n)

n = int(input("Введите порядковый номер числа = "))
fibArr1 = []
fibArr2 = []
for e in range(1,n+1):
     fibArr1.append(negaFib(e))
for a in range(1,n+1):
     fibArr2.append(fib(a))

fibArr1.reverse()
fullArr= fibArr1+fibArr2

print(fullArr)