"""Handler for showing upcoming birthdays."""

from .input_error import input_error
from address_book import AddressBook
from get_upcoming_birthdays import get_upcoming_birthdays


@input_error
def birthdays(book: AddressBook):
    users = []
    for record in book.data.values():
        if record.birthday is not None:
            users.append(
                {
                    "name": record.name.value.capitalize(),
                    "birthday": record.birthday.value.strftime("%d.%m.%Y"),
                }
            )
    if not users:
        return "No birthdays saved."
    result = get_upcoming_birthdays(users)
    if not result:
        return "No upcoming birthdays in the next 7 days."
    lines = [f"{r['name'].capitalize()}: {r['congratulation_date']}" for r in result]
    return "\n".join(lines)
