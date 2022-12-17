
print('Задача №1')
n = input('Введите число: ')
decimal = input('Введите десятичную дробь: ').split('.')
decimal = '0' * len(decimal[1])
# print(decimal)
n = n + '.' + decimal
print(n)

print('Задача №2')
n = int(input('Введите число: '))
pros_list = []
multi_list = []
for i in range(1, n+1):
    pros_list.append(i)
# print(pros_list)
c = 2
while c < n: 
    for j in range(0, len(pros_list)):
        if pros_list[j]%c == 0 and pros_list[j]/c > 1:
            pros_list [j] = 0
    c = c +1      
# print(pros_list)
# print('Задача №2')
# print(17/9 == 0)
pros_list = set(pros_list)
pros_list.remove(0)
print(pros_list)
for i in pros_list:
    if n%i == 0: 
        multi_list.append(i)
print(f'Простые множители: {multi_list} числа {n}')


print('Задача №3')

from random import randint

input_list = [randint(0, 20) for _ in range(int(input('Введи число элементов: ')))]
print(input_list)
out_list = []
check_list = []
for i in range(1, len(input_list)):
    for j in range(0, len(input_list)):
        if input_list[i] == input_list[j]:
            input_list [i] = randint(0, 20)
            i = j  
print(input_list)


print('Задача №4')
    
k = int(input('Введите степень: '))
list_koff = []
equation = ''
for i in range(0, k+1):
    x = randint(0, 100)
    list_koff.append(x)
print(list_koff)
j = 0
for i in range(k, -1, -1):
    if i == 0:
        equation += str(list_koff[j])
        equation += ' = 0'
    elif i == 1:
        equation += str(list_koff[j])
        equation += 'x + '
    else:
        equation += str(list_koff[j])
        equation += f'x*{i} + '
    j += 1
print(equation)

data = open ('../Lessons/file_equ.txt', 'w')
data.write(equation)
data.close()


            


    
