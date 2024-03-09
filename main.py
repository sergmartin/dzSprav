
from dobavl import add_entry
from obnova import update_entry
from delete import delete_entry
from poisk import find_entry





def main():
    while True:
        choice = input("Выберите действие (добавить/обновить/удалить/найти/выход): ").lower()
        if choice == "выход":
            break
        elif choice == "добавить":
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            add_entry(surname, name, phone)
        elif choice == "обновить":
            surname = input("Введите фамилию: ")
            name = input("Введите новое имя (оставьте пустым, чтобы не менять): ")
            phone = input("Введите новый номер телефона (оставьте пустым, чтобы не менять): ")
            update_entry(surname, name, phone)
        elif choice == "удалить":
            surname = input("Введите фамилию для удаления: ")
            delete_entry(surname)
        elif choice == "найти":
            surname = input("Введите фамилию для поиска: ")
            entry = find_entry(surname)
            if entry:
                print(f"Имя: {entry[0]}, Номер телефона: {entry[1]}")
            else:
                print("Запись не найдена.")
        else:
            print("Неизвестное действие.")


if __name__ == "__main__":
    main()