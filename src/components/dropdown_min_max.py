from dash import dcc, html

from main import app


def create_dropdown_min_max():
    return html.Div(
        className="dropdown",
        children=[
            dcc.Dropdown(
                options=[
                    {'label': 'Température Minimum', 'value': False},
                    {'label': 'Température Maximum', 'value': True},
                ],
                value=True,
                id='temp-dropdown'
            )
        ]
    )