n = None
while n != '0':
    print('Меню')
    print('0 - Выйти')
    print('1 - Лабораторные работы за 1 семестр')
    print('2 - Лабораторные работы за 2 семестр')
    n = input('Сделайте выбор: ')

    if n =='0':
        print("Конец работы")
        exit()

    if n == '1':
        print('1 - Выполнить ЛР №1')
        print('2 - Выполнить ЛР №2')
        print('3 - Выполнить ЛР №3')
        print('4 - Выполнить ЛР №4')
        print('5 - Выполнить ЛР №5')
        print('6 - Выполнить ЛР №6')
        print('')
        n1 = input('Сделайте выбор: ')
        if n1 == '1':
            import packageForPracticeTasks.PracticalTask1.Laboratornay1
            exit()
        if n1 == '2':
            import packageForPracticeTasks.PracticalTask2.laboratornay2
            exit()
        if n1 == '3':
            import packageForPracticeTasks.PracticalTask3.Laboratornay3
            exit()
        if n1 == '4':
            import packageForPracticeTasks.PracticalTask4.Laboratornay4
            exit()
        if n1 == '5':
            import packageForPracticeTasks.PracticalTask5.Laboratornay5
            exit()
        if n1 == '6':
            import packageForPracticeTasks.PracticalTask6.laboratornay6
            exit()
        else:
            print('Такого варианта нет')
            exit()

    if n == '2':
        print('1 - Работа со списками')
        print('2 - Работа со списками')
        print('3 - Запись списков во внешние программы и работа с Pandos')
        print('5 - Двумерный массив')
        print('6 - Консервация и расконсервация данных')
        print('7 - Вывод во внешние программы')
        print('8 - Матрица студентов')
        print('')
        n1 = input('Сделайте выбор: ')
        if n1 == '1':
            import packageForPracticeTasks.PracticalTask2_1.Laboratornay2_1
            exit()
        if n1 == '2':
            import packageForPracticeTasks.PracticalTask2_2.Laboratornay2_2
            exit()
        if n1 == '3':
            import packageForPracticeTasks.PracticalTask2_3.Laboratornay2_3
            exit()
        if n1 == '5':
            import packageForPracticeTasks.PracticalTask2_5.Laboratornay2_5
            exit()
        if n1 == '6':
            import packageForPracticeTasks.PracticalTask2_6.Laboratornay2_6
            exit()
        if n1 == '7':
            import packageForPracticeTasks.PracticalTask2_7.Laboratornay2_7
            exit()
        if n1 == '8':
            import packageForPracticeTasks.PracticalTask2_8.Laboratornay2_8
            exit()
        else:
            print('Такого варианта нет')
            exit()
    else:
        print('Такого варианта нет')
        exit()