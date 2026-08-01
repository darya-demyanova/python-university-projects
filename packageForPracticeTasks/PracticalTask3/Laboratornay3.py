from packageForPracticeTasks import moduls

try:
    x = input('Введите x(использовать "."):')
    y = input('Введите y(использовать "."):')
    a = input('Введите y(использовать "."):')
    x = float(x)
    y = float(y)
    a = float(a)
except ValueError:
    print('Ошибка: неверный тип данных. Введите корректные данные.')
    exit()

h = moduls.q(x, y, a)
print(h)