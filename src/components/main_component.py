from dash import html
from src.components.graphs.temperature import create_temperature_layout
from src.components.map import create_map_layout
from src.components.graphs.rain import create_rainfall_layout

def create_main():
    return html.Main([
        create_map_layout(),
        create_temperature_layout(),
        create_rainfall_layout(),
    ])
