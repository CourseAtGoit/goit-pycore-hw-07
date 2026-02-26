"""Handler for showing birthday of a contact."""

from .input_error import input_error
from address_book import AddressBook


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    if record.birthday is None:
        return f"{name.capitalize()} has no birthday set."
    return (
        f"{name.capitalize()}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    )
