# def f(x):
#     x**2


# g = f
# print(type(f))
# print(g(1))
# print(f(1))


# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# def calc1(x):
#     return x+10

# # print(calc1(10))

# def calc2(x):
#     return x*10

# # print(calc2(10))

# def math(op,x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x,y):
#     return x+y

# f = sum

# sum = lambda x, y: x+y + 1 # тоже самое, что и функция сверху

# def mult(x,y):
#     return x*y

# def calc(op, a, b): # в качестве переменной может быть функция
#     print(op(a,b))
#     # return op(a,b)

# calc(mult, 4, 5)
# calc(sum, 4, 5)
# calc(lambda x, y: x+y, 4, 5)  # одноразовая функция
# f

# #                     List Comprehension

# 1: [exp for item in iterable]        # for  в какаом то итерируемом объекте
# 2: [exp for item in iterable(if conditional)]
# 3: [exp <if conditional> for item in iterable(if conditional)]

# 1:
# list = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)

# print(list)

# # упрощенная запись в одну строку того, что сверху
# list = [i for i in range(1, 21)]
# print(list)

# list = [i for i in range(1, 21) if i % 2 == 0]  # однострок с условием
# print(list)

# list = [(i, i) for i in range(1, 21) if i % 2 == 0]  # список кортежей
# print(list)


# def f(x):
#     return x**3


# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# path ='/Users/ernstavraev/Desktop/Python/Lesson3/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))  # стандартный код
#     data = data[space_pos+1:]


# out = []
# for e in numbers:
#     if not e %2:
#         out.append((e, e**2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# data = '1 2 3 5 8 23 38'.split() # прописаный список

# res = select(int, data)
# res = where(lambda x: not x%2, res)     # с использованием лямбды и лист компрехеншн
# res = select(lambda x: (x, x**2),res)
# print(res)


#                   map


# li = [x for x in range(1, 20)]
# print(li)
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int,input().split()))
# print(data)
# data = list(map(int, '1 2 3 4 55 6'.split())) # итератор map

# for e in data:
#     print(e)
# print('--')

# for e in data:
#     print(e)

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()                 #Правка задачки с использованием map

# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# data = [x for x in range(10)]

#               filter
# 
# 
#  res = list(filter(lambda x: x % 2 ==0, data))
# print(res)

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#               zip, enumerate
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# data = list(zip(users, ids, salary))
# # data = list(enumerate(ids))
# print(data)