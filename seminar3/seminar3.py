#  Задача 1. Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла,
# а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество
# подряд выпавших Решек.

# Формат входных данных
# На вход программе подается строка текста, состоящая из букв
# русского алфавита "О" и "Р".

# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число
# 0
# 0.

# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31

# def countInLines(randomLine):
#     count = 0
#     countRow = 0
#     for i in range(len(randomLine)):
#         if inputLine[i] == "Р" or inputLine[i] == "р":
#             count += 1
#             if count > countRow:
#                 countRow = count
#         elif inputLine[i] != "Р" or inputLine[i] != "р":
#             count = 0
#     print(f"Количество выпавших подряд решек = {countRow}")


# inputLine = input("Введите результат выпадения монеты: ")

# countInLines(inputLine)

#  Задача 2. Искусственный интеллект Антон, созданный Гилфойлом,
# взломал сеть умных холодильников. Теперь он использует их в
# качестве серверов "Пегого дудочника". Помогите владельцу фирмы
# отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая
# из строчных букв и цифр, и если в ней присутствует слово "anton"
# (необязательно рядом стоящие буквы, главное наличие
# последовательности букв), то холодильник заражен и нужно вывести
# номер холодильника, нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число n
# n – количество холодильников. В последующих
# n строках вводятся строки, содержащие латинские строчные буквы
# и цифры, в каждой строке от до 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через
# пробел. Если таких холодильников нет, ничего выводить не нужно.

# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8

# n = int(input())
# arr1 = []
# for i in range(0, n):
#     arr1.append(i)
# print(arr1)

# searchName = ["a","n","t","o","n"]

# for i in arr1:
#     arr1[i] = str(input())
#     count = 0
#     for j in searchName:
#         for k in arr1[i]:
#             if k == j:
#                 count+=1
#                 break
#     if count >=5:
#         print('infected')
#     else:
#         print('not infected')

# # черновик
# searchName = ["a","n","t","o","n"]

# count = 0
# for i in searchName:
#     for j in n:
#         if j == i:
#             count+=1
#             break
# if count >=5:
#     print('infected')
# else:
#     print('not infected')


# # Решение преподавателя: 

# s = input()
# t = 0
# while "Р"*(t+1) in s:
#     t += 1
# if t != 0:
#     print(t)
# else:
#     print(0)

# # anton 
# l =list()
# la = 'anton'
# for i in range(int(input())):
#     l.append(input())
# for i in l:
#     for j in i:
#         if len(la) == 0:

#             if j == la[0]:
#                 la = la[1:]
#     if len(la) == 0:
#         print(i)

# n=int(input())
# f=[]
# hacker = ['a', 'n', 't', 'o', 'n','']
# count=0
# otvet=[]


# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

s = list(input())
num = int(input())
for word in s:
    if str(num) in word:
        print("Yes")
    else:
        print("No")