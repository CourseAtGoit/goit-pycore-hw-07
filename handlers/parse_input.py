"""Module for parsing user input."""


def parse_input(user_input):
    """
    Parse user input into command and arguments.

    Args:
        user_input: Raw user input string.

    Returns:
        tuple: (command, list of arguments)
    """
    # Split input: first word is command, rest are arguments
    cmd, *args = user_input.split()
    # Normalize command to lowercase
    cmd = cmd.lower().strip()
    return cmd, args
