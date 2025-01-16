# src/utils/common_functions.py
from datetime import datetime
def format_number(number):
    """Formate les nombres pour l'affichage"""
    return f"{number:,.2f}"

def calculate_percentage(part, whole):
    """Calcule un pourcentage"""
    return (part / whole * 100) if whole != 0 else 0


def get_year_from_date(date_string):
    """
    Extracts the year from an ISO 8601 date string.
    Args:
        date_string (str): The date string in ISO 8601 format.
    Returns:
        int: The year extracted from the date.
    """
    try:
        # Parse the date string
        date = datetime.fromisoformat(date_string)
        # Return the year
        return date.year
    except ValueError:
        raise ValueError("Invalid date format. Please provide a valid ISO 8601 date string.")


if __name__ == "__main__":
    print(get_year_from_date("2010-01-05T10:00:00+01:00"))