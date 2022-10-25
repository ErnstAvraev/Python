# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = (input("Введите число: "))
# arr = [a for a in str(n)]
# print(arr)
# sum = 0
# for i in range(len(arr)+1):
#     sum += i
# print(sum)


# Решение Гаи

# print(sum([int(i) for i in input("Input number: ") if i.isdigit()]))

# numb = float(input())
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

# from curses.ascii import isdigit


# s= input()
# summ = 0
# for i in s:
#     if i.isdigit():
#         summ+=int(i)
# print(summ)

# # 2. Напишите программу, которая принимает на вход число N
# #  и выдает набор произведений чисел от 1 до N.
# # Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input("Введите число: "))
# arr = []
# elem = 1
# for i in range(1,num+1):
#     elem *=i
#     arr.append(elem)
# print(arr)

# # 3. Задайте список из n чисел последовательности
# # $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# # Пример:
# # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Введите число n: "))
# dic = {}
# for i in range(1,n+1):
#     dic[i] = 3 * i + 1

# print(dic)

# Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

# import random

# N = int(input("Введите число N: "))
# arr = []
# for i in range(-N, N+1):
#     arr.append(i)
# print(arr)

# random.shuffle(arr)
# print(arr)

# another solutions:
# 1

# user_range_num = int(input("smth: "))
# user_pos_1 = int(input("Input position 1 number: "))
# user_pos_2 = int(input("Input position 2 number: "))

# path = "file.txt"
# data = open("file.txt", "w")
# list = []
# product = 1

# for i in range(-user_range_num, user_range_num+1):
#     list.append(i)
# print(list)

# for i in range(1, user_range_num*2+2):
#     i = str(i)
#     data.write("\n")
#     data.write(i)
# data.close()

# 2

# numN = int(input("Input number N: "))
# list = []
# for i in range(-numN, numN+1):
#     list.append(i)
# print(list)
# position1 = int(input("input position 1: "))
# position2 = int(input("input position 2: "))
# print(f"multiplication of numbers = {list[(position1-1)]*list[(position2-1)]}")

# 3




# import random



# n = int(input('input number: '))
# list = []
# for i in range(n):
#     a = random.randint(-n,n)
#     list.append(a)
# print(list)
# index_list = input(f'input position from 1 to {n} using space: ').split()
# result = 1
# for j in range(len(index_list)):
#     a = int(index_list[j])-1
#     print (f'{result}*{int(list[a])}', end = ' ')
#     result *= int(list[a])
# print(f'= {result}')