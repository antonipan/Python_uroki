# def press(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             ind = 0
#             count = 1
#             while ind < len(inp_str) - 1:
#                 if inp_str[ind] == inp_str[ind + 1]:
#                     count += 1
#                 else:
#                     if count == 1:
#                         res.write(inp_str[ind])
#                     else:
#                         res.write(str(count) + inp_str[ind])
#                     count = 1
#                 ind += 1

# def depress(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             count = ''
#             for letter in inp_str:
#                 if letter.isdigit():
#                     count += letter
#                 else:
#                     if not count:
#                         res.write(int(count) * letter)
#                     else:
#                         res.write(letter)
#                     count = ''
# # some_dict = {}
# # N = int(input())
# # for _ in range(N):
# #     line = input()
# #     some_dict[line.split()[0]] = line.split()[1:]

# # M = int(input())
# # some_list = [input() for _ in range(M)]

# # for word in some_list:
# #     if word.lower() in some_dict:
# #         print(*some_dict[word])
# #     else:
# #         print('Нет в словаре')


# def arifmetic_operation(operation):
#     if operation == '+':
#         return lambda x, y: x + y
#     elif operation == '-':
#         return lambda x, y: x - y
#     elif operation == '*':
#         return lambda x, y: x * y
#     else: 
#         return lambda x, y: x / y

# operation = arifmetic_operation('/')
# print(operation(5, 2))

some_list = list(filter(lambda x: x % 9 == 0, range(10, 100)))
print(some_list)
some_list = list(map(lambda x: x ** 2, some_list))
print(some_list)
print(sum(some_list))