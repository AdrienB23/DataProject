import dash
from dash import html, dcc
from dash.dependencies import Input, Output

from src.pages import home
from src.components.navbar import create_navbar
from config import CONFIG
from src.utils.clean_data import clean_data

# Initialisation de l'application
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.config['suppress_callback_exceptions'] = True
server = app.server

# Callback pour la navigation
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)

def display_page(pathname):
    if pathname == '/':
        return home.layout
    else:
        return '404 - Page non trouvée'

# Lancement du serveur
if __name__ == '__main__':
    # Layout principal
    app.layout = html.Div([
        create_navbar(),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ])
    app.run_server(
        host=CONFIG['APP_HOST'],
        port=CONFIG['APP_PORT'],
        debug=CONFIG['DEBUG']
    )
