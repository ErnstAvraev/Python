# 1.        Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел 
# в одну строчку через пробел.

# data = list(map(int, input("Input list of numbers dividing by space: \n").split()))
# res = list(filter(lambda x: True if 9 < x < 100 else False, data))
# print(res)

# # Sergei's solution

# print(*filter(lambda x: len(str(abs(int(x)))) == 2, input("input list of numbers dividing by space: ").split()))

# # 2.        Дан список, вывести отдельно буквы и цифры.

# inp_string = list(map(str, input('Введите строку: ').split()))
# result_digits = [i for i in inp_string if i.isdigit() == True]
# result_letters = [i for i in inp_string if i.isdigit() == False]
# print(result_digits, '\n', result_letters)

# # Sergei's solution

# a = ("a", "b", "2", "3", "c")
# b = ('a','b','c')
# c = ('1','2','3')

# b = filter(str.isalpha, a)
# c = filter(str.isdigit, a)

# print(*b)
# print(*c)

# 3. Преобразовать набора списков 
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор 
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# result = list(zip(users, ids, salary))
# print(result,'\n')

# new_users = [i[0] for i in result]
# new_ids = [i[1] for i in result]
# new_salary = [i[2] for i in result]
# print(new_users,'\n',new_ids,'\n',new_salary,'\n')

# # Sergei's solution

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# a,b,c = map(list,zip(users,ids,salary))
# print(a,b,c, sep = "\n")
# a,b,c = map(list,zip(a,b,c))
# print(a,b,c, sep = "\n")

# Решение Максима

users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

for i in zip(users, ids, salary):
    print(i)

users_1, ids_1, salary_1 = map(list, zip(*zip(users,ids,salary)))

print(users_1,ids_1,salary_1, sep='\n')