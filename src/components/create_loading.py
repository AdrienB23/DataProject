from dash import dcc, html

from main import app


def create_loading(loading_id, component_id):
    return dcc.Loading(
        id=loading_id,
        type="dot",
        children=[
            dcc.Graph(id=component_id)
        ],
        fullscreen=False,
    )