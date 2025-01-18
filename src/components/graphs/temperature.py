from dash import html
from src.components.create_dropdown import create_dropdown
from src.components.create_loading import create_loading
from dash import Input, Output, callback
from src.utils.graphs_functions import create_global_temperature
from src.utils.data_loader import df_cleaned

def create_temperature_layout():
    """
    Generates a layout of average temperature in France

    Returns:
        html.Div: A Dash HTML Div containing the graph and title.
    """
    values=[
        {'label': 'Température Minimum', 'value': False},
        {'label': 'Température Maximum', 'value': True}
    ]
    return html.Div(
        className="component-container",
        children=[
            html.H1("Graphique des températures extrêmes en France"),
            create_dropdown(values, True, 'temp-dropdown'),
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
    """
    Updates the graph depending on the year selected.
    Parameters:
        selected_year (int): Year selected by the slider.
        
    Returns:
        plotly.graph_objs._figure.Figure: Graph update.
    """
    return create_global_temperature(df_cleaned, selected_temp)
