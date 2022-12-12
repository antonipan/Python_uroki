# # # Энумерейт
print('Задача №1')
key = int(input('Введите число недели: '))
day_name = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
week = dict(enumerate(day_name, start=1))
print(week[key])

# # # # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # # # Пример:
# # # # - 6782 -> 23
# # # # - 0,56 -> 11
print('Задача №2')
# # # str_vvod = input('Введите любое вещественное число: ' )
# # # # str_res = str_vvod.replace('.' and ',', '' )
# # # str_res = ''
# # # for i in str_vvod:
# # #     # print(i)
# # #     if i == '.' or i == ',':
# # #         i = ''
# # #         str_res += i
# # #     str_res += i
# # # # print(str_res)
# # # res: int = 0
# # # for i in str_res:
# # #     res += int(i)
# # # print(res)
# # # лист компрехеншен
n = input('Найдём сумму элементов вещественного числа: ')
summa = sum(int(el) for el in n if el != '.')
print(summa)



print('Задача №3')
# # n = int(input('Введите любое число: ' ))
# # mark = []
# # sum = 0
# # for i in range(1, n+1):
# #     sum = sum + round((1+1/i)**i)
# #     mark.append(sum)
# #     print(f'{i}: {sum} ')
# # print(mark)
n = int(input('Введите любое число: ' ))
f = lambda x: round((1+1/x)**x)
mark = [(1, f(i)) for i in range(1, n+1)]
print(mark)

print('Задача 4')
some_list1 = [1, 3, 5, 8, 3, 0, 2]
# some_list1 = list(filter(lambda x: x%2 != 0, some_list1))
# # summa = 0
# # for index in range(0, len(some_list1)):
# # # for index in range(1, len(some_list1, 2))
# #     if index%2 != 0:
# #         summa += some_list1[index]
# # print(summa)
some_list1 = list(filter(lambda x: x%2 != 0, some_list1))
print(sum(some_list1))


# # Не доделал
print('Задача №5')
some_list2 = [1.1, 1.2, 3.1, 5, 10.01]
some_list2 = list(map(str, some_list2))
print(some_list2)
som = []
some_list2 = [i.split('.') for i in some_list2 if i [:1] not in some_list2]
print(some_list2)