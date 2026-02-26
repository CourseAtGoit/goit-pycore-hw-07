"""Handler for finding and displaying contact information."""

from .input_error import input_error
from address_book import AddressBook


@input_error
def find_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    phones = "; ".join(p.value for p in record.phones)
    return f"{name.capitalize()}: {phones}"
