from dash import html

from src.components.navbar import create_navbar

def create_header():
    return html.Header([
        html.P("Tableau de Bord Météo", className="header-title"),
    ])