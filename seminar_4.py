from random import randint
# some_list1 = [randint(0, 100) for _ in range(10)]
# min = some_list1[0]
# max = some_list1[0]
# for i in range(0, len(some_list1)):
#     if some_list1[i] > max:
#         max = some_list1[i]
#     if some_list1[i] < min:
#         min = some_list1[i]
# print(min, max, sep=' ')

# some_str = input('Введите числа')
# # int_list = some_str.split()
# int_list = list(map(int, some_str.split()))
# # Если не сделать преобразование инт, то сравнивается по первому символу.
# print(min(int_list))
# print(max(int_list))
# # for i in range(0, len(int_list)):
# #     int_list[i] = int(int_list[i])

import math

print('Найдите корни уравнения')
# a = int(input())
# b = int(input())
# c = int(input())
# d = b**2 - 4*a*c
# if d > 0: 
#     x1 = round(-b + math.sqrt(d))/(2*a)
#     x2 = round(-b - math.sqrt(d))/(2*a)
#     print(x1, x2, sep=' ')

# elif d == 0:
#     x1 = round(-b)/(2*a)
#     print(x1)
# else: 
#     print('Корней нет')

import sympy
a = int(input())
b = int(input())
c = int(input())
x = sympy.Symbol('x')
print(sympy.solveset(a*x**2 + b*x + c))

# a, b = map(int, input('Введите два числа: '))
# print(a, b, sep=' ')