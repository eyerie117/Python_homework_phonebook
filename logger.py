from date_create import *

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def add_contact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)
        print()

def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for contact in enumerate(contacts_list, 1):
            print(*contact)
            print()

def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу\n'
    )
    var_search = input('Выберете вариант поиска: ')
    
    while var_search not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод данных, выберете существующий пункт меню')
            print()
            var_search = input('Выберете вариант поиска: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')
    print()

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        search_result = False

        for contact_str in contacts_list:
            contact_lst = contact_str.replace('\n', ' ').split()

            if search in contact_lst[index_var]:
                search_result = True
                print(contact_str)
                print()

        if search_result != True:
            print('По вашему запросу ничего не найдено')
            print()

def copy_contact():
    var_copy = int(input('Укажите номер строки для копирования: '))
    print()

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

        if var_copy > len(contacts_list):
                print('Строки с таким номером не существует')
                print()
                
        for id, contact in enumerate(contacts_list, 1):            
            if id == var_copy:
                with open('phonebook_copy.txt', 'a', encoding='UTF-8') as file:
                    file.write(f'{contact}\n\n')
                    print()
            

def delete_contact():
    var_del = int(input('Укажите номер строки для удаления: '))
    print()

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

        if var_del > len(contacts_list):
                print('Строки с таким номером не существует')
                print()

        with open('phonebook.txt', 'w+', encoding='UTF-8') as file:
            for id, contact in enumerate(contacts_list, 1):
                if id != var_del:
                    file.write(f'{contact}\n\n')