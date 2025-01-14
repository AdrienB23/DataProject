from dash import html, dcc

def create_navbar():
    return html.Nav([
        dcc.Link('Accueil', href='/', className='nav-link'),
        dcc.Link('Analyse Simple', href='/simple', className='nav-link'),
    ])