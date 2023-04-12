book = dict()
a = True
while a:
    command_user = input("Введіть команду (stats, add, delete, list, show, exit): ")
    if command_user.lower() == "stats":
        print(f"Кількість записів в книгі {len(book)}")
    elif command_user.lower() == "add":
        new_user = input("Введіть імя нового контакту:")

        if new_user.title() in book.keys():
            print(f"Користувач з імям {new_user.title()} вже є !!!!")
        else:
            new_phone = input("Введіть його телефон:")
            book[new_user.title()] = new_phone
            print(f"Ваш новий запис {new_user.title()} --- {new_phone}")
    elif command_user.lower() == "delete":
        delete_user = input("Введіть імя користувача якого хочете видалити: ")
        if delete_user.title() in book.keys():
            del book[delete_user.title()]
            print(f"Контакт {delete_user.title()} видалено !!!")
        else:
            print(f"Контакт з іменем {delete_user.title()} немає")
    elif command_user.lower() == "list":
        for key in book.keys():
            print(f"Є контакт: {key}")
    elif command_user.lower() == "show":
        show_user = input("Введіть імя для інформації:")
        if show_user in book.keys():
            info_user = book.get(show_user.title())
            print(f"Користувач з імям {show_user.title()} має номер {info_user}")
        else:
            print("Такого користувача немає =(")
    elif command_user.lower() == "exit":
        print("Кінець")
        a = False
