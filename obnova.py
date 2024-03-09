from zapis import write_phonebook
from chitalka import read_phonebook

def update_entry(surname, name=None, phone=None):
    phonebook = read_phonebook()
    if surname in phonebook:
        current_name, current_phone = phonebook[surname]
        phonebook[surname] = (name if name else current_name, phone if phone else current_phone)
        write_phonebook(phonebook)