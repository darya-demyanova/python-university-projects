from packageForPracticeTasks.PracticalTask2.moduls import *

numstud = int(input("Введите количество студентов: "))
subjects = ["Физика", "Математика", "Информационные технологии"]
matrix = generate_students(numstud, subjects)

data, count_above, best_recordbook_num, allstud = analyze_students(matrix, subjects)

print("\nВсе студенты:")
headers = ["№", "Фамилия"] + subjects
print_students_matrix(allstud, headers)

print(f"\nНомер зачётки с максимальной суммой положительных оценок: {best_recordbook_num}")
print("\nСтуденты, у которых ВСЕ оценки >", best_recordbook_num)
print_students_matrix(data, headers)
print(f"\nКоличество подходящих студентов: {count_above}")