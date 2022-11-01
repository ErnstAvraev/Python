# Больше предыдущего

# На вход программе подается строка текста из натуральных чисел.
# Из неё формируется список чисел. Напишите программу подсчета
# количества чисел, которые больше предшествующего им в этом списке
# числа, то есть, стоят вслед за меньшим числом.

# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами
# натуральных чисел.

# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка,
# больших предыдущего.

# Тестовые данные 🟢
# Sample Input 1:
# 1 2 3 4 5
# Sample Output 1:
# 4
# Sample Input 2:
# 1 1 3 2 2 1 1 1 1
# Sample Output 2:
# 1
# Sample Input 3:
# 5 4 3 2 1
# Sample Output 3:
# 0

# lst = list(map(int, input("Введите числа через пробел:\n").split()))

# count = 0
# for i in range(1, len(lst)):
#     if lst[i-1]<lst[i]:
#         count+=1

# print(count)

# # Транслитерация

alphabetE = \
    ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o',
     'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'i', '\'', 'e',
     'yu', 'ya', ',', '.', '!', '?', ' ']
alphabetR = \
    ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
     "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", ",", ".", "!", "?", " "]

base = input('Input word: ')
word = []

for i in range(len(base)):
    word.append(alphabetR.index(base[i]))
    index = word[i]
    print(alphabetE[index], end='')

# for i in range(len(base)):
#     print(base[i].replace(alphabetR[alphabetR.index(base[i])],alphabetE[alphabetR.index(base[i])]), end = '')

# # dictionary

# transleterate = \
#     {'a': "а", 'b': "б", 'v': "в", 'g': "г", 'd': "д", 'e': "е", 'yo': "ё", 'zh': "ж",
#      'z': "з", 'i': "и", 'y': "й", 'k': "к", 'l': "л", 'm': "м", 'n': "н", 'o': "о",
#      'p': "п", 'r': "р", 's': "с", 't': "т", 'u': "у", 'f': "ф", 'kh': "х", 'ts': "ц",
#      'ch': "ч", 'sh': "ш", 'shch': "щ", '': "ъ", 'i': "ы", '\'': "ь", 'e': "э",
#      'yu': "ю", 'ya': "я", ',': ",", '.': ".", '!': "!", '?': "?", ' ': " "}

# text = input('input text: ')

# for i in text:
#     print(transleterate[i], end="")

# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

# start_index = ord('а')
# title = 'Переводим этот текст, сейчас!'
# print(title.lower())

# slug = ""
# for s in title.lower():

#     if "а" <= s <= "я":
#         slug += t[ord(s) - ord('а')]

#     else:
#         slug += s



# print(slug)
