"""Handler for displaying all contacts."""

from .input_error import input_error
from address_book import AddressBook


@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "No contacts found."
    result = []
    for record in book.data.values():
        result.append(str(record))
    return "\n".join(result)
