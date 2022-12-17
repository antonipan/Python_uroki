# Данные, модули, функции

# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# colors = ['green', 'blue', 'yellow', 'black', 'red']
# data = open('file.txt', 'a') # Путь к файлу и мод. Текстовая переменная.
# # data.writelines(colors) # Разделителей не будет
# data.write('\nLINE.121\n')
# data.write('LINE.131\n')

# data.close() # Разорвать связь файловой переменной с файлом на диске. 

# with open('file.txt', 'a') as data: # это может автоматически закрывать. Связываешь переменные с дата.
#     data.write('\nLINE.11\n')
#     data.write('LINE.33\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line) # считаем все строки
# data.close()

# ФУНКЦИИ

# Как разбить своё приложение, чтобы не было 1000 строк кода
# Упрощает программу, разбивает её на файлы
# import lesson_1 as l_1
# print(l_1.f(-1))


# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # TypeError missing 1 required ...
# print(new_string('', 8))

# def concatenatio(*params): # Неограниченное количество функций
#     res: str = "" # явно прописывается тип данных
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2

# def concatenatio(*params): # Неограниченное количество функций
#     res: int = 0 # явно прописывается тип данных
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# РЕКУРСИЯ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# # КОРТЕЖ
# a, b = 3, 4
# e = (3, 4, -2, 11, 40)
# print(e)
# print(e[3] + e[2])
# print(e)


# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
#     t[0] = 'black' # TypeError: 'tuple' object does not support item assignment

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться

# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

list1 = [1,2,4,56,8]
# list2 = list1

# for item in list1:
#     print(item)
# print()
# for item in list2:
#     print(item)

# list1 [0] = 123
# list2 [1] = 333
# print()
# for item in list1:
#     print(item)
# print()
# for item in list2:
#     print(item)

print(list1.pop(3))
print(f'элементов: {len(list1)}')
print(list1)
# print(list1.pop())
# print(f'элементов: {len(list1)}')
# print(list1.pop())
# print(f'элементов: {len(list1)}')
print(list1.insert(2, 11))
print(list1)
list1.append(13)
print(list1)