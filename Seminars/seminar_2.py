print('Задача №11')

# print('Задача №11')
#
# num = int (input())
# for i in range(0,num-1):
#     print((-3) ** i, end=', ')
# print((-3)**(num-1))

print('Задача №13')

# num = int (input())
# slovar = {}
# for i in range(1,num+1):
#     slovar [i] = 3*i+1
# print(slovar)

print('Задача №13')

user_str = 'От топота копыт пыль по полю летит'
str_find = input()

print(user_str.count(str_find) or str_find.count(user_str))

s1 = input()
s2 = input()
if s1 < s2:
    s2, s1 = s1, s2
ind = 0
c = 0
while ind < len(s1):
    if s1[ind: ind + len(s2)] == s2:
        c += 1
        ind += len(s2)
    else:
        ind += 1
print(c)

