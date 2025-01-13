from dash import html
from src.components.header import create_header
from src.components.footer import create_footer

layout = html.Div([
    create_header(),
    html.Div([
        html.H2("À propos"),
        html.P("Information sur le projet et son utilisation.")
    ]),
    create_footer()
])