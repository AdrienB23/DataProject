from dash import Dash, dcc, html, Input, Output, callback

from main import app


def create_dropdown_tom_tom():
    return html.Div(
        className="dropdown",
        children=[
            dcc.Dropdown(['France Métropolitaine', 'Guadeloupe', 'Guyane', 'La Réunion', 'Martinique'], 'France Métropolitaine', id='country-dropdown'),
        ]
    )