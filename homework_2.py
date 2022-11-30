# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # - 6782 -> 23
# # - 0,56 -> 11
# print('Задача №1')
# # str_vvod = input('Введите любое вещественное число: ' )
# # # str_res = str_vvod.replace('.' and ',', '' )
# # str_res = ''
# # for i in str_vvod:
# #     # print(i)
# #     if i == '.' or i == ',':
# #         i = ''
# #         str_res += i
# #     str_res += i
# # # print(str_res)
# # res: int = 0
# # for i in str_res:
# #     res += int(i)
# # print(res)
# n = input()
# summa = 0
# for el in n: 
#     if el != '.':
#         summa += int(el)
# print(summa)



# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# print('Задача №2')
# num = int(input('Введите любое число: ' ))
# list = []
# element = 1
# for index in range (1, num+1):
#     element *= index
#     list.append(element) 
# print(list)


# # Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# # Пример:
# # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# # Реализуйте алгоритм перемешивания списка.
# print('Задача №3')
# n = int(input('Введите любое число: ' ))
# mark = []
# sum = 0
# for i in range(1, n+1):
#     sum = sum + round((1+1/i)**i)
#     mark.append(sum)
#     print(f'{i}: {sum} ')
# print(mark)

print('Задача №4')
# m = int(input('Введите любое число: ' ))
# place = []
# for i in range(1,m+1):
#     place.append(i)
# print(place)
# print()
from random import randint
# p = len(place)
# for i in range(p):
#     j = randint(0, p-1)
#     element = place.pop(j)
#     place.append(element)
# print(place)

import random
some_list = [1, 2, 3, 4, 5, 6]
random.shuffle(some_list)
print(some_list)

