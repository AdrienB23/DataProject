from dash import html
from src.components.graphs.temperature import create_temperature_layout
from src.components.map import create_map_layout
from src.components.graphs.rain import create_rainfall_layout
from src.components.graphs.wind import create_wind_layout

def create_main():
    """
    Creates the main layout for the dashboard.

    Returns:
        html.Main: A container element that holds the main sections of the dashboard.
    """
    return html.Main([
        create_map_layout(),
        create_temperature_layout(),
        create_rainfall_layout(),
        create_wind_layout(),
    ])
