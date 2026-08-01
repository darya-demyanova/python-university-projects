from packageForPracticeTasks.PracticalTask2.moduls import *

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrica = generate(n, m)
print("Сгенерированная последовательность:")
print_matr(matrica)

max_col = find_max_positive_column(matrica)
new_array = create_filtered_array(matrica, max_col)

print(f"\nСтолбец с максимальной суммой положительных элементов: {max_col}")
print(f"Отфильтрованные элементы (элементы > номера столбца): {new_array}\n")

save_to_binary6("matrix_data.bin", matrica, max_col, new_array)

loaded_matrix, loaded_max_col, loaded_filtered = load_from_binary6("matrix_data.bin")
print("\nЗагруженные данные из бинарного файла:")
print_matr(loaded_matrix)
print(f"\nСтолбец с макс. суммой положительных: {loaded_max_col}")
print(f"Отфильтрованные элементы: {loaded_filtered}\n")

# Сохранение в shelve
save_to_shelve6("matrix_shelve", matrica, max_col, new_array)

# Загрузка из shelve
loaded_matrix, loaded_max_col, loaded_filtered = load_from_shelve6("matrix_shelve")
print("\nЗагруженные данные из shelve:")
print_matr(loaded_matrix)
print(f"\nСтолбец с макс. суммой положительных: {loaded_max_col}")
print(f"Отфильтрованные элементы: {loaded_filtered}")

