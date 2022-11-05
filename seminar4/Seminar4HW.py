# # 1. Задача №30: Вычислить число c заданной точностью d. Пример:
# # при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)



# from math import pi

# d = float(input("Введите число заданной точности d для числа Пи: \n"))
# count = 0
# newD = d
# while newD!=1:
#     newD*=10
#     count+=1
# print(f'число Пи с заданной точностью {d} равно {round(pi, count)}')

# #                 Решение с семинара

# # for i in range(-10,0): print(10**i, round(pi, -i), sep =' ->')
# i = int(input("Введите кол-во знаков после запятой от 1 до 10: "))
# while i<1 or i>10:
#     i = int(input("Введите кол-во знаков после запятой от 1 до 10: "))
# else:
#     print(10**-i, round(pi, i), sep = ' ->')



# # 2. Задайте натуральное число N. Напишите программу, которая составит
# # список простых множителей числа N.



# num = int(input("Введите число: "))
# i = 2
# lst = []
# temp = num
# while i <= temp:
#     if temp % i == 0:
#         lst.append(i)
#         temp //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {num} -> {lst}")

# #                     Решение с семинара

# def simple(a):
#     k = 0
#     for i in range(2, a// 2+1):
#         if(a % i == 0):
#             k += 1
#     if(k <= 0):
#         return True
#     else:
#         return False

# N = int(input("Input number: "))
# prime_factors = list()
# i = 2
# while N != 1:
#     if N % i == 0 and simple(i) == True:
#         N /= i
#         prime_factors.append(i)
#     else:
#         i += 1
# print(*prime_factors, sep = "*")

# #                     Решение Сергея

# n = int(input("Введите число N: "))
# i = 2 
# list = []

# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")



# # 3. Задайте последовательность чисел. 
# # Напишите программу, которая выведет список неповторяющихся элементов 
# # исходной последовательности.



# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# #                 Решение с семинара

# numbers = list(map(int, input("Input numbers using space: ").split()))
# print(numbers)
# new_numbers = []
# for i in numbers:
#     if i not in new_numbers:
#         new_numbers.append(i)
# print(new_numbers)

# # Решение Сергея

# def elements(nums):
#     nums = [int(i) for i in nums.split()]
    # return list(set(nums))  # set функция выводит все уникальные элементы

# numbers = input()
# print(elements(numbers))

#           Второе решение Сергея с исключением повторяющихся

# b = list(map(int, input("input numbers using space: ").split()))
# a = []
# for i in b:
#     if b.count(i) == 1:
#         a.append(i)

# print(a)



# # 4. Задана натуральная степень k. 
# # Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# # многочлена и записать в файл многочлен степени k. 
# # Пример:
# # k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



# import random

# def write_file(st):
#     with open('fileSem4HW.txt', 'w') as data:
#         data.write(st)

# def rnd():
#     return random.randint(0,101)

# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))

# #                    Решение с семинара

# k = int(input("input power: "))
# koeff = 100
# from random import randint
# while k > 0:
#     if k > 1:
#         print(f'{randint(1,100)}x^{k}', end = ' + ')
#     k-=1
#     if k == 1:
#         print(f'{randint(1,100)}x', end = ' + ')
#     if k == 0:
#         print(randint(1, 100), end = ' = 0')

# #                   Решение Сергея

# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}x^{k}')
#     flag = randint(0, 1)
#     if flag == 1:
#         ans.append(' + ')
#     elif flag == 0:
#         ans.append(' - ')
#     k -= 1

# ans.pop(-1)
# ans.append(' = 0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()



# #         5. Даны два файла, в каждом из которых находится запись многочлена. 
# #         Задача - сформировать файл, содержащий сумму многочленов.



# import random

# def write_file(name,st):
#     with open(name, 'w') as data:
#         data.write(st)

# def rnd():
#     return random.randint(0,101)

# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    
# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# def sq_mn(k):
#     if 'x^' in k:
#         i = k.find('^')
#         num = int(k[i+1:])
#     elif ('x' in k) and ('^' not in k):
#         num = 1
#     else:
#         num = -1
#     return num

# def k_mn(k):
#     if 'x' in k:
#         i = k.find('x')
#         num = int(k[:i])
#     return num

# def calc_mn(st):
#     st = st[0].replace(' ', '').split('=')
#     st = st[0].split('+')
#     lst = []
#     l = len(st)
#     k = 0
#     if sq_mn(st[-1]) == -1:
#         lst.append(int(st[-1]))
#         l -= 1
#         k = 1
#     i = 1 
#     ii = l-1 
#     while ii >= 0:
#         if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
#             lst.append(k_mn(st[ii]))
#             ii -= 1
#             i += 1
#         else:
#             lst.append(0)
#             i += 1     
#     return lst
    
# k1 = int(input("Введите натуральную степень для первого файла k = "))
# k2 = int(input("Введите натуральную степень для второго файла k = "))
# koef1 = create_mn(k1)
# koef2 = create_mn(k2)
# write_file("file_1.txt", create_str(koef1))
# write_file("file_2.txt", create_str(koef2))

# with open('file_1.txt', 'r') as data:
#     st1 = data.readlines()
# with open('file_2.txt', 'r') as data:
#     st2 = data.readlines()
# print(f"Первый многочлен {st1}")
# print(f"Второй многочлен {st2}")
# lst1 = calc_mn(st1)
# lst2 = calc_mn(st2)
# ll = len(lst1)
# if len(lst1) > len(lst2):
#     ll = len(lst2)
# lst_new = [lst1[i] + lst2[i] for i in range(ll)]
# if len(lst1) > len(lst2):
#     mm = len(lst1)
#     for i in range(ll,mm):
#         lst_new.append(lst1[i])
# else:
#     mm = len(lst2)
#     for i in range(ll,mm):
#         lst_new.append(lst2[i])
# write_file("file_res.txt", create_str(lst_new))
# with open('file_res.txt', 'r') as data:
#     st3 = data.readlines()
# print(f"Результирующий многочлен {st3}")

# # Решение Сергея

# ffile1 = open('file1.txt', 'r')
# ffile2 = open('file2.txt', 'r')
# ffile3 = open('file3.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):  # решение верное для многочленов одинаковой длины
#     if file1[i-1] != '^':
#         if file1[i].isnumeric():
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close

# Еще одно от Сергея

import random
def nmnogochlen1(a=random.randint(1,100), b=random.randint(0, 100), c=random.randint(0,100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res

def nmnogchlen2(a=random.randint(1,100), b=random.randint(0,100), c=random.randint(0,100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res

f = open('dz40.txt', 'w')
f.write(nmnogochlen1())
print(nmnogochlen1())
f.close

f = open('dz41.txt', 'w')
f.write(nmnogchlen2())
print(nmnogchlen2())
f.close()

f = open('dz40.txt', 'r')
list_5 = str(f.readline()).split('x')
c1 = b1 = a1 = 0
if len(list_5) == 3:
    c1 = list_5[2][1:]
if len(list_5) >= 2:
    b1 = list_5[1][3:-1]
a1 = list_5[0][:-1]
f.close()

f = open('dz41.txt', 'r')
list_51 = str(f.readline()).split('x')
c2 = b2 = a2 = 0
if len(list_51) == 3:
    c2 = list_51[2][1:]
if len(list_51) >= 2:
    b2 = list_51[1][3:-1]
a2 = list_51[0][:-1]
f.close()

f = open('dz42.txt', 'w')
f.write(nmnogochlen1(int(a1)+ int(a2), int(b1)+ int(b2), int(c1)+ int(c2)))

print(nmnogochlen1(int(a1)+int(a2), int(b1)+int(b2), int(c1)+int(c2)))