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

save_to_file7("matrix_output.txt", matrica, max_col, new_array)
print("Результаты сохранены в 'matrix_output.txt'")

save_to_excel7("matrix_results.xlsx", matrica, max_col, new_array)
print("\nРезультаты сохранены в 'matrix_results.xlsx'")

save_to_sqlite7("Vlog_posled.db", matrica, max_col, new_array)
print("\nРезультаты сохранены в 'Vlog_posled.db'")

write_to_word7(matrica, max_col, new_array)
print("\nРезультаты сохранены в 'Vlog_Posled.docx'")

