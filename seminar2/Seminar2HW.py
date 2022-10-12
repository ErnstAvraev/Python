# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = (input())
arr = [a for a in str(n)]
print(arr)
sum = 0
for i in range(len(arr)+1):
    sum += i
print(sum)
