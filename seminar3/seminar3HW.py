# # 1. Задайте список из нескольких чисел. Напишите программу,
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

# # Добавил решение с одной строкой
# def sum(arr):
#      sum = 0
#      for i in range(len(arr)):
#           sum += arr[i]
#      return sum
# arr = list(map(int, input().split()))
# res = [arr[i] for i in range(len(arr)) if i % 2 != 0]
# print(sum(res))

# # Решение Максима

# def elements_sum(array=[], sum=0):
#      if len(array)>1:
#           return sum + array[1] + elements_sum(array[2:], sum)
#      else:
#           return sum

# numbers_list = list(map(int, input().split()))
# print(f'\n The sum of the elements on the odd position is: {elements_sum(numbers_list)}')

# # Решение Сергея

# my_list = [8, 5, 7, 3, 6]
# # my_list = list(map(int, input().split()))
# print(sum(my_list[1::2]))

# a=[1,2,3,4,5]
# x=a[::-1] # разворот списка
# print(x)

# # 2. Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний
# # и т.д.
# # Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]


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

# # Решение Максима


# def elements_sum(array=[], result_array: list = []):
#      if len(array) >= 2:
#         result_array.append(array[0]*array[-1])
#         return elements_sum(array[1:-1], result_array)
#      else:
#           if len(array) == 1:
#                result_array.append(array[0] **2)
#           return result_array

# numbers_list = list(map(int, input('Enter a list of numbers separated by space: ').split()))
# print(f'{numbers_list} => {elements_sum(numbers_list)}')

# # Решение Сергея

# import random
# b = int(input('Введите кол-во чисел в списке for 2# = '))
# list_b = list(random.randint(0, 10) for i in range(b))
# print(list_b)
# proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b % 2)))
# print(proiz_b)

# # 3. Задайте список из вещественных чисел. Напишите программу,
# # которая найдёт разницу между максимальным и минимальным
# # значением дробной части элементов.
# # Пример:
# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

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

# # Решение Максима

# def get_fractional_value(list):
#      array = []
#      for i in range(len(numbers_list)):
#           temp_list = numbers_list[i].rsplit('.', 1)
#           if len(temp_list) > 1:
#                array.append(temp_list[1])
#      for i in range(len(array)):
#           if len(array[i]) == 1:
#                array[i] = array[i] + '0'
#      return array

# numbers_list = input('Enter a list of numbers separated by a space: ').split()
# fract_value_list = get_fractional_value(numbers_list)
# print(f'{max(fract_value_list)} - {min(fract_value_list)} = 0.{int(max(fract_value_list)) - int(min(fract_value_list))}')


# # Решение Сергея

# list = [1.1, 1.2, 3.1, 5, 10.01]
# mix_list = []

# for i in list:
#      mix_list.append(round(i-int(i), 2))

# print(list, end = ' => ')
# print(max(mix_list) - min(mix_list))

# # 4. Напишите программу, которая будет преобразовывать десятичное
# # число в двоичное.
# # Пример:
# # - 45 -> 101101
# # - 3 -> 11
# # - 2 -> 10

# s = " "
# n = int(input("Input a number to convert to binary: \n"))
# while n != 0:
#     s = str(n % 2)+s
#     n //= 2
# print(s)

# # Решение Максима

# def to_binar(number, array: list = []):
#      number = int(number)
#      if number == 0:
#           array.append(0)
#           return array
#      if number == 1:
#           array.append(1)
#           array.reverse()
#           return array
#      if number % 2 == 0:
#           array.append(0)
#           return to_binar(number/2, array)
#      else:
#           array.append(1)
#           return to_binar((number-1)/2, array)

# number = int(input('Input number: '))
# print(f'your number ({number}) in binary system = {to_binar(number)}')


# # Решение Сергея

# num = int(input("Input number: "))
# binum = ''

# while num:
#      binum = str(num%2) + binum
#      num//=2
# print(binum)

# # Второе решение Сергея(как у меня)

# a = int(input('input number = '))
# b = ''
# while a != 0:
#      b += str(a%2)
#      a = a//2
# print(b)

# # 5. Задайте число. Составьте список чисел Фибоначчи, в том числе
# # для отрицательных индексов.
# # Пример:
# # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def fib(n):
#      if n in [1,2]:
#           return 1
#      else:
#           return fib(n-1)+fib(n-2)

# def negaFib(n):
#      return ((-1)**(n+1))*fib(n)

# n = int(input("Введите порядковый номер числа = "))
# fibArr1 = []
# fibArr2 = []
# for e in range(1,n+1):
#      fibArr1.append(negaFib(e))
# for a in range(1,n+1):
#      fibArr2.append(fib(a))

# fibArr1.reverse()
# fullArr= fibArr1+fibArr2

# print(fullArr)

# # Решение Максима

# def nega_fibonacci(numb):
#      array = [1, 0, 1]
#      for i in range (1, numb):
#           array.insert(0, array[1] - array[0])
#           array.append(array[-2] + array[-1])
#      return array

# num = int(input('input number: '))
# print(nega_fibonacci(num))

# # Решение
# import math
# b = abs(int(input('input number: ')))
# kod = []
# for i in range(-b,b+1):
#      kod.append(i)
# for i in range(-b-2, -len(kod)-1, -1):
#      kod[i] = kod[i+2] - kod[i+1]
# for i in range(b+2, len(kod),1):
#      kod[i] = kod[i-2] + kod[i-1]
# print(kod)

