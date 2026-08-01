import math
from packageForPracticeTasks import moduls

eps = 1e-10
m_iter = 10


try:
    a=float(input('Введите x1(использовать ".") - Начало интервала:'))
    b=float(input('Введите x2(использовать ".") - Конец интервала:'))
    print(f"Максимальное приближение {eps}")
    print(f"Максимальное количество итераций {m_iter}")
    if a<0 or b>math.pi or a>=b:
        raise ValueError("Производная равна нулю")
    root =moduls.newton_method(a,b, eps, m_iter)
except Exception as e:
    print(f"Ошибка:{e}")