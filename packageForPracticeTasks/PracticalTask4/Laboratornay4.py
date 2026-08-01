from packageForPracticeTasks import moduls

try:
    x1 = input('Введите x1(использовать ".") - начало отрезка:')
    x2 = input('Введите x2(использовать ".") - конец отрезка:')
    h = input('Введите h(использовать ".") - конец отрезка:')
    a = input('Введите a(использовать "."):')
    x1 = float(x1)
    x2 = float(x2)
    h = float(h)
    a = float(a)
except ValueError:
    print('Ошибка: неверный тип данных. Введите корректные данные.')
    exit()

h = moduls.tabul_sis(x1, x2, h, a)
print(h)
