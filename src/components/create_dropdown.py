from dash import Dash, dcc, html, Input, Output, callback

from main import app


def create_dropdown(values, default, dropdown_id):
    """
    Creates a Dash HTML Div containing a Dropdown component.

    This function generates a `html.Div` that wraps around a `dcc.Dropdown`.

    Args:
        values (list): A list of options to be displayed in the dropdown.
        default (str): The default selected value from the dropdown options.
        dropdown_id (str): The unique identifier for the Dropdown component.

    Returns:
        html.Div: A Dash HTML Div containing a Dropdown with the specified options.
    """
    return html.Div(
        className="dropdown",
        children=[
            dcc.Dropdown(values, default, id=dropdown_id),
        ]
    )