import dash
from dash import html, dcc
from dash.dependencies import Input, Output

from src.pages import home
from config import CONFIG

# Application initialization
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
# Suppressing callback exceptions allows for defining callbacks on components that are not
# immediately present in the initial layout. This is useful when dynamically loading pages or content.
app.config['suppress_callback_exceptions'] = True
server = app.server

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)

def display_page(pathname):
    """
        Callback function to update the page content based on the current URL pathname.

        Args:
            pathname (str): The URL pathname obtained from the dcc.Location component.

        Returns:
            html.Div or str: The layout of the corresponding page if the pathname matches, otherwise a 404 message.
        """
    if pathname == '/':
        return home.layout
    else:
        return '404 - Page non trouvée'

# Lancement du serveur
if __name__ == '__main__':
    # Main layout definition
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False), # Tracks the URL changes
        html.Div(id='page-content'), # Placeholder for dynamic page content
    ])
    app.run_server(
        host=CONFIG['APP_HOST'],
        port=CONFIG['APP_PORT'],
        debug=CONFIG['DEBUG']
    )
