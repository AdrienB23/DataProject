from dash import html, dcc
from src.components.header import create_header
from src.components.footer import create_footer
from src.components.map import create_map
from src.components.graphs.temperature import create_graph
from src.utils.get_data import get_cleaned_data
df = get_cleaned_data()
from src.pages.simple_page import simple_page
layout = html.Div([
    create_header(),
    html.Div([
        html.H2("Bienvenue sur le Dashboard"),
        html.P("Sélectionnez une pages dans la navigation pour commencer.")
    ]),
    create_map(df),
    create_graph(df),
    create_footer()
])
