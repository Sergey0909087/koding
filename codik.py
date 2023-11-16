# # перебор строки
# word = 'hello'
# for char in word:
#     print(char)

# #конкатенация строк
# word = 'hello'
# print(word + 'hi')

# # нахождение длины строки
# word = 'hello'
# print(len(word))

# #проверка вхождения в строку
# word = 'pencil'
# if 'pen' in word:
#     print('YES')

# # умножение строки на число
# print('hello' * 3)

# индексация в строках
# s = 'PYTHON'
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print()
# print(s[-6])
# print(s[-5])
# print(s[-4])
# print(s[-3])
# print(s[-2])
# print(s[-1])
# s[6] # получим исключение

# s = 'abcdefg'
# print(s[0] + s[2] + s[4] + s[6])
# print(s[0] * 3 + s[-1] * 3 + s[3] * 2 + s[3] * 2)

# Итерация по индексам
# s = 'abcdef'
# for i in range(len(s)):
    # print(s[i])
# print()
# for c in s:
    # print(c)

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
    # print(s[i], end='')

# срезы строк
# s[начало среза : конец среза : шаг среза]
# s[x:y]

# s = 'abcdefghij'
# print(s[2:5])
# print(s[0:6])
# print(s[2:7])
# print(s[3:])
# print(s[:5])
# 
# print(s[-9:-4])
# print(s[-3:])
# print(s[:-3])
# 
# print(s[1:7:2]) # 3 символ количество шагов
# print(s[::-1])
# print(s[::-2])

# age = 15
# name ='Иван'
# print(f'Привет! меня зовут {name}, мне {age} лет.')

# Методы строк
# имя_обьекта.имя_метода(параметры)

# методы конвертации регистров
# capitalize - сделать заглавным
# swapcase - сменить регистр
# tittle - заголовок
# lower - нижний
# upper - верхний

# word = 'hELLo wORLD'
# print(word.capitalize())
# print(word.swapcase())
# print(word.title())
# print(word.lower())
# print(word.upper())
# print(word)


# методы поиска и замены
# count - считает количество фрагментов в целевой строке
# startswith - проверяет, начинается ли строка с указанных символов
# endswith - поверяет, оканчивается ли строка указанными символами
# find, rfind - возращает индекс первого вхождения фрагмента в строку
# index, rindex
# strip, lstrip, rstrip - удалить символ
# replace - заменить указанный символ на

# word = 'hello world'
# print(word.lower().count('l'))
# print(word.startswith('he'))
# print(word.endswith('rld'))
# print(word.find('o'))
# print(word.rfind('o'))
# print(word.index('o'))
# print(word.rindex('o'))
# word = '  hello world  '
# print(word)
# print(word.strip())
# print(word.lstrip())
# print(word.rstrip())
# print(word.replace('w', 'woooo'))
# print(word.replace('l', 'L'))

name = input('Введи свое имя: ')
familiya = input('Введи фамилию: ')
# print(name.lower(), familiya.lower())
print(f'Привет {name.title()} {familiya.title()}.')