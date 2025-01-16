from dash import dcc, html
from src.utils.graphs_functions import create_global_temperature

def create_temperature_graph(df):
    """
    Generates a graph of average daily temperature in France

    Parameters:
        df (pd.DataFrame): DataFrame containing temperature data with a column named
                            'Température Moyenne (°C)' and 'Date'.

    Returns:
        html.Div: A Dash HTML Div containing the graph and title.
    """
    fig = create_global_temperature(df)
    return html.Div(
        className="component-container",
        children=[
            html.H1("Graphique de la température moyenne en France"),

            dcc.Graph(
                id='temperature-graph',
                figure=fig
            )
        ]
    )