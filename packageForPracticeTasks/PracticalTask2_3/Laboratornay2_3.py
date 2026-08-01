from packageForPracticeTasks.PracticalTask2.moduls import *

create_bd2()
students = get_students_from_bd ()

print("Список студентов в базе данных")
for student in students:
    print(f"{student['name']} - Математика: {student['math']}, Физика: {student['physic']}")

print(" ")

rez_spisok = find(students)
min_score = minim(students)
print("Минимальная чётная оценка - ", min_score)

print(" ")

print("Студенты, у которых хотя бы одна оценка выше минимальной чётной оценки")
for student in rez_spisok:
    print(f"{student['name']} - Математика: {student['math']}, Физика: {student['physic']}")

print(" ")

save_to_excel2(rez_spisok)
save_to_world2(students,rez_spisok)
save_to_pdf(students)
save_to_csv(students, rez_spisok)
diagram_student(students)

#PANDAS

csv_file = "Height of Male and Female by Country 2022.csv"
male, female = calculate_pandas(csv_file)
print(f"Средний рост мужчин: {male:.2f} см")
print(f"Средний рост женщин: {female:.2f} см")

male1, female1 = calculate_no_pandas(csv_file)
print(f"Средний рост мужчин: {male1:.2f} см")
print(f"Средний рост женщин: {female1:.2f} см")


csv_filename = "Height of Male and Female by Country 2022.csv"
filter_countries = filter_pandas(csv_filename)
print(filter_countries.to_string(index=False))

filter_countries1 = filter_no_pandas(csv_filename)
print("{:<5} {:<30} {:<15}".format('Rank', 'Country Name', 'Male Height (cm)'))
for country in filter_countries1:
    print("{:<5} {:<30} {:<15.1f}".format(
        country['Rank'],
        country['Country Name'],
        float(country['Male Height in Cm'])
    ))

shortest_male, shortest_female = find_shortest(csv_filename)
print(f'Страна с самим низкими мужчинами: {shortest_male}')
print(f'Страна с самим низкими женщинами: {shortest_female}')

shortest_male1, shortest_female1 = find_shortest_pandas(csv_filename)
print("Страны с самыми низкими мужчинами:")
print(shortest_male1)
print("\nСтраны с самыми низкими женщинами:")
print(shortest_female1)

