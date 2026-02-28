from collections import UserDict
from dataclasses import dataclass
from datetime import datetime, date
from typing import TypeVar, Generic
from get_upcoming_birthdays import get_upcoming_birthdays

T = TypeVar("T")


@dataclass
class Field(Generic[T]):
    value: T

    def __str__(self):
        return str(self.value)


@dataclass
class Name(Field[str]):
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("Name cannot be empty.")


@dataclass
class Phone(Field[str]):
    value: str

    def __post_init__(self):
        if not self.value.isdigit() or len(self.value) != 10:
            raise ValueError("Phone number must be a string of 10 digits.")


class Birthday(Field[date]):
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        self.phones = [p for p in self.phones if p.value != phone]

    def find_phone(self, phone: str) -> Phone | None:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for p in self.phones:
            if p.value == old_phone:
                p.value = Phone(new_phone).value
                return
        raise ValueError(f"Phone number '{old_phone}' not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value if self.birthday else 'None'}"


class AddressBook(UserDict):

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        if name not in self.data:
            return None
        return self.data[name]

    def delete(self, name: str) -> None:
        if name not in self.data:
            raise ValueError(f"Record with name '{name}' not found.")

        del self.data[name]
        
    def upcoming_birthdays(self, days_ahead=7):
        users = []
        for record in self.data.values():
            if record.birthday is not None:
                users.append(
                    {
                        "name": record.name.value.capitalize(),
                        "birthday": record.birthday.value.strftime("%d.%m.%Y"),
                    }
                )
        if not users:
            return "No birthdays saved."
        result = get_upcoming_birthdays(users, days_ahead)
        if not result:
            return f"No upcoming birthdays in the next {days_ahead} days."
        lines = [f"{r['name'].capitalize()}: {r['congratulation_date']}" for r in result]
        return "\n".join(lines)
