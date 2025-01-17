from dash import dcc, html
from src.utils.graphs_functions import create_rainfall_region

def create_rainfall_graph(df):
    """
    Generates a graph of average yearly rainfall by region

    Parameters:
        df (pd.DataFrame): DataFrame containing rainfall data with a column named
                            'Précipitations dans les 24 dernières heures' and 'Date'.

    Returns:
        html.Div: A Dash HTML Div containing the graph and title.
    """
    fig = create_rainfall_region(df)
    return html.Div(
        className="component-container",
        children=[
            html.H1("Graphique de la précipitation moyenne anuelle en France"),

            dcc.Graph(
                id='rainfall-graph',
                figure=fig
            )
        ]
    )