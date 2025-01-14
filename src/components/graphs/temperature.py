from dash import dcc, html
from src.utils.graphs_functions import create_global_temperature

def create_graph(df):
    fig = create_global_temperature(df)
    # Création de la figure avec Plotly
    return html.Div([
        html.H1("Graphique de la température moyenne en France"),

        dcc.Graph(
            id='temperature-graph',
            figure=fig
        )
    ])