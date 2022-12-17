# # Второй вариант
# number_set = set()
# out_list = []
# some_list = list(map(int, input().split()))
# for ind in range(0, len(some_list)):
#     if some_list[ind] not in number_set:
#         number_set.add(some_list[ind])
#         for ind1 in range(ind + 1, len(some_list)):
#             if some_list[ind] == some_list[ind1]:
#                 break
#         else:
#             out_list.append(some_list[ind])
# print(out_list)
# for i in some_list:
#     if some_list.count(i) == 1:
#         print(i, end=' ')
# def even(i):
#     return i % 2 == 0


# some_list = [1, 2, 3, 4, 5, 6, 8]
# # new_list = list(filter(even, some_list))
# # Любой фильтр, любое правило.
# new_list = list(filter(lambda i: i % 2 == 0 , some_list))
# new_list = list(map(lambda i: i ** 2, some_list))

# print(new_list)

# number_list = [1, 2, 3, 4, 5]
# str_list = ['one', 'two', 'three', 'four', 'five']
# translate_list = {}
# print(zip(str_list, number_list))
# for i, j in zip(str_list[3:], number_list[2:]):
#     translate_list[j] = i
# print(translate_list)

# some_list = [10, 2, 33, 14, 5, 6, 8]
# for ind, el in some_list:
#     print(ind, el)
# print(list(enumerate(some_list)))

# Задача №35
data = open('../Lessons/natur.txt', 'r')
f = data.read()
some_list = list(map(int, f.split(' ')))
for i in range(1, len(some_list)):
    if some_list[i] - 1 != some_list[i - 1]:
        print(f'Отсутствует число {i + 1}')
data.close()



