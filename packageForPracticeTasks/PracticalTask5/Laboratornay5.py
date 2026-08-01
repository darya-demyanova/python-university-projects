import time

from packageForPracticeTasks import moduls
from packageForPracticeTasks.PracticalTask2.moduls import save_to_excel, save_to_word

try:
    xa = input('Введите xa(использовать "."):')
    ya = input('Введите ya(использовать "."):')
    xb = input('Введите xb(использовать "."):')
    yb = input('Введите yb(использовать "."):')
    xc = input('Введите xc(использовать "."):')
    yc = input('Введите yc(использовать "."):')
    xd = input('Введите xd(использовать "."):')
    yd = input('Введите yd(использовать "."):')
    xa = float(xa)
    ya = float(ya)
    xb = float(xb)
    yb = float(yb)
    xc = float(xc)
    yc = float(yc)
    xd = float(xd)
    yd = float(yd)
except ValueError:
    print('Ошибка: неверный тип данных. Введите корректные данные.')
    exit()

start_time = time.time()

res = moduls.Pram(xa, ya, xb, yb, xc, yc, xd, yd)
for i in res:
    print(i)

end_time = time.time()
calc_time = end_time - start_time

save_to_excel(res, 'Ploshad_pram.xlsx')
save_to_word(res, calc_time, 'Ploshad_pram.docx')

print(res)
print(calc_time)

