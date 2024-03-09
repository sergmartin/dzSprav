from zapis import write_phonebook
from chitalka import read_phonebook

def delete_entry(surname):
    phonebook = read_phonebook()
    if surname in phonebook:
        del phonebook[surname]
        write_phonebook(phonebook)