# сумма двух чисел
#a = 1
#b = 2
#c = a + b
# print(c)

#print(10,11,12, sep ="+++++",end="\n")
#print(10,11,12, sep="+++++")

# Задачи:

# 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

# примеры
# 5, 25 -> yes
# 4, 16 -> yes
# 25, 5 -> yes
# 8, 9 -> no

#a = int(input("Введите число a = "))
#b = int(input("Введите число b = "))

# if a*a == b:
#    print("да")
# elif b*b == a:
#    print("да")
# else:
#    print("нет")

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

# Примеры
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

#fiver = list(map(int, input('Введите 5 чисел через пробел: ').split()))
# max=fiver[0]
# for i in range(len(fiver)):
#    if fiver[i]>max:
#        max=fiver[i]
# print(max)

#numbers = int(input(' input amount of numbers: '))
#count = 1
#arr = []
# while( count <= numbers):
#    num = int(input(f"input {count} number: "))
# arr.append(num)
#count += 1
#print (arr)
#max_num = arr[0]
# for i in arr:
#    if i > max_num:
#        max_num = i

#print(f' max number is: {max_num}')

#a=[1, 4, 8, 7, 5]
#print(max(1, 4, 8, 7, 5))


# a = int (input("введите a: "))
# b = int (input("введите b: "))
# c = int (input("введите c: "))
# d = int (input("введите d: "))
# e = int (input("введите e: "))

# m = a
# for i in b,c,d,e:
# if i>m: m=i
# print(m)

# a = int (input("введите a: "))
#b = int (input("введите b: "))
# if a*a == b or b*b==a:
#    print ("да")
# else:
#    print ("нет")

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('Input number: '))

# for i in range(-n,n+1):
#     print(i, end = " ")

# print("input number: ")

# value = int(input())

# print(list (range(-value, value+1)))

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

num = float(input("Input float number: "))
# if int((num*10) % 10) == 0:
#     print("No")
# else:
#     print(int((num*10) % 10))

result = int((num*10)%10)
if result == 0:
    print("No")
else:
    print(result)
# f = float(input())
# d = int((f*10) % 10)
# print(f, d, sep="->")

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int(input())
b = (n % 5 == 0 and n % 10 ==0 or n % 15 == 0) and not n % 30 == 0
print(n, b, sep=" -> ")
