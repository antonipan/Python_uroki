# print('Hello World')

# ПЕРЕМЕННЫЕ

# # Переменные пишутся без типа переменных
# c = None

# a = 123
# b = 1.23

# # print(type (a))

# # Значение None позволяет не присваивать переменной значения.

# c = 'princ datcky'

# # функция type позволяет увидеть в терминале тип переменной.
# # print(type(c))


# # Одинарными кавычками пишем строку и символ. Можно обрамлять двойные кавычки.

# # print (c) # - так пишется комментарий.


# value = "hello \"world\" "

# # print(value)

# # Интерполяция

# print (a, b, c)
# print (a, '-', b, '-', c)
# print ('{} - {} - {}'.format(b,c,a))
# print (f'{a} - {b} - {c}')

# f = False
# print(f)

# МАССИВЫ И СПИСКИ

# list = []
# print(list)

# list = [1,2,3,4]
# print(list)

# list = ['1',2,3,'kot', True] # Лучше так не делать. Переменные одного типа
# # Пробел может поломать программу
# print(list)

# ВВОД И ВЫВОД

# print - вывод. input - ввод

# print ('Введите a')
# a = float(input())
# print ('Введите b')
# b = float(input())

# print (a, b)
# # print(f'{a}, {b}')
# # Типизация динамическая, поэтому по умолчанию мы работаем со строками.
# # Для этого нужно использовать тип данных от инпут.
# print(a, ' ', b, ' ', '=', a+b)

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ

# + - / * 
# a = +23 # Унарный плюс, обычно не пишется.
# b = 7 # Унарный минус -7
# c  = b+a
# print(c)

# d = a-b
# print(d)
# print(d*c)
# print(c/b) # Деление. Если с остатком то дробь
# print(c%b) # Остаток
# print(c**b) # С вовзодится в степень б
# # Нет ограничения по храненю данных 
# x = 1.3123335513451
# y = 3
# print(x*y) # Особенность хранения
# z = round(x*y, 4) # Огругление. По умолчанию округляет по математическим правилам.
# print(z)
# Сокращённые операции присваивания

# a = 5
# a += 5
# print(a)
# b = 4
# b -= 1
# print(b)

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ < > <= >= == != ^ | &

# a = 1 > 4
# print(a)
# a = 1 !=2
# print(a)
# d = 'eug' # в списках идёт сравнение по элементно. 
# c = 'eug'
# print(c == d)

# b = 3
# a = 1 < 3 > 5 # Тройное неравенство
# print(a)

# f = 1 < 2 and 4 > 5 # and = or in 
# print(f)
# m = [1,2,3,4,5]
# print(2 in m) # Два содержится в списке m
# print(not 2 in m) # Два содержится в списке m

# is_odd = not m[3] % 2
# print(is_odd)

# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ
# Соблюдаем отступы

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура! Это Маша')
# elif username == 'Марина':
#     print('А это Марина')
# else:
#     print('Привет, ', username)

# ЦИКЛЫ

# value = 14
# inverted = 0
# while value != 0:
#     value -= 1
#     inverted +=10
#     print(value)
# else:
#     print('Пожалуй, хватит')
# print(inverted)

# list1 = {1,5,3,4}
# for i in list1:
#     print(i**2)

# # От нолика до 9. итератор.
# r = range(5, 10, 7)
# for i in r:
#     print(i)


# РАБОТА СО СТРОКАМИ
text = 'Хорошая сегодня погода! Не правда ли?'
# print(len(text))
# print('a' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('Не', 'ЕЩЁ' ))
# print(text)

# help(text.capitalize)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)

# СПИСКИ

# numbers = [1,2,3,4,5]
# ran = range(1,3)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(numbers)
# numbers[0] = 10
# print(numbers)
# print(f'{len(numbers)} len')
# for i in range(0, 3):
#     i *= 2
#     print(i)

# text = "Это не те дроиды, которых вы ищет"
# new_text = ""
# for char in enumerate(text):
#     if char[0] % 5 == 0:
#         new_text += '*'
#     else:
#         new_text += char[1]
# print(new_text)
# Можно добавить или убрать из списка элемент.

def f(a):
    if a < 1:
        return 'Celoe'
    elif a == 2.3:
        return 23
    else:
        return

# arg = -4

# print(f(arg))
# print(type(f(arg)))
