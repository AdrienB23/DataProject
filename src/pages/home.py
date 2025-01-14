from dash import html, dcc
from src.components.header import create_header
from src.components.footer import create_footer
from src.components.map import create_map

layout = html.Div([
    create_header(),
    html.Div([
        html.H2("Bienvenue sur le Dashboard"),
        html.P("Sélectionnez une pages dans la navigation pour commencer.")
    ]),
    create_map(),
    create_footer()
])
