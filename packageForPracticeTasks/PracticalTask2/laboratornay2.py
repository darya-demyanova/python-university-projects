from packageForPracticeTasks.PracticalTask2 import moduls

try:
    x = input('Введите x(использовать "."):')
    y = input('Введите y(использовать "."):')
    x = float(x)
    y = float(y)
except ValueError:
    print('Ошибка: неверный тип данных. Введите корректные данные.')
    exit()

if abs(x + y) == 0:
    print('Ошибка: деление на ноль. Введите корректные данные.')
    exit()
z, k, l, m, n = moduls.f(x, y)
print(z)
print(k)
print(l)
print(m)
print(n)