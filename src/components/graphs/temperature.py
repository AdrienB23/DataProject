from dash import html
from src.components.create_loading import create_loading
from src.components.dropdown_min_max import create_dropdown_min_max
from dash import Input, Output, callback
from src.utils.graphs_functions import create_global_temperature
from src.utils.data_loader import df_cleaned

def create_temperature_layout():
    """
    Generates a graph of average daily temperature in France

    Parameters:
        df (pd.DataFrame): DataFrame containing temperature data with a column named
                            'Température Moyenne (°C)' and 'Date'.

    Returns:
        html.Div: A Dash HTML Div containing the graph and title.
    """
    return html.Div(
        className="component-container",
        children=[
            html.H1("Graphique de la température moyenne en France"),
            create_dropdown_min_max(),
            create_loading("loading-temp", "temperature-graph"),
        ]
    )

@callback(
    Output('temperature-graph', 'figure'),
    [
        Input('temp-dropdown', 'value'),
    ]
)
def update_temp_graph(selected_temp):
    return create_global_temperature(df_cleaned, selected_temp)
