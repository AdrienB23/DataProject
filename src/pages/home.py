from dash import html, dcc
from src.components.header import create_header
from src.components.footer import create_footer
from src.components.graphs.temperature import create_temperature_graph
from src.components.graphs.rain import create_rainfall_graph
from src.components.map import create_map_layout
from src.utils.get_data import get_cleaned_data
df = get_cleaned_data()
layout = html.Div([
    create_header(),
    html.Div([
        html.H2("Bienvenue sur le Dashboard"),
    ]),
    create_map_layout(df),
    create_temperature_graph(df),
    create_rainfall_graph(df),
    create_footer()
])
