#  Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

print('Задача 1')
some_list1 = [1, 3, 5, 8, 3, 0, 2]
summa = 0
for index in range(0, len(some_list1)):
# for index in range(1, len(some_list1, 2))
    if index%2 != 0:
        summa += some_list1[index]
print(summa)

print('Задача 2')
# # Напишите программу, которая найдёт произведение пар чисел списка. 
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# print(len(some_list1))

multipl_list = []
# for index index range(0, (len(some_list1) - 1 // 2 + 1))
for index in range(0, len(some_list1)):
    if index < len(some_list1)/2:
        multi = some_list1[index] * some_list1[len(some_list1) - index-1]
        multipl_list.append(multi)
    else:
        break
print(multipl_list)

print('Задача 3')
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
from random import randint
# some_list2 = [randint(0, 10) for _ in range(4)]
# some_list2 = [float(input()) for _ in range(int(input()))]
some_list2 = [1.1, 1.2, 3.1, 5, 10.01]
fraction_list = []
# for index in range(0, len(some_list2)):
#     fraction = round(some_list2[index]%1, 3)
#     if fraction > 0: 
#         fraction_list.append(fraction)
# print(fraction_list)
# min = fraction_list[0]
# max = fraction_list[0]

# for i in range(0, len(fraction_list)):
#     if fraction_list[i] > max: 
#         max = fraction_list[i]
#     if fraction_list[i] < min: 
#         min = fraction_list[i]
# print(max - min)
minn = 1
maxx = 0
for el in some_list2:
    if '.' in el:
        if float('0.' + el.split('.')[1] < minn):
            minn = float

print('Задача 4')
# Приведите число в бинарный код
n = int(input('Введите любое число: '))
inv_binari = ''
while n > 0:
    ost = int(n%2)
    n = int(n/2)
    inv_binari += str(ost)
binari = ''
# print(inv_binari, len(inv_binari))
for i in range(len(inv_binari)-1, -1, -1):
    binari += inv_binari[i]
print(binari)