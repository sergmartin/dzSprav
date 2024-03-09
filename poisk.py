from chitalka import read_phonebook


def find_entry(surname):
    phonebook = read_phonebook()
    return phonebook.get(surname, None)