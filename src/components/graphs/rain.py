from dash import html, dcc
from src.utils.data_loader import df_cleaned
from src.utils.graphs_functions import create_rainfall_graph

def create_rainfall_layout() -> html.Div:
    """
    Generates a layout of average yearly rainfall by region

    Returns:
        html.Div: A Dash HTML Div containing the graph and title.
    """
    fig = create_rainfall_graph(df_cleaned)
    return html.Div(
        className="component-container",
        children=[
            html.H1("Graphique des Précipitations Moyenne en France"),

            dcc.Graph(
                id='rainfall-graph',
                figure=fig
            )
        ]
    )