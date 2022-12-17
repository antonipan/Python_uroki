import view
import export
import imported


def buttomclick():
    mode = int(input('Выберите режим работы: 1 - импорт, 2 - экспорт '))
    if mode == 1:
        find_str = view.view_import()
        row = imported.impoter(find_str)
        view.view_import_out(row)
    elif mode == 2:
        some_list = view.view_export()
        export.expotrer(some_list)
    else:
        print('Попробуйте ещё раз!')
