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
        
    


# if __name__ == "__main__":
#     try:
#         # Створення нової адресної книги
#         book = AddressBook()

#         # Створення запису для John
#         john_record = Record("John")
#         john_record.add_phone("1234567890")
#         john_record.add_phone("5555555555")
#         john_record.add_birthday("15.04.1990")

#         # Додавання запису John до адресної книги
#         book.add_record(john_record)

#         # Створення та додавання нового запису для Jane
#         jane_record = Record("Jane")
#         jane_record.add_phone("9876543210")
#         jane_record.add_phone("2222222222")
#         book.add_record(jane_record)

#         # Виведення всіх записів у книзі
#         for name, record in book.data.items():
#             print(record)  # Виведення: 1990-04-15

        # print(list(book.data.items()))  # Виведення словника з записами

    #     # Знаходження та редагування телефону для John
    #     john = book.find("John")

    #     john.edit_phone("1234567890", "1112223333")

    #     print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    #     # Пошук конкретного телефону в записі John

    #     found_phone = john.find_phone("5555555555")
    #     print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    #     # Видалення запису Jane
    #     book.delete("Jane")
    #     # Виведення всіх записів після видалення Jane
    #     for name, record in book.data.items():
    #         print(
    #             record
    #         )  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    # except ValueError as e:
    #     print(f"Error: {e}")
