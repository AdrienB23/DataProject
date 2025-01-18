# src/utils/common_functions.py
from datetime import datetime
def format_number(number):
    """
        Formats a number with commas and two decimal places for display.

        Args:
            number (float): The number to format.

        Returns:
            str: The formatted number as a string.
    """
    return f"{number:,.2f}"

def calculate_percentage(part, whole):
    """
       Calculates the percentage of a part relative to a whole.

       Args:
           part (float): The part value.
           whole (float): The whole value.

       Returns:
           float: The percentage of the part relative to the whole.

       Raises:
           ValueError: If the whole is zero.
    """
    return (part / whole * 100) if whole != 0 else 0


def get_year_from_date(date_string):
    """
       Extracts the year from an ISO 8601 date string.

       Args:
           date_string (str): The date string in ISO 8601 format (e.g., '2010-01-05T10:00:00+01:00').

       Returns:
           int: The year extracted from the date.

       Raises:
           ValueError: If the date string is not in a valid ISO 8601 format.
    """
    try:
        # Parse the date string and return the year
        date = datetime.fromisoformat(date_string)
        return date.year
    except ValueError:
        raise ValueError("Invalid date format. Please provide a valid ISO 8601 date string.")


if __name__ == "__main__":
    print(get_year_from_date("2010-01-05T10:00:00+01:00"))