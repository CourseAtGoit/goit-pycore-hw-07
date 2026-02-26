"""Handler for deleting contacts."""

from .input_error import input_error
from address_book import AddressBook


@input_error
def delete_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    book.delete(name)
    return f"Contact '{name}' deleted."
