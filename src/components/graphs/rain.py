from dash import dcc, html
from src.utils.graphs_functions import create_rainfall_region

def create_rainfall_graph(df):
    fig = create_rainfall_region(df)
    # Création de la figure avec Plotly
    return html.Div([
        html.H1("Graphique de la précipitation moyenne anuelle en France"),

        dcc.Graph(
            id='rainfall-graph',
            figure=fig
        )
    ])