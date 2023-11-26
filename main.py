from phone_func import show_contacts, find_contact, count_lines, count_lines, add_contact, change_contact, delete_contact, finder, decorate_str, import_contacts, insert_contact

def main():
    file_name = 'phone_book.txt'
    flag_exit = False
    while not flag_exit:
        print('s - показать контакты')
        print('i - создать копию телефонной книги')
        print('f - найти контакт')
        print('a - добавить контакт')
        answer = input('Введите операцию или Х для выхода: ')
        if answer == 's':
            show_contacts(file_name)
        elif answer == 'f':
            find_contact(file_name)
        elif answer == "a":
            add_contact(file_name)
        elif answer == 'i':
            import_contacts(file_name)
        elif answer == "x":
            flag_exit = True
            
main()
