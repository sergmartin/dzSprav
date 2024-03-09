from zapis import write_phonebook
from chitalka import read_phonebook

def add_entry(surname, name, phone):
    phonebook = read_phonebook()
    phonebook[surname] = (name, phone)
    write_phonebook(phonebook)