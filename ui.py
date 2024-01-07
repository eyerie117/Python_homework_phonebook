from logger import *

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass

    command = '-1'
    while command != '6':
        print('Выберете необходимое действие:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Копирование данных\n'
            '5. Удаление данных\n'
            '6. Выход из программы')        
        print()

        command = input('Выберете пункт меню: ')
        print()

        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод данных, выберете существующий пункт меню')
            command = input('Выберете пункт меню: ')

        match command: 
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                delete_contact()
            case '6':
                print('Программа завершила свою работу')