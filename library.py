import json


lib = dict()
a = ''
with open("data.json", "r", encoding="utf-8") as file:
    lib = json.load(file)
while a != '0':
    print('===========T-библиотека===========\n\
           1 добавить книгу\n\
           2 настройки книги\n\
           3 моя библиотека\n\
           4 прочитанные книги\n\
           5 любимые книги\n\
           0 выход')
    a = input()
    if a == '1':
        print('Две одинаковые книги по названию добавить нельзя :(')
        b = input('Введите название: ')
        c = input('Введите автора: ')
        d = input('Введите кр. описание: ')
        e = 0
        f = 0
        lib.update({b: [c, d, e, f]})
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(lib, file)
    elif a == '3':
        for i in lib:
            print(f'название {i}' + ('✔' if lib[i][2] % 2 == 1 else ''),  ('✨' if lib[i][3] % 2 == 1 else ''), f" \n\
    автор {lib[i][0]}\n\
    кр. описание {lib[i][1]}\n ")
        input('Для продолжения нажмите Enter...')
    elif a == '2':
        c = 0
        b = input('Введите название книги для поиска: ')
        while True:
            if b not in lib:
                print('Такой книги нет в библиотеке. Введите заново')
                b = input('Введите название книги для поиска: ')
            else:
                while c != '0':
                    c = input('Выберите действие:\n\
        1 удалить книгу\n\
        2 пометить как прочитанную\n\
        3 пометить как избранную\n\
        0 вернуться\n')
                    if c == '1':
                        del lib[b]
                    elif c == '2':
                        lib[b][2] += 1
                    elif c == '3':
                        lib[b][3] += 1
                    elif int(c) < 0 or int(c) > 3:
                        input('Введите корректное действие. Нажмите Enter')
                break
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(lib, file)
    elif a == '4':
        for i in lib:
            if lib[i][2]:
                print(i, '-', lib[i][0])
    elif a == '5':
        for i in lib:
            if lib[i][3]:
                print(i, '-', lib[i][0])
