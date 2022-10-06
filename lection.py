# типы данных и переменная
# int, float, boolean, str, list, None
from errno import ESHLIBVERS
import numbers


value = None
a = 123
b = 1.23
print(a)
print(b)
value = 12334
print(type(value))
s = 'hello world'
print(s)
str = 'hello \nworld'
print(str)  # вывод строки

print(a, '-', b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)

list = ['1', '2', '3', 'hello', 1, 2, 3, 1.2, True]
col = [1, 2, 3, 4, 5]
print(list)
print(col)

# input
print('Введите а')
a = int(input())  # для ввода можно присвоить тип данных
print('Введите b')
b = int(input())
print('{} {}'.format(a, b))
print(f'{a} {b}')
print(a, '+', b, '=', a+b)

# арифметические операции
# +, -, *, /, %, //, **

a = 1.33414
b = 3
#c = a+b
#c = a-b
#c = a*b
#c = a/b
#c = a%b
#c = a//b
c = round(a*b, 5)
print(c)

a = 3
a += 3
#a *= 3
print(a)


a = 1 > 4
#a = 1!=4
print(a)

a = 1 < 3 < 5 < 10
print(a)

func = 1
t = 4
x = 123

print(func < t > (x))

f = 1 > 2 or 4 < 6
print(f)
f = [1, 2, 3, 4]
print(f)
print(not 2 in f)

is_odd = not f[0] % 2
print(is_odd)

# if
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждал вас, Марина')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)

# while

original = 23
inverted = 0
# while original != 0:
#inverted = inverted*10+(original % 10)
#original //= 10
# print(inverted)

# while-else

while original != 0:
    inverted = inverted*10+(original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

# for

for i in 1, 2, 3, 4, 5:
    print(i**2)
list = [1, 2, 3, 4, 10, 5]
for i in list:
    print(i**2)
for i in range(1, 10, 2):
    print(i)

text = 'съешь еще этих мягких французских булок'
print(len(text))
print('еще' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('еще', 'ЕЩЕ'))

help(text.istitle)
print(text[0])
print(text[1])
print(text[-5])


numbers = [1, 2, 3, 4, 5]
print(numbers)
ran = range(1, 6)
print(type(ran))
numbers = list(ran)
print(type(numbers))

print(numbers)
numbers[0] = 10

# def


def f(x):
    if x == 1:
        return 'целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 2.3
print(f(arg))
