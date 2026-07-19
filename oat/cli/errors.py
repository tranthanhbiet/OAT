"""
CLI error handling utilities.
"""

import sys


def cli_error(title: str, message: str, exit_code: int = 1) -> None:
    """
    Print a user-friendly error message and exit.

    Parameters
    ----------
    title
        Short error title.
    message
        Detailed explanation.
    exit_code
        Process exit code.
    """

    print()

    print("=" * 60)
    print("ERROR")
    print("=" * 60)

    print()
    print(title)
    print()

    print(message)
    print()

    sys.exit(exit_code)