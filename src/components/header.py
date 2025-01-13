from dash import html

def create_header():
    return html.Header([
        html.H1("Tableau de Bord d'Analyse", className='text-center'),
        html.Hr()
    ])