from packageForPracticeTasks import moduls
from packageForPracticeTasks.PracticalTask2.moduls import create_bd2, get_students_from_bd, find, minim, save_to_excel2

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