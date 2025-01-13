import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import flask
from src.pages import home, about, simple_page
from src.components.navbar import create_navbar
from config import CONFIG
from src.utils.clean_data import clean_data
from src.utils.get_data import get_cleaned_data
# Initialisation de l'application
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

# Layout principal
app.layout = html.Div([
    create_navbar(),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback pour la navigation
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/about':
        return about.layout
    elif pathname == '/simple':
        return simple_page.layout
    else:
        return '404 - Page non trouvée'

# Lancement du serveur
if __name__ == '__main__':
    d = get_cleaned_data()
    app.run_server(
        host=CONFIG['APP_HOST'],
        port=CONFIG['APP_PORT'],
        debug=CONFIG['DEBUG']
    )
