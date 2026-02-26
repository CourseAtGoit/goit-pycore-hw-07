"""Handler for adding birthday to a contact."""

from .input_error import input_error
from address_book import AddressBook


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.add_birthday(birthday)
    return f"Birthday for {name.capitalize()} added."
