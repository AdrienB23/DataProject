from dash import html

def create_header():
    return html.Header([
        html.P("Tableau de Bord Météo", className="header-title"),
    ])