from dash import Dash, dcc, html, Input, Output, callback

from main import app


def year_slider():
    return html.Div([
        dcc.Slider(2010, 2024, 1,
                   value=2024,
                   marks={year: str(year) for year in range(2010, 2025)},
                   id='slider-year'
        ),
        html.Div(id='slider-output-container'),
    ])