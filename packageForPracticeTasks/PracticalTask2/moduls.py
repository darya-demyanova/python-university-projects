import os.path
from math import *
import math
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import os
import openpyxl
import pandas as pd
from openpyxl import Workbook
from docx import Document
import sqlite3
import random
import csv
import pickle
import shelve
from tabulate import tabulate


def f(x, y):
    z1 = round(((3.14/2) - sqrt(2*x) - ((x + y**2)/(0.75*tan(abs(x+y)))))*1000)/1000
    z = 'Вывод значения z =' + str(z1)
    k = 'Целая часть результата (неявно) К =' + str(round(z1))
    l = 'Целая часть результата (явно) L =' + str(int(z1))
    m = 'Округление в большую сторону =' + str(ceil(z1))
    n = 'Округление в меньшую сторону =' + str(floor(z1))
    return z, k, l, m, n

#------------------------------------

def y1(x, y, a):
    mini = a**x
    if y**x < mini:
        mini = y**x
    if math.exp(x+a) < mini:
        mini = math.exp(x+a)
    x1 = mini
    maxi = (math.log(x))**2
    if (sin(abs(x+a)))**2 > maxi:
        maxi = (sin(abs(x+a)))**2
    if a > maxi:
        maxi = a
    x2 = maxi
    h = a + x1 + x2
    return h
def y2(x, y, a):
    maxi = x
    if y > maxi:
        maxi = y
    xx = maxi
    mini = xx
    if y**2 < mini:
        mini= y**2
    h = mini
    return h
def y3(x, y, a):
    h = (a + x**2 + y**2)/(10-x)
    return h

def q(x, y, a):
    if (x > 0) and (x < 8) and (y > 3):
        print('Тест 1 ветки')
        return y1(x, y, a)
    elif (x <= -0.5) and (y <= -3):
        print ('Тест 3 ветки')
        return y2(x, y, a)
    else:
        if x == 10:
            print('Ошибка: деление на ноль. Введите корректные данные')
        else:
            print('Тест 2 ветки')
            return y3(x, y, a)

# ----------------------------------------

def create_bd():
    """Создает базу данных и таблицу, если они не существуют."""
    try:
        conn = sqlite3.connect('Sis_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                t TEXT NOT NULL,  
                y REAL NOT NULL
            )
        ''')
        conn.commit()
        print("База данных и таблица успешно созданы.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании базы данных: {e}")
    finally:
        if conn:
            conn.close()

def insert_into_db(t, y):
    """Вставляет данные в базу данных."""
    try:
        conn = sqlite3.connect('Sis_data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Sis_results (t, y) VALUES (?, ?)", (str(t), y)) # Преобразуем t в строку
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при вставке данных: {e}")
    finally:
        if conn:
            conn.close()

def sis(x, a):
    """
    Вычисляет результат кусочно-ломанной функции.
    :param x: Число, для которого вычисляется кусочно-ломанная функция.
    :return: Значение кусочно-ломанной функции.
    """
    if x > a:
        y = x * (sqrt(x - a))**2
    elif x == a:
        y = x * sin(a*x)
    else:
         y = exp(-a*x) * cos(a*x)
    return y

def tabul_sis(x1, x2, h, a):
    """
    Табулирует кусочно-ломанной функции и записывает результат в текстовый файл, Exel, Word.
    :param x1: Начало отрезка.
    :param x2: Конец отрезка.
    :param h: Шаг.
    """
    print(f"{'x':>10} | {"y" :>10}")
    print("-" * 23)
    with open ('sis_table.txt', 'w') as txt_file:
        txt_file.write(f"{'x':>10} | {"y" :>10}\n")
        txt_file.write("-" * 23 + "\n")

        wb = Workbook()
        ws = wb.active
        ws.title = "Sis_Table"
        ws.append(["x", "y"])



        doc = Document()
        doc.add_heading("Sis_Table", level = 1)
        table = doc.add_table(rows = 1, cols = 2)
        table.style = "Table Grid"
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'x'
        hdr_cells[1].text = 'y'

        n = round((x2 - x1)/h + 1)
        p = x1
        mini = 1000000
        maxi = -1000000
        sum = 0
        max_x = None
        min_x = None
        for x in range (1, n+1):
            sis_x = sis(p, a)
            print(f"{p:10.1f} | {sis_x:10.5f}")
            txt_file.write(f"{p:10.5f} | {sis_x:10.5f}\n")
            ws.append([p, sis_x])
            row_cells = table.add_row().cells
            row_cells[0].text = f'{p:.1f}'
            row_cells[1].text = f'{sis_x:.5f}'


            if sis_x < mini:
                mini = sis_x
                min_x = p
            if sis_x > maxi:
                maxi = sis_x
                max_x= p
            if sis_x < 0:
                sum += sis_x
            p += h

        ws.append([""])
        ws.append(['Макс.', maxi, 'при x', max_x])
        ws.append(['Мин.', mini, 'при x', min_x])
        ws.append(['Сум.', sum])

        txt_file.write('\n' + '-'*23 + '\n')
        txt_file.write(f"Maksimum y: {maxi:.5f} pri x = {max_x:.1f}\n")
        txt_file.write(f"Minimum y: {mini:.5f} pri x = {min_x:.1f}\n")
        txt_file.write(f"Summa otricatelnix znacheniy: {sum:.5f}\n")

        doc.add_paragraph(f"Максимум y: {maxi:.5f} при x = {max_x:.1f}")
        doc.add_paragraph(f"Минимум y: {mini:.5f} при x = {min_x:.1f}")
        doc.add_paragraph(f"Сумма отрицательных значений: {sum:.5f}")

        wb.save("Sis_Table.xlsx")
        doc.save("Sis_Table.docx")
    conn = sqlite3.connect('Sis_data.db')
    texts = ['Минимальное значение', 'Максимальное значение', 'Сумма отрицательных значений']
    dop = [mini, maxi, sum]
    for text, i in zip(texts, dop):
        insert_into_db(text, i)
    conn.commit()
    conn.close()

    print(f"Максимум y: {maxi:.5f} при x = {max_x:.1f}")
    print(f"Минимум y: {mini:.5f} при x = {min_x:.1f}")
    print(f"Сумма отрицательных значений: {sum:.5f}")
    print('\nТаблица сохранена в файлы: "sis_table.txt", "Sis_table.xlsx", "Sis_Table.docx". Данные записаны в базу данных. ')


# ----------------------------------------

def Pram(xa, ya, xb, yb, xc, yc, xd, yd):
    S1 = abs(xa - xb) * abs(ya - yb)
    S2 = abs(xc - xd) * abs(yc - yd)
    return ({"n": f"({xa}, {ya}), ({xb}, {yb})", "Ploshad": S1},
            {"n": f"({xc}, {yc}), ({xd}, {yd})", "Ploshad": S2})

def save_to_excel(res, file_name):
    """
    Сохраняет результаты в Excel.
    :param res: список с результатами
    :param file_name: имя файла Excel
    """
    df = pd.DataFrame(res)
    df.to_excel(file_name, index = False)
    print(f"Данные сохранены в Excel: {file_name}")

def save_to_word(res, calc_time, file_name):
    """
    Сохраняет результаты в Word.
    :param res: список с результатами
    :param calc_time: время выполнения программы
    :param file_name: имя файла в Word
    """
    doc = Document()
    doc.add_heading("Результаты расчёта", level=1)
    doc.add_paragraph(f"Время выполнения программы: {calc_time:.3f} секунд" )
    table = doc.add_table(rows = 1, cols = 2)
    table.style = 'Table Grid'
    table.rows[0].cells[0].text = 'Точки'
    table.rows[0].cells[1].text = 'Площадь'

    c = 0
    for i in res:
        c += 1
        row_cells = table.add_row().cells
        row_cells[0].text = str(i['n'])
        row_cells[1].text = f"{i['Ploshad']:.5f}"

    print(f"\nВремя выполнения программы: {calc_time:.5f} секунд")
    doc.save(file_name)
    print(f"Данные сохранены в Word: {file_name}")

# ----------------------------------------

def fx(x):
    return exp(-x) - x**2
def dfx(x):
    return -(exp(-x)) - 2 * x
def log_iteration_to_file(file_name, iter, x, f_x, df_x):
    """
    Функция для записи данных об одной итерации в файле
    :param file_name: Имя файла
    :param iter: Номер итерации
    :param x: Текущее значение х
    :param f_x: Значение функции f(x)
    :param df_x: Значение производной f'(x)
    """
    with open(file_name, "a") as file:
        file.write(f"{iter:10} | {x:12.10f} | {f_x:12.10f} | {df_x:12.10f}\n")

def log_iteration_to_excel(file_name, iter, x, f_x, df_x):
    """
    Функция для записи данных об одной итерации в Excel
    :param file_name: Имя файла
    :param iter: Номер итерации
    :param x: Текущее значение х
    :param f_x: Значение функции f(x)
    :param df_x: Значение производной f'(x)
    """
    try:
        workbook = Workbook.load_workbook(file_name)
        sheet = workbook.active
    except FileNotFoundError:
        workbook = Workbook.Workbook()
        sheet = workbook.active
        sheet.append(["Итерация", "x", "f(x)", "f'(x)"])
    sheet.append([iter, x, f_x, df_x])
    workbook.save(file_name)

def newton_method(x1, x2, tol, m_iter, file_name ="newton_iterations.txt", file_name2 = "newton_itertions.xlsx"):
    """
    Функция для расчета методом Ньютона
    :param x1: Начало интервала
    :param x2: Конец интервала
    :param tol: Значение максимального приближения
    :param m_iter: Значение максимального количества итераций
    :param file_name: Имя файла
    :param file_name2: Имя файла в Excel
    """
    with open(file_name, "w") as file:
        file.write(f"{'Итерация':>10} | {'x':>12} | {'f(x)':>12} | {'f\'(x)':>12}\n")
        file.write("-" * 70 + "\n")

    iter = 0
    x_new = (x1 + x2) / 2

    print(f"{'Итерация':>10} | {'x':>12} | {'f(x)':>12} | {'f\'(x)':>12}")
    print("-" * 70)

    while iter <= m_iter:
        x = x_new
        fu = fx(x)
        pr = dfx(x)
        if pr == 0:
            print ('Производная равна нулю')
        x_new = x - fu / pr
        iter += 1

        log_iteration_to_file(file_name, iter, x_new, fu, pr)
        log_iteration_to_excel(file_name2, iter, x_new, fu, pr)
        print(f"{iter:10} | {x_new:12.10f} | {fu:12.10f} | {pr:12.10f}")

        if abs(x_new - x) < tol:
            print(f"\nКорень найден за {iter} итераций.")
            with open(file_name, "a") as file:
                file.write(f"\nКорень найден за {iter} итераций: x = {x_new:.10f}\n")
            log_iteration_to_excel(file_name2, "Результат", x_new, fx(x_new), "-")
            return x_new


#----------------------------------------------------------------------


def generate_list(size, min_val, max_val):
    """ Генерирует список случайных чисел."""
    rezult = []
    for _ in range(size):
        rezult.append(random.randint(min_val, max_val))
    return rezult

def minim_chet(lst):
    mini = 1000000000000
    for x in lst:
        if x % 2 ==0 and x < mini:
            mini = x
    return mini

def filter_list(lst, chet_minim):
    result = []
    for index, x in enumerate(lst):
        if x > chet_minim:
            result.append(index)
    return result

#----------------------------------------------------------------------

def create_bd2():
    connection = sqlite3.connect("students.bd")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        math INTEGER,
        physic INTEGER
    )
    """)
    cursor.execute("DELETE FROM students")
    students_data = [
        ("Миронова Софья", 67, 69),
        ("Петрова Таисия", 94, 98),
        ("Коршунов Никита", 74, 55),
        ("Богомолов Александр", 58, 43),
        ("Нестерова Милана", 81, 82),
        ("Кузнецова Татьяна", 75, 45),
        ("Карпов Егор", 66, 76)
    ]
    cursor.executemany("INSERT INTO students (name, math, physic) VALUES (?, ?, ?)", students_data)
    connection.commit()
    connection.close()

def get_students_from_bd():
    connection = sqlite3.connect("students.bd")
    cursor = connection.cursor()
    cursor.execute("SELECT name, math, physic FROM students")
    students = [{"name": row[0], "math": row[1], "physic": row[2]} for row in cursor.fetchall()]
    connection.close()
    return students

def find(students):
    rez_spisok = []
    for student in students:
            if student["math"] > minim(students) or student["physic"] > minim(students):
                rez_spisok.append(student)
    return rez_spisok

def minim(students):
    min_score = 101
    for student in students:
        if student["math"] < min_score and student["math"] % 2 == 0:
            min_score = student["math"]
        if student["physic"] < min_score and student["physic"] % 2 == 0:
            min_score = student["physic"]
    return min_score

def save_to_excel2(rez_spisok):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Оценка выше минимальной чётной"
    sheet.append(["Студент", "Математика", "Физика"])
    for student in rez_spisok:
        sheet.append([student["name"], student["math"], student["physic"]])
    workbook.save("Spisok.xlsx")
    print("Результаты сохранены в файл Excel")

#---------------------------------------------------------------------

def save_to_world2(students,rez_spisok):
    doc = Document()
    doc.add_heading("Список студентов", level = 1)
    for student in students:
        doc.add_paragraph(f"{student ['name']} - Математика: {student ['math']}, Физика: {student ['physic']}")

    doc.add_heading("Студенты, у которых oценка выше минимальной чётной")
    for student in rez_spisok:
        doc.add_paragraph(f"{student['name']}, {student['math']}, {student['physic']}")

    doc.save("Списки в Word.docx")
    print("Результаты сохранены в файл Word")

def save_to_pdf(students):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("Arial", "", os.path.join("C:\\Windows\\Fonts", "arial.ttf"), uni = True)
    pdf.set_font("Arial", size=12)

    pdf.cell(200,10, "Список студентов", ln = True, align = 'C')
    pdf. ln(5)
    for student in students:
        pdf.cell(200, 10, f"{student ['name']} - Математика: {student ['math']}, Физика: {student ['physic']}", ln = True)

    pdf.output("Списки.pdf")
    print("Результаты сохранены в файл PDF")

def save_to_csv(original_list, filtered_list):
    with open ("students_list.csv", mode = 'w', newline = '', encoding = 'utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(["Исходный список студентов"])
        for student in original_list:
            writer.writerow([student["name"], student["math"], student["physic"]])

        writer.writerow([])
        writer.writerow(["Студенты, у которых oценка выше минимальной чётной"])
        for student in filtered_list:
            writer.writerow([student["name"], student["math"], student["physic"]])
    print("Результаты сохранены в students_list.csv")

def diagram_student(students):
    names = [student["name"] for student in students]
    math_scores = [student["math"] for student in students]
    physics_scores = [student["physic"] for student in students]
    x = np.arange(len(names))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, math_scores, width, label = 'Математика')
    rects2 = ax.bar(x + width / 2, physics_scores, width, label='Физика')

    ax.set_xlabel("Студенты")
    ax.set_ylabel("Оценки")
    ax.set_title("Оценки студентов по предметам")
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation = 45, ha='right')
    ax.legend()

    plt.tight_layout()
    plt.show()



def calculate_pandas(csv):
    """
    Вычисляет средний рост мужчин и женщин с использовнием Pandas
    """
    df = pd.read_csv(csv)
    avg_male = df["Male Height in Cm"].mean()
    avg_female = df["Female Height in Cm"].mean()
    return avg_male, avg_female

def calculate_no_pandas(csv_file):
    """
    вычисляет средний рост мужчин и женщин без использования Pandas
    """
    male_heights = []
    female_heights = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if ('Male Height in Cm' in row and
                    'Female Height in Cm' in row and
                    row['Male Height in Cm'].replace('.', '', 1).isdigit() and
                    row['Female Height in Cm'].replace('.', '', 1).isdigit()):
                male_height = float(row['Male Height in Cm'])
                female_height = float(row['Female Height in Cm'])
                male_heights.append(male_height)
                female_heights.append(female_height)
    avg_male = sum(male_heights) / len(male_heights) if male_heights else 0
    avg_female = sum(female_heights) / len(female_heights) if female_heights else 0
    return avg_male, avg_female

def filter_pandas(csv):
    """
    фильтрует страны, где средний мужской рост составляет 175–179 см, используя Pandas.
    """
    df = pd.read_csv(csv)
    df["Male Height in Cm"] = pd.to_numeric(df["Male Height in Cm"], errors="coerce")
    filtered_df = df[(df["Male Height in Cm"] >= 175) & (df["Male Height in Cm"] <= 179)]
    return filtered_df[["Rank", "Country Name", "Male Height in Cm"]]

def filter_no_pandas(csv_file):
    """
    фильтрует страны, где средний мужской рост составляет 175–179 см, не используя Pandas.
    """
    result = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            male_height_str = row.get('Male Height in Cm', '')
            if (male_height_str.replace('.', '', 1).isdigit() and
                    male_height_str.count('.') <= 1):
                male_height = float(male_height_str)
                if 175 <= male_height <= 179:
                    result.append({
                        'Rank': row.get('Rank', ''),
                        'Country Name': row.get('Country Name', ''),
                        'Male Height in Cm': male_height
                    })
    return result

def find_shortest(csv_file):
    """
    находит страны с самым низким средним ростом мужчин и женщин без использования Pandas
    """
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    shortest_male = min(data, key=lambda x: float(x["Male Height in Cm"]))
    shortest_female = min(data, key=lambda x: float(x["Female Height in Cm"]))
    return shortest_male["Country Name"], shortest_female["Country Name"]

def find_shortest_pandas(csv_file):
    """
    находит страны с самым низким средним ростом мужчин и женщин с использованием Pandas
    """
    df = pd.read_csv(csv_file)
    shortest_male = df.loc[df['Male Height in Cm'].idxmin()]
    shortest_female = df.loc[df['Female Height in Cm'].idxmin()]
    male_country = shortest_male['Country Name']
    female_country = shortest_female['Country Name']
    print(f"Страна с самым низким мужчиной: {male_country} ({shortest_male['Male Height in Cm']:.2f} cm)")
    print(f"Страна с самой низкой женщиной: {female_country} ({shortest_female['Female Height in Cm']:.2f} cm)")
    return male_country, female_country
#--------------------------------------------------


def generate(n, m):
    """
    Cоздает вложенную последовательность размером n×m со случайными числами
    """
    return [[i + j for j in random.sample(range(35), m)] for i in random.sample(range(45), n)]

def print_matr(matrica):
    """
    выводит последовательность в отформатированном виде с выравниванием чисел по правому краю в колонках шириной 3 символа
    """
    for row in matrica:
        for num in row:
            print(f" {num:3d} ", end=" ")
        print()

def find_max_positive_column(matrix):
    """
    находит индекс столбца матрицы с максимальной суммой положительных элементов
    """
    max_sum = -1
    max_col = -1
    for j in range(len(matrix[0])):
        col_sum = sum(num for row in matrix for num in [row[j]] if num > 0)
        if col_sum > max_sum:
            max_sum = col_sum
            max_col = j
    return max_col


def create_filtered_array(mas, column_num):
    """
    создает список из всех элементов входной матрицы, которые больше заданного значения column_num
    """
    filtered_array = []
    for n in mas:
        for num in n:
            if num > column_num:
                filtered_array.append(num)

    return filtered_array

#--------------------------------------------------
def save_to_file7(filename, matrix, max_col, new_array):
    """
    Запись последовательности и результатов в блокнот
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Исходная последовательность:\n")
        for row in matrix:
            file.write(" ".join(f"{num:3d}" for num in row) + "\n")
        file.write(f"\nСтолбец с макс. суммой положительных: {max_col}\n")
        file.write("\nЭлементы > номера столбца:\n")
        file.write(" ".join(f"{num:3d}" for num in new_array) + "\n")

def save_to_binary6(filename, matrix, max_col, new_array):
    """
    Запись последовательности и результатов в бинарный файл
    """
    data = {"matrix": matrix, "max_positive_column": max_col, "filtered_elements": new_array}
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def load_from_binary6(filename):
    """
    Загрузка данных из бинарного файла
    """
    with open(filename, "rb") as file:
        data = pickle.load(file)
    return data['matrix'], data['max_positive_column'], data['filtered_elements']

def save_to_shelve6(filename, matrix, max_col, filtered_array):
    """
    Сохраняет в shelve-файл:
    """
    with shelve.open(filename) as db:
        db["matrix"] = matrix
        db["max_positive_column"] = max_col
        db["filtered_elements"] = filtered_array

def load_from_shelve6(filename):
    """
    Загрузка данных из shelve-файла
    """
    with shelve.open(filename) as db:
        matrix = db.get("matrix", [])
        max_col = db.get("max_positive_column", 0)
        filtered = db.get("filtered_elements", [])
    return matrix, max_col, filtered

def save_to_excel7(filename, a, max_col, filtered):
    """
    Запись данный в Excel-файл
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Matrix"

    for i in range(len(a)):
        for j in range(len(a[i])):
            ws.cell(row=i + 1, column=j + 1, value=a[i][j])

    ws.cell(row=len(a) + 2, column=1, value="Столбец с макс. суммой положительных:")
    ws.cell(row=len(a) + 2, column=2, value=max_col)
    ws.cell(row=len(a) + 3, column=1, value="Отфильтрованные элементы:")

    for idx, val in enumerate(filtered, start=1):
        ws.cell(row=len(a) + 3, column=idx + 1, value=val)

    wb.save(filename)


def save_to_sqlite7(db_name, a, max_col, filtered):
    """
    Запись данных в БД SQLite
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS matrix")
    cursor.execute("CREATE TABLE matrix (row_data TEXT)")

    for row in a:
        row_str = ",".join(map(str, row))
        cursor.execute("INSERT INTO matrix (row_data) VALUES (?)", (row_str,))

    cursor.execute("DROP TABLE IF EXISTS results")
    cursor.execute("CREATE TABLE results (max_column INTEGER, filtered_data TEXT)")

    filtered_str = ",".join(map(str, filtered))

    cursor.execute("INSERT INTO results (max_column, filtered_data) VALUES (?, ?)",
                   (max_col, filtered_str))

    conn.commit()
    conn.close()


def write_to_word7(matrix, max_col, filtered, filename='Vlog_Posled.docx'):
    """
    Запись данных в Word-файл
    """
    doc = Document()
    doc.add_paragraph('Исходная матрица:')

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    table = doc.add_table(rows=rows, cols=cols)
    table.style = 'Table Grid'

    for i in range(rows):
        for j in range(cols):
            table.cell(i, j).text = str(matrix[i][j])

    doc.add_paragraph(f'\nНомер столбца с максимальной суммой: {max_col}')

    doc.add_paragraph('Отфильтрованный массив:')
    filtered_str = ', '.join(map(str, filtered))
    doc.add_paragraph(filtered_str)

    doc.save(filename)
    print(f"Данные успешно записаны в Word-файл: {filename}")

#-----------------------------------------------------------------------


def print_students_matrix(matrix, headers):
    """Выводит таблицу студентов"""
    print(tabulate(matrix, headers=headers, tablefmt="grid"))

def generate_students(n, subjects):
    """Генерирует список студентов"""
    surnames = ["Васильева Анастасия", "Исаев Иван", "Анохина Кира", "Муравьева Варвара",
                "Смирнова Мария", "Лазарева Софья", "Майорова Кира", "Рябов Роман",
                "Иванов Михаил", "Тимофеев Илья", "Ефремов Андрей"]
    students = []
    for i in range(n):
        student = [random.choice(surnames), 10 + i]
        grades = {subject: random.randint(-10, 20) for subject in subjects}
        student.append(grades)
        students.append(student)
    return students

def analyze_students(students_data, subjects):
    """
    1. Находит номер зачётки студента с максимальной суммой положительных оценок
    2. Возвращает студентов, у которых СУММА ВСЕХ оценок > этого номера зачётки
    """
    max_positive_sum = -1
    best_recordbook_num = -1

    # Шаг 1: Находим номер зачётки с максимальной суммой положительных оценок
    for student in students_data:
        surname, recordbook_num, grades = student
        positive_sum = sum(grade for grade in grades.values() if grade > 0)

        if positive_sum > max_positive_sum:
            max_positive_sum = positive_sum
            best_recordbook_num = recordbook_num

    # Шаг 2: Фильтруем студентов по сумме всех оценок
    results = []
    all_students = []
    count_above = 0

    for student in students_data:
        surname, recordbook_num, grades = student
        total_sum = sum(grades.values())
        all_students.append([recordbook_num, surname] + [grades[subj] for subj in subjects])

        if total_sum > best_recordbook_num:
            results.append([recordbook_num, surname] + [grades[subj] for subj in subjects])
            count_above += 1

    return results, count_above, best_recordbook_num, all_students

#-----------------------------------------------------------------------

class Educational_Institution:
    age = 0

    def __init__(self, name, foundation_year, current_year):
        self.name = name
        self.foundation_year = foundation_year
        self.current_year = current_year

    def calculate_age(self):
        self.age = self.current_year - self.foundation_year

    def info(self):
        print("\nСоздан класс Учебное заведение")
        print(f"Название: {self.name} Год основания: {self.foundation_year} Возраст: {self.age}")


class School(Educational_Institution):
    def __init__(self, name, foundation_year, current_year, school_type):
        super().__init__(name, foundation_year, current_year)
        self.school_type = school_type

    def info(self):
        Educational_Institution.calculate_age(self)
        Educational_Institution.info(self)
        print("Создан класс Школа")
        print(f"Тип школы: {self.school_type}")


class College(Educational_Institution):
    def __init__(self, name, foundation_year, current_year, study_profile):
        super().__init__(name, foundation_year, current_year)
        self.study_profile = study_profile

    def info(self):
        Educational_Institution.calculate_age(self)
        Educational_Institution.info(self)
        print("Создан класс Колледж")
        print(f"Профиль обучения: {self.study_profile}")


class University(Educational_Institution):
    def __init__(self, name, foundation_year, current_year, education_forms, legal_form):
        super().__init__(name, foundation_year, current_year)
        self.education_forms = education_forms
        self.legal_form = legal_form

    def info(self):
        Educational_Institution.calculate_age(self)
        Educational_Institution.info(self)
        print("Создан класс Университет")
        print(f"Формы обучения: {', '.join(self.education_forms)}")
        print(f"Организационно-правовая форма: {self.legal_form}")

#--------------------------------------------------
from tkinter import *
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime


# --- Главное окно с заставкой ---
class ZastavkaFrame(Frame):
    """Класс заставки приложения. Отображает начальное окно с информацией о программе и авторе."""

    def __init__(self, master):
        """
        Инициализация заставки.
        :param master: Родительское окно Tkinter
        """
        super().__init__(master)
        self.master = master
        self.master.title("Заставка")
        self.master.geometry("600x400")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает и размещает все виджеты на заставке (текст, кнопки)."""
        text = (
            "                    МИНИСТЕРСТВО ЦИФРОВОГО РАЗВИТИЯ, СВЯЗИ\n"
            "         И МАССОВЫХ КОММУНИКАЦИЙ РОССИЙСКОЙ ФЕДЕРАЦИИ\n"
            "   ордена Трудового Красного Знамени федеральное государственное\n"
            "       бюджетное образовательное учреждение высшего образования\n"
            "МОСКОВСКИЙ ТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ СВЯЗИ И ИНФОРМАТИКИ\n"
        )
        Label(self, text=text, justify=LEFT).grid(row=0, column=0, padx=10, pady=10)
        Label(self, text='Тестовая программа на тему "Введение в модель данных SQL"', font=("Arial", 14)).grid(row=1,
                                                                                                               column=0,
                                                                                                               pady=10)
        Label(self, text="Выполнил: Демьянова Д.Д.\nПроверил: Гуриков С.Р.").grid(row=2, column=0, pady=5)
        Button(self, text="Войти", command=self.open_auth).grid(row=3, column=0, pady=15)

    def open_auth(self):
        """Закрывает текущее окно и открывает окно авторизации."""
        self.master.destroy()
        show_auth_window()


# --- Окно авторизации ---
def show_auth_window():
    """Создает и отображает окно авторизации с полями для ввода имени и фамилии."""
    auth_root = Tk()
    auth_root.title("Авторизация")
    auth_root.geometry("300x200")

    Label(auth_root, text="Имя:").grid(row=0, column=0, sticky='e')
    Entry(auth_root).grid(row=0, column=1, padx=10, pady=5)

    Label(auth_root, text="Фамилия:").grid(row=1, column=0, sticky='e')
    Entry(auth_root).grid(row=1, column=1, padx=10, pady=5)

    Button(auth_root, text="Начать тестирование", command=lambda: start_test(auth_root)).grid(row=2, column=0,
                                                                                              columnspan=2, pady=20)


# --- Запуск теста ---
def start_test(auth_window):
    """
    Запускает тестирование после авторизации.
    :param auth_window: Окно авторизации, которое нужно закрыть
    """
    auth_window.destroy()
    root = Tk()
    app = Final(root)
    root.mainloop()


# --- Класс вопроса с Checkbutton ---
class CheckQuestionFrame(Frame):
    """Класс для вопроса с вариантами ответов (Checkbutton)."""

    def __init__(self, master, on_next_callback, question_index):
        """
        Инициализация вопроса с чекбоксами. Вопрос с одним вариантом ответа
        :param master: Родительское окно
        :param on_next_callback: Функция обратного вызова для перехода к следующему вопросу
        :param question_index: Индекс текущего вопроса
        """
        super().__init__(master)
        self.grid()
        self.on_next_callback = on_next_callback
        self.question_index = question_index
        self.create_widgets()

    def proverka(self):
        """Проверяет правильность выбранных ответов и показывает результат."""
        correct = self.otvet1.get() and self.otvet2.get() and not self.otvet3.get() and not self.otvet4.get()
        result = "Ответ правильный" if correct else "Ответ неправильный"
        self.textbox2.delete("1.0", END)
        self.textbox2.insert("1.0", result)
        self.after(1500, lambda: self.load_next(correct))

    def load_next(self, is_correct):
        """
        Загружает следующий вопрос.
        :param is_correct: Флаг правильности ответа на текущий вопрос
        :return: окно нового вопроса
        """
        self.destroy()
        self.on_next_callback(is_correct)

    def create_widgets(self):
        """Создает и размещает виджеты для вопроса с чекбоксами."""
        Label(self, text=f"Вопрос {self.question_index + 1}:").grid(row=0, column=0, sticky=W)
        Label(self, text="Какие из перечисленных операторов используются для фильтрации данных в SQL?").grid(row=1,
                                                                                                           column=0,
                                                                                                           sticky=W)
        self.otvet1 = BooleanVar()  # WHERE
        self.otvet2 = BooleanVar()  # HAVING
        self.otvet3 = BooleanVar()  # SELECT
        self.otvet4 = BooleanVar()  # FILTER

        Checkbutton(self, text="WHERE", variable=self.otvet1).grid(row=2, column=0, sticky=W)
        Checkbutton(self, text="HAVING", variable=self.otvet2).grid(row=3, column=0, sticky=W)
        Checkbutton(self, text="SELECT", variable=self.otvet3).grid(row=4, column=0, sticky=W)
        Checkbutton(self, text="FILTER", variable=self.otvet4).grid(row=5, column=0, sticky=W)

        self.textbox2 = Text(self, width=40, height=3)
        self.textbox2.grid(row=6, column=0, pady=5)

        Button(self, text="Ok", command=self.proverka, width=10, height=2).grid(row=7, column=0, pady=5)


# --- Класс вопроса с Radiobutton ---
class RadioQuestionFrame(Frame):
    """Класс для вопроса с вариантами ответов."""
    def __init__(self, master, on_next_callback, question_index):
        """
        Инициализация вопроса с радиокнопками.
        :param master: Родительское окно
        :param on_next_callback: Функция обратного вызова для перехода к следующему вопросу
        :param question_index: Индекс текущего вопроса
        """
        super().__init__(master)
        self.grid()
        self.on_next_callback = on_next_callback
        self.question_index = question_index
        self.create_widgets()

    def proverka(self):
        """Проверяет правильность выбранного ответа и показывает результат."""
        answer = self.otvet.get()
        correct = answer == "WHERE"
        result = "Вы ответили правильно" if correct else "Вы ответили неправильно"
        self.textbox2.delete("1.0", END)
        self.textbox2.insert("1.0", result)
        self.after(1500, lambda: self.load_next(correct))

    def load_next(self, is_correct):
        """
        Загружает следующий вопрос
        :param is_correct:  Флаг правильности ответа на текущий вопрос
        """
        self.destroy()
        self.on_next_callback(is_correct)

    def create_widgets(self):
        """Создает и размещает виджеты для вопроса с радиокнопками."""
        Label(self, text=f"Вопрос {self.question_index + 1}:").grid(row=0, column=0, sticky=W)
        Label(self, text="Какой раздел SQL-запроса отвечает за фильтрацию строк?").grid(row=1, column=0, sticky=W)
        self.otvet = StringVar(value="")
        options = [
            "SELECT",
            "FROM",
            "WHERE",
            "GROUP BY"
        ]

        for i, option in enumerate(options):
            Radiobutton(self, text=option, variable=self.otvet, value=option).grid(row=2+i, column=0, sticky=W, padx=10)

        self.textbox2 = Text(self, width=40, height=3)
        self.textbox2.grid(row=5, column=0, pady=5)

        Button(self, text="Ok", command=self.proverka, width=10, height=2).grid(row=6, column=0, pady=5)


# --- Класс вопроса с текстовым вводом ---
class TextBoxFrame(Frame):
    """Класс для вопроса с текстовым вводом ответа."""
    def __init__(self, master, on_next_callback, question_index):
        """
        Инициализация вопроса с текстовым полем.
        :param master: Родительское окно
        :param on_next_callback: Функция обратного вызова для перехода к следующему вопросу
        :param question_index: Индекс текущего вопроса
        """
        super().__init__(master)
        self.grid()
        self.on_next_callback = on_next_callback
        self.question_index = question_index
        self.create_widgets()

    def proverka(self):
        """Проверяет правильность введенного текстового ответа."""
        user_input = self.answer_entry.get().strip().lower()
        correct_answers = ["4096"]
        correct = any(ans in user_input for ans in correct_answers)

        result = "Вы ответили правильно" if correct else "Вы ответили неправильно"
        self.textbox2.delete("1.0", END)
        self.textbox2.insert("1.0", result)
        self.after(1500, lambda: self.load_next(correct))

    def load_next(self, is_correct):
        """
        Загружает следующий вопрос.
        :param is_correct: Флаг правильности ответа на текущий вопрос
        """
        self.destroy()
        self.on_next_callback(is_correct)

    def create_widgets(self):
        """Создает и размещает виджеты для вопроса с текстовым вводом."""
        Label(self, text=f"Вопрос {self.question_index + 1}:").grid(row=0, column=0, sticky=W)
        Label(self, text="Сколько столбцов максимально может быть возвращено оператором SELECT в SQL Server?").grid(row=1, column=0, sticky=W)

        self.answer_entry = Entry(self, width=40)
        self.answer_entry.grid(row=2, column=0, pady=5)

        self.textbox2 = Text(self, width=40, height=3)
        self.textbox2.grid(row=3, column=0, pady=5)

        Button(self, text="Ok", command=self.proverka, width=10, height=2).grid(row=4, column=0, pady=5)


# --- Класс итогового окна ---
class ItogFrame(Frame):
    """Класс для отображения итоговых результатов тестирования."""
    def __init__(self, master, root, correct, total):
        """
        Инициализация итогового окна.
        :param master: Родительское окно
        :param root: Главное окно приложения
        :param correct: Количество правильных ответов
        :param total: Общее количество вопросов
        """
        super().__init__(master)
        self.root = root
        self.grid()
        percent = round(100 * correct / total)
        Label(self, text="Тест завершен", font=("Arial", 16)).grid(row=0, column=0, pady=10)
        Label(self, text=f"Правильных ответов: {correct} из {total}").grid(row=1, column=0, pady=5)
        Label(self, text=f"Результат: {percent}%").grid(row=2, column=0, pady=5)
        Button(self, text="Выход", command=self.quit_app).grid(row=3, column=0, pady=10)

    def quit_app(self):
        """Завершает работу приложения."""
        self.root.destroy()


# --- Главный класс управления тестом ---
class Final:
    """Главный класс управления тестированием."""
    def __init__(self, root):
        """
        Инициализация теста.
        :param root: Главное окно приложения
        """
        self.root = root
        self.question_index = 0
        self.correct_answers = 0

        self.question_frames = [CheckQuestionFrame, RadioQuestionFrame, TextBoxFrame]
        self.total_questions = len(self.question_frames)

        self.load_question()

    def load_question(self, was_correct=False):
        """
        Загружает текущий вопрос или завершает тест.
        :param was_correct: Был ли предыдущий ответ правильным
        :return:
        """
        if self.question_index > 0 and was_correct:
            self.correct_answers += 1

        if self.question_index < self.total_questions:
            frame_class = self.question_frames[self.question_index]
            self.frame = frame_class(self.root, self.load_question, self.question_index)
            self.question_index += 1
        else:
            self.save_to_excel()
            self.frame = ItogFrame(self.root, self.root, self.correct_answers, self.total_questions)

    def save_to_excel(self):
        """Сохраняет результаты тестирования в файл Excel."""
        filename = "test_results.xlsx"
        file_exists = os.path.exists(filename)

        if file_exists:
            wb = load_workbook(filename)
            ws = wb.active
        else:
            wb = Workbook()
            ws = wb.active
            ws.append(['Дата и время', 'Правильных ответов', 'Всего вопросов', 'Процент'])

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        percent = round(100 * self.correct_answers / self.total_questions)
        ws.append([now, self.correct_answers, self.total_questions, f"{percent}%"])
        wb.save(filename)
        print("Сохранено в файл test_results.xlsx")