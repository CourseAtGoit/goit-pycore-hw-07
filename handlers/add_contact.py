"""Handler for adding new contacts."""

from .input_error import input_error
from address_book import AddressBook, Record


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message
