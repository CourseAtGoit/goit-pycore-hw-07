"""Handler for changing contact phone numbers."""

from .input_error import input_error
from address_book import AddressBook


@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.edit_phone(old_phone, new_phone)
    return f"Phone number for {name.capitalize()} has been updated."
