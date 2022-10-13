# #  Работа с файлами

# colors =['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('line11\n')
#     data.write('line22\n')


# exit()
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# # Функции и модули

# import lection as l

# print(l.f(1))


# def new_string(symbol, count=3):
#     return symbol*count
# print(new_string('!', 5) # !!!!!
# print(new_string('!'))   # !!!
# print(new_string(4))     # 12

# def concatenatio(*params):
#     res: str = ""
#     # res: int = 0
#     for item in params:
#         res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1'))  # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# # Реккурсия

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# # Кортежи

# t = ()
# print(type(t))  # tuple
# t = (1,)
# print(type(t))  # tuple
# t = (1)
# print(type(t))  # int
# t = (28, 9, 1990)
# print(type(t))  # tuple
# colors = ['red', 'green', 'blue']
# print(colors)   # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)        # ['red', 'green', 'blue']

# a = (3, 1, 41, 4) # не изменяемы список
# print(a)
# print(a[-2])
# a[0] =12
# a = (3,) # кортеж из одного элемента


# a = (3, 4, 5)
# for item in a:
#     print(item, end =" ")

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

# dictionary = {}
# dictionary = \
#     {
#         'up': '!',
#         'left': '<-',
#         'down': '|',
#         'right': '->'
#     }
#     # указание ключей
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys(): # ключи
#     print(k)
# for k in dictionary.values(): # значения
#     print(k)
# for v in dictionary: # keys
#     print(v)
# for v in dictionary:
#     print(dictionary[v]) # values


# Множества (set)


# colors = {'red', 'green', 'blue'}
# print(colors)       # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)       # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors)       # {'green', 'blue', 'gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors)       # {'green', 'blue', 'gray'}
# colors.clear()      # { }
# print(colors)       # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()            # c = {1, 2, 3, 5, 8} копирование множества
# u = a.union(b)          # u = {1, 2, 3, 5, 8, 13, 21} объединение
# i = a.intersection(b)   # i = {8, 2, 5} пересечения множеств
# dl = a.difference(b)    # dl = {1, 3} разница а от б
# dr = b.difference(a)    # dr = {13, 21} разница б от а

# q = a \
#     .union(b) \
#     .difference(a.intersection(b)) # {1, 21, 3, 13} объединение уникальных элементов множества

# print(a)
# print(b)
# print(c)
# print(u)
# print(i)
# print(dl)
# print(dr)
# print(q)

# #  не изменяемые множества
# s = frozenset(a)

# Списки

# list1 = [1,2,3,4,5]
# list2 = list1

# list1[0] = 123
# list2[-1] = 321
# for e in list1:
#     print(e, end=' ')

# print()

# for e in list2:
#     print(e, end=' ')

# print(list1)
# print(list1.pop()) # удаляет последний элемент списка
# print(list1)
# print(list1.pop(2)) # удаляет выбранный элемент списка
# print(list1)
# print(list1.insert(2, 11)) # добавляет на нужную позицию элемент
# print(list1)
# print(list1.append(12)) # добавляет элемент в конец списка
# print(list1)