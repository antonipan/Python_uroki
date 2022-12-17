def view_export():
    family = input('Введите фамилию: ')
    name = input('Введите имя: ')
    fatherly = input('Введите отчество: ')
    is_who_it_you = input('Кем он вам приходится: ')
    phone = input('Введите телефон: ')
    person = [family, name, fatherly, is_who_it_you, phone]
    return person


def view_import():
    find_str = input('Кого вы хотите найти?  ')
    return find_str

def view_import_out(data):
    print(data)