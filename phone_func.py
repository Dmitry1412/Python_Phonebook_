#from phone_func import show_contacts, find_contact, count_lines, count_lines, add_contact, change_contact, delete_contact, finder, decorate_str, insert_contact

# s - показать контакты - complete
def show_contacts(file: str):
    print('*'*25)
    with open(file,encoding = 'utf-8') as f:
        for line in f:
            data = eval(line)
            num = list(data.keys())
            data = list(data.values())
            
            print(f'Фамилия: {data[0][0]}, Имя: {data[0][1]}, Отчество: {data[0][2]}, Телефон: {data[0][3]}')
    print('*'*25)
        
# f - найти контакт
def find_contact(file: str):
    user_str = input('Введите запрос: ')
    tmp_list = list()
    with open(file, encoding='UTF-8') as f:
        for line in f:
            if user_str in line:
                tmp_list.append(line)
                decorate_str(line)
        if len(tmp_list) > 1:
            #decorate_str(finder(tmp_list)[0])
            tmp_list = finder(tmp_list)
    if not tmp_list is None:
        print('> Вы можете изменить (с), удалить (d) или скопировать (i) данный контакт')
        print('> для отмены (x)')
        user_answer = input('>>>: ')
        if user_answer == "c":
            change_contact(file, tmp_list)   
        elif user_answer == "d":
            delete_contact(file, tmp_list)   
        elif user_answer == "i":
            insert_contact(file, tmp_list)    
        elif user_answer == "x":
            print("> Работа программы завершена!")      
    else:
        print("> Работа программы завершена!")      

# a - добавить запись
def count_lines(file: str):
    with open(file) as f:
        try:
            for i, _ in enumerate(f):
                pass
            return i + 1
        except:
            return 0

def add_contact(file: str):
    print('Для создания новой записи в телефонной книге введите пожалуйста фамилию, имя, отчество и номер телефона')
    l_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    p_name = input("Введите отчество: ")
    phone_num = input("Введите номер телефона: ")
    
    new_dict = {count_lines(file): [l_name, f_name, p_name, phone_num]}
    with open(file,'a',encoding='UTF-8') as f:
        f.write(f'{new_dict}\n')
    print('*'*25)
    print("Контакт добавлен")
    print('*'*25)
        
# c - изменить контакт
def change_contact(file: str, tmp_list: list):
    num_key = list(eval(tmp_list[0]).keys())
    old_data = list(eval(tmp_list[0]).values())
    new_data = old_data.copy()

    print('Для внесения изменений в запись, введите пожалуйста что вы хотите изменить: фамилию - 0, имя - 1, отчество - 2 и номер телефона - 3')
    print('для измения записи полностью, введите Enter')
    user_answer = input(">>>: ")
    if user_answer == '0':
        new_data[0][int(user_answer)] = input("Введите фамилию: ")
    elif user_answer == '1':
        new_data[0][int(user_answer)] = input("Введите имя: ")
    elif user_answer == '2':
        new_data[0][int(user_answer)] = input("Введите отчество: ")
    elif user_answer == '3':
        new_data[0][int(user_answer)] = input("Введите номер телефона: ")
    elif user_answer == '':
        new_data[0][int(user_answer)] = input("Введите фамилию: ")
        new_data[0][int(user_answer)] = input("Введите имя: ")
        new_data[0][int(user_answer)] = input("Введите отчество: ")
        new_data[0][int(user_answer)] = input("Введите номер телефона: ")
    new_list = [new_data[0][0], new_data[0][1], new_data[0][2], new_data[0][3]]
    new_dict = {num_key[0]: new_list}

    with open(file, 'r',encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(tmp_list[0])
        data[i] = (f'{new_dict}\n')

    with open(file, 'w',encoding='utf-8') as f:
        f.writelines(data)
    print('*'*25)
    print('Контакт изменен!')       
    print('*'*25)
# d - удалить контакт
def delete_contact(file: str, tmp_list: list):
    with open(file, encoding='utf-8') as f:
        data = f.readlines()
        data.remove(str(tmp_list[0]))
    with open(file, 'w',encoding='utf-8') as f:
        f.writelines(data)
    print('*'*25)
    print('Контакт удален!')
    print('*'*25)
# вспомогательная функция для find_contact
def finder(contacts: list):
    if len(contacts) > 1:
        result = list()
        print('> Для внесения изменений, удаления, создания копии записи необходимо уточнить запрос')
        print('> Уточните данные или передайте порядковый номер строки')
        print('> Для отмены нажмите X')
        user_answer = input('>>>: ')
        if user_answer != 'x':
            try:
                user_answer = int(user_answer)
                result.append(contacts[user_answer - 1])
            except:
                for el in contacts:
                    if user_answer in el: result.append(el)
        else: 
            result.append("> Поиск завершен!")     
        return result
    else: return contacts
    
# преобразователь
def decorate_str(line: str):
    try:
        data = eval(line)
        num = list(data.keys())
        data = list(data.values())
        print(f'Фамилия: {data[0][0]}, Имя: {data[0][1]}, Отчество: {data[0][2]}, Телефон: {data[0][3]}')
    except:
        print(line)

def import_contacts(file: str):
    print("Для создания копии телефонной книги введите название книги")
    new_book = input(">>>: ")
    print("вы можете сохранить файл в расширении .txt, .csv")
    print("для выбора форамата txt введите (t)")
    print("для выбора форамата csv введите (c)")
    format_new_book = input(">>>: ")
    if format_new_book == 't': format_new_book = '.txt'
    else: format_new_book = '.csv'
    new_book = new_book + format_new_book
    with open(file, encoding='UTF-8') as f:
        data = f.read()
    with open(new_book, 'a',encoding='UTF-8') as f:
        f.write(data)
    print('*'*25)
    print(f'Копия телефонной книги создана: {new_book}!')        
    print('*'*25)
    
def insert_contact(file: str, tmp_list: list):
    print("Для того, чтобы скопировать данный контакт в другую телефонную книгу")
    print("введите ее полное название")
    target_book = input(">>>: ")
    with open(target_book, 'a',encoding='UTF-8') as f:
        f.write(str(*tmp_list))
    print('*'*25)
    print(f'Контакт скопирован в книгу: {target_book}!')        
    print('*'*25)
