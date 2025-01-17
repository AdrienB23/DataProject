from dash import html
from src.components.graphs.temperature import create_temperature_graph
from src.components.indicators import create_indicators
from src.components.map import create_map_layout
from src.components.graphs.rain import create_rainfall_graph

def create_main(df):
    return html.Main([
            html.Div(
                create_indicators(df)
            ),
            html.Div(
                className="temp-container",
                children=[
                    create_map_layout(df),
                    create_temperature_graph(df),
                ]
            ),
            create_rainfall_graph(df),
        ]
    )