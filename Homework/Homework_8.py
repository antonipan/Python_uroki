import random as ran

print('Задача про ракеты')


def numberRocket():
    bukva = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = str(ran.randint(10, 99))
    num_rocket = bukva[ran.randint(0, len(bukva) - 1)] + '-' + number
    return num_rocket


def countRocket():
    n = int(input('Введите количество ракет: '))
    name_rockets = []
    for i in range(0, n):
        num_rocket = numberRocket()
        if num_rocket in name_rockets:
            while num_rocket in name_rockets:
                num_rocket = numberRocket()
                name_rockets.append(num_rocket)
        else:
            name_rockets.append(num_rocket)
    return name_rockets, n


def loading(n):
    loadings = []
    size = len(loadings)
    while size != n:
        xxx = ran.randint(0, 1001)
        if xxx % 50 == 0:
            loadings.append(xxx)
            size = len(loadings)
    return loadings


def distans(n):
    distantions = []
    for i in range(0, n):
        way = round(ran.uniform(0, 10), 1)
        distantions.append(way)
    return distantions


def loads(n):
    bukva = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name_load = []
    for i in range(0, n):
        x = bukva[ran.randint(0, len(bukva) - 1)]
        y = bukva[ran.randint(0, len(bukva) - 1)]
        z = bukva[ran.randint(0, len(bukva) - 1)]
        xyz = x + y + z
        name_load.append(xyz)
    return name_load


name_rockets, n = countRocket()
loadings = loading(n)
distantions = distans(n)
name_load = loads(n)
dict_rocket = {}
for i in range(0, n):
    dict_rocket[name_rockets[i]] = loadings[i], distantions[i], name_load[i]
    print(f'Ракета: {name_rockets[i]} (грузоподъёмность {loadings[i]}, дальность {distantions[i]}, груз {name_load[i]}')
print(f'Справочник ракет: {dict_rocket}')
