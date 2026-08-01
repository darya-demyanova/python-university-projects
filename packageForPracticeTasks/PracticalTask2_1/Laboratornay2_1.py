from random import random
from packageForPracticeTasks import moduls
from packageForPracticeTasks.PracticalTask2.moduls import generate_list, minim_chet, filter_list

x = int(input('Введите размер списка:'))

random_list = generate_list(x, -10, 10)
minim_chetn = minim_chet(random_list)
filtered_list = filter_list(random_list, minim_chetn)

print('Исходный список:', random_list)
print('Минимальный четный элемент:', minim_chetn)
print('Новый список:', filtered_list)