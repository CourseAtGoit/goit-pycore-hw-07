"""Handler for showing upcoming birthdays."""

from .input_error import input_error
from address_book import AddressBook


@input_error
def birthdays(args, book: AddressBook):
    if len(args) > 1:
        raise ValueError("Too many arguments.")
    days_ahead = int(args[0]) if args else 7
    return book.upcoming_birthdays(days_ahead)
    
