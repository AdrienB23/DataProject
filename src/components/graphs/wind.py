from dash import html, dcc
from src.components.year_slider import year_slider
from src.utils.data_loader import df_cleaned
from src.utils.graphs_functions import create_wind_graph
from dash import Input, Output, callback
from src.components.create_loading import create_loading

def create_wind_layout():
    """
    Generates a layout of average yearly rainfall by region

    Parameters:
        df (pd.DataFrame): DataFrame containing rainfall data with a column named
                            'Précipitations dans les 24 dernières heures' and 'Date'.

    Returns:
        html.Div: A Dash HTML Div containing the graph and title.
    """
    return html.Div(
        className="component-container",
        children=[
            html.H1("Graphique de la Vitesse Moyenne des Vents par Région"),
            
            year_slider('wind-slider-year'),
            create_loading("loading-wind", "wind-bar-graph"),
        ]
    )
    
@callback(
    Output('wind-bar-graph', 'figure'),
    Input('wind-slider-year', 'value')
)
def update_wind_graph(selected_year):
    return create_wind_graph(df_cleaned, selected_year)