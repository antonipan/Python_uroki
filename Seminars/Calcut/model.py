def some_sign(some_str):
    some_list = some_str.split()
    a = int(some_list[0])
    b = int(some_list[2])
    oper = some_list[1]
    return a, b, oper
