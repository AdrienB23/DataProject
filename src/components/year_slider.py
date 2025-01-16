from dash import Dash, dcc, html, Input, Output, callback

from main import app


def year_slider():
    return html.Div([
        dcc.Slider(
            min=2010,
            max=2024,
            step=1,
            value=2024,
            marks={year: str(year) for year in range(2010, 2025)},
            id='slider-year'
        ),
        html.Div(id='slider-output-container'),
    ])

@callback(
    Output('slider-output-container', 'children'),
    Input('slider-year', 'value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)