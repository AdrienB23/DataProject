from dash import html
from src.components.indicators import create_indicators
from src.components.graphs.temperature import create_temperature_layout
from src.components.map import create_map_layout
from src.components.graphs.rain import create_rainfall_layout
from src.utils.data_loader import df_cleaned

def create_main():
    return html.Main([
        create_indicators(df_cleaned),
        create_map_layout(),
        create_temperature_layout(),
        create_rainfall_layout(),
    ])
