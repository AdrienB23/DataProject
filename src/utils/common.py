# src/utils/common_functions.py
def format_number(number):
    """Formate les nombres pour l'affichage"""
    return f"{number:,.2f}"

def calculate_percentage(part, whole):
    """Calcule un pourcentage"""
    return (part / whole * 100) if whole != 0 else 0