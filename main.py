"""Main module for contact assistant bot."""

from handlers import *
from address_book import AddressBook, Record
from collections import UserDict


def main():
    book = AddressBook()

    # Command dispatcher: maps command names to handler functions
    commands = {
        "add": lambda args: add_contact(args, book),
        "all": lambda args: show_all(book),
        "phone": lambda args: find_contact(args, book),
        "change": lambda args: change_phone(args, book),
        "delete": lambda args: delete_contact(args, book),
        "add-birthday": lambda args: add_birthday(args, book),
        "show-birthday": lambda args: show_birthday(args, book),
        "birthdays": lambda args: birthdays(book),
    }

    print("Welcome to the assistant bot!")

    while True:
        try:

            user_input = input("Enter a command: ").lower().strip()

            if not user_input:
                print("Usage: Please enter a command")
                continue

            # Parse user input into command and arguments
            command, args = parse_input(user_input)

            if command in ["exit", "close"]:
                print("Goodbye!")
                break

            elif command == "hello":
                print("How can I help you?")
            # Execute command if it exists in command dispatcher
            elif command in commands:
                result = commands[command](args)
                if result is not None:
                    print(result)
            else:
                print("Invalid command.")

        except ValueError as e:
            print(f"Invalid input format: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
