# НОД Доп задание

# a = 50
# b = 130

# for i in range(a, 1, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break

# OR

# a = 72
# b = 130

# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#      #    print(a)
#     else:
#         b = b % a
#      #    print(b)

# print(a+b)

# # Решение Сергея
# # условия
# a = 20
# b = 58

# if a < b:
#      a, b = b, a
# while b!= 0:                #первое
#      a, b = b, a % b

# print(a)

# # Второе решение

# while a != b:
#      if a > b:
#           a -= b
#      else:
#           b -= a

# print(a)

# # Объявите анонимную(лямбда) функцию для определения вхождения в переданную ей 
# # строку фрагмента "plr". То есть, функция должна возвращать True, если такой
# # фрагмент присутствует в строке и False в противном случае.

# # Решение Максима

# f = lambda x: x.count('plr')>0
# print(f(''))

# # Решение Сергея

# print((lambda x: 'plr' in x)(input()))

# # второе

# contains = lambda s, sample = 'plr': sample in s
# s = input()
# print(contains(s))

