from packageForPracticeTasks.PracticalTask2.moduls import *

# Создание списка учебных заведений
institutions_list = []
n = int(input("Введите количество учебных заведений: "))
current_year = int(input("Введите текущий год: "))

for i in range(n):
    institution_type = input("Тип заведения? 1) Школа, 2) Колледж, 3) Университет: ")
    name = input("Введите название заведения: ")
    foundation_year = int(input("Введите год основания: "))

    if institution_type == "1":
        school_type = input("Введите тип школы: ")
        institutions_list.append(School(name, foundation_year, current_year, school_type))
    elif institution_type == "2":
        study_profile = input("Введите профиль обучения: ")
        institutions_list.append(College(name, foundation_year, current_year, study_profile))
    elif institution_type == "3":
        education_forms = input("Введите формы обучения через запятую: ").split(',')
        legal_form = input("Введите организационно-правовую форму: ")
        institutions_list.append(University(name, foundation_year, current_year, education_forms, legal_form))

# Вывод информации
print("\nПолная информация о всех учебных заведениях:")
for institution in institutions_list:
    institution.info()

# Поиск по возрасту
min_age = int(input("\nВведите минимальный возраст для поиска: "))
max_age = int(input("Введите максимальный возраст для поиска: "))

print(f"\nУчебные заведения возрастом от {min_age} до {max_age} лет:")
found = False
for institution in institutions_list:
    institution.calculate_age()
    if min_age <= institution.age <= max_age:
        institution.info()
        found = True

if not found:
    print("Заведений с указанным возрастом не найдено.")