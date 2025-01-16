from dash import html

from src.components.navbar import create_navbar

def create_header():
    return html.Header([
        # html.H1("Tableau de Bord d'Analyse Météorologique", className='text-center'),
        html.P("Tableau de Bord Météo", className="header-title"),
        create_navbar(),
    ])