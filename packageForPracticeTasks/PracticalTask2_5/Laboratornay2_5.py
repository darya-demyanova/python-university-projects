from packageForPracticeTasks.PracticalTask2.moduls import *


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrica = generate(n, m)

print("Сгенерированная последовательность:")
print_matr(matrica)

max_col = find_max_positive_column(matrica)
print(f"Столбец с максимальной суммой положительных элементов: {max_col}")

new_array = create_filtered_array(matrica, max_col)

print(f"Новый массив (элементы > номера столбца): {new_array}")
