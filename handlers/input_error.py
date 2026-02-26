"""Decorator for handling input errors in command handlers."""

from functools import wraps


def input_error(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"Contact not found."
        except IndexError:
            return f"Missing argument."
        except ValueError as e:
            return str(e) if str(e) else "Enter the arguments for the command."
        except Exception as e:
            return f"An error occurred: {e}"

    return wrapper
