import random
# print('Задача №17')

# n = int (input())
# some_list = [random.randint(-n, n) for _ in range(n)] #Правило задания списка
# mult = 1
# print(some_list)
# with open ('file.txt', 'w', encoding='utf-8') as file:
#     count = random.randint(1, n)
#     for _ in range (count):
#         file.writelines(f'{random.randint(1, n-1)}' + '\n')
#         print(count)
# with open ('file.txt', 'r', encoding='utf-8') as file:
#     index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * some_list[int(index)]
# print (mult)

# print('Задача №2')

# n = int(input('Введите число'))
# some_list = []
# with open ('file_str.txt', 'w', encoding='utf-8') as data:
#     for _ in range(n):
#         data.writelines(input('Строка: ') + '\n')
# print()

# simvol = input()

# with open ('file_str.txt', 'r', encoding='utf-8') as data:
#     strings = data.read().splitlines()
#     count = 1
#     for line in strings:
#         if simvol in line: 
#             print(f'Символ {simvol} найден в {count}-ой строке' )
#         count +=1
#     if not b:
#         print('no')
        

# print('Задача №3')

# def mounth (x, y):
#     listEn = ['Jan', 'Fa', 'Ma', 'Apr', 'My', 'Ju', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
#     listRus = ['Ян', 'Фев', 'Мар', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
#     if 0 < x < 13:
#         if y == 'en':
#             return listEn[x-1]
#         if y == 'ru':
#             return listRus[x-1]
#     else:
#         return print('Некорректный ввод')
        
        