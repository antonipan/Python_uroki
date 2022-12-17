
#Проверить квадраты двух чисел.


# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))

# if num1**2 == num2 or num2**2 == num1:
#     print ('Да')

# else: 
#     print ('Нет')

# Разделить вводимые данные.
# some_set = input().split(', ') # Метод сплит.
# print(some_set)
# num1 = int(some_set[0])
# num2 = int(some_set[1])

# if num1**2 == num2 or num2**2 == num1:
#     print ('Да')

# else: 
#     print ('Нет')

# num1, num2 = map(int, input('Введите числа: ')) # Метод сплит.

# if num1**2 == num2 or num2**2 == num1:
#     print ('Да')

# else: 
#     print ('Нет')


# numbers = [0] * 5
# for _ in range(5): #Генерирует последовательность от 0 до 4.
#     n = int(input())
#     numbers.append(n)
# max = numbers[0]
# for el in numbers:
#     if el > max:
#         max = el
# print(max)

# print(max(numbers))

# max = int(input())
# for _ in range (4):
#     n = int(input())
#     if n > max:
#         max = n
# print(max)

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# num = int(input())
# for i in range(-num, num, +1):
#     print(i, end=', ')
# print(num)

# n = int(input())
# print(*list(range(-n, n + 1)), sep=', ')

#Ещё один вариант вывода
# num = int(input())
# some_str = ''
# for i in range(-num, num+1):
#     some_str *= str(i) + ', '
#     print(some_str[:-2])

# print(5, 6, 7, 8, sep='**', end='!')

# some_str = input()
# if ',' in some_str:
#     some_list = # index или split

#     some_str = input()
# if ',' in some_str:
#     ind = some_str.index(',')
#     print(some_str[ind + 1])
# else:
#     print('нет')


some_str = input()
if ',' in some_str:
    some_list = some_str.split(',')
    print(some_list[1][0])
else:
    print('нет')
