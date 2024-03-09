def write_phonebook(phonebook, filename="phonebook.txt"):
    """Записывает телефонный справочник в файл."""
    with open(filename, "w") as file:
        for surname, (name, phone) in phonebook.items():
            file.write(f"{surname};{name};{phone}\n")
