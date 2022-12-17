slovar = (['ivanov', 'Potter', 'Dobby'], ['Smitt', 'Lui', '135'], ['now', 'row', 'xxx'])
print(type(slovar))
ale = input('Введите строку')
for row in slovar:
    for el in row:
        if el == ale:
            print(row)