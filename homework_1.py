# from random import randint
# # Урок 1. Знакомство с Python
# # Задание №1
# # Напишите программу, которая принимает на вход цифру,
# # обозначающую день недели, и проверяет, является ли этот день выходным.
# print('Задача №1')
# number = int(input('Введите число от 1 до 7: '))
# if 0 < number < 8:
#     if number > 5:
#         print('Да, это выходной!')
#     else:
#         print('Будни(((')
# else:
#     print('Некорректное значение')

# day = int(input())
# day_name = {1: 'Понедельник',
#             2: 'Вторник',
#             3: 'Среда',
#             4: 'Четверг',
#             5: 'Пятница',
#             6: 'Суббота',
#             7: 'Воскресенье'}
# print(day_name.get(day, 'Такого дня недели не существует'))


# # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# print('Задача №2')

# count = 0
# for i in range(1, 101, 1):

#     x = bool(randint(0, 1))
#     y = bool(randint(0, 1))
#     z = bool(randint(0, 1))
#     print(bool(x), bool(y), bool(z))

#     result_left = (not (x and y and z))
#     result_right = (not x or not y or not z)
#     # print(result_right)
#     # print(result_left)
#     if result_left == result_right:
#         print('Значения совпадают')
#         count +=1
#     else:
#         break
# print(f'в {count} проверках из 100 - равенство выполняется')

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            some_str = not (x or y or z) == (not x and not y and not z)
            print(f'x = {x} y = {y} z = {z} -> {some_str}')

# # for i in range(0b111 + 1):
# #     binary_string = format(i, '03b')
# #     x = int(binary_string[0])
# #     y = int(binary_string[1])
# #     z = int(binary_string[2])
# #     print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} есть {not (x or y or z) == (not x) and (not y) and (not z)}')

# # Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# # номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# #
# # Пример:
# #
# # - x=34; y=-30 -> 4
# # - x=2; y=4-> 1
# # - x=-34; y=-30 -> 3
# print('Задача №3')

# a = input('Введите координаты точки A через запятую: ').split(',')
# x = int(a[0])
# y = int(a[1])
# if 0 != (x and y):
#     print ('Можем начинать')
#     if x > 0:
#         if y > 0:
#             print('Точка в 1-ой четверти')
#         else:
#             print('Точка в 4-ой четверти')
#     if x < 0 :
#         if y < 0:
#             print('Точка в 3-ой четверти')
#         else:
#             print('Точка в 2-ой четверти')
# elif (x or y) != 0:
#     print('Точка на оси. Четверть не определена')
# else:
#     print ('Точка в начале координа. Четверть не определена')

# print('Задача №4')

# # Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# x = int(input('Введите номер четверти: '))
# if 0 < x < 5:
#     if x == 1: print('Диапозон координат точки 0 < x; 0 < y')
#     if x == 2: print('Диапозон координат точки x < 0; 0 < y')
#     if x == 3: print('Диапозон координат точки x < 0; y < 0')
#     if x == 4: print('Диапозон координат точки 0 < x; y < 0')
# else:
#     print('Четверть не определена')


# # Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# #
# # Пример:
# #
# # - A (3,6); B (2,1) -> 5,09
# # - A (7,-5); B (1,-1) -> 7,21
# print('Задача №5')

# a = input('Введите координаты точки A через запятую: ').split(',')
# x1 = int(a[0])
# y1 = int(a[1])
# b= input('Введите координаты точки B через запятую: ').split(',')
# x2= int(b[0])
# y2 = int(b[1])
# distant = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# distant = round(distant, 3)
# print(distant)

import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
ac = y2 - y1
bc = x2 - x1
print(round((ac ** 2 + bc ** 2) ** 0.5, 2))
print(int(math.sqrt(ac ** 2 + bc ** 2) * 100) / 100)
print(str(math.sqrt(ac ** 2 + bc ** 2)).split('.')[0] + '.' + str(math.sqrt(ac ** 2 + bc ** 2)).split('.')[1][:2])
