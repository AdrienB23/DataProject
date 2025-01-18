from dash import dcc



def create_loading(loading_id, component_id) -> dcc.Loading:
    """
    Creates a Dash Loading component with a nested Graph component.

    This function generates a `dcc.Loading` component that wraps around a `dcc.Graph`.
    It displays a loading indicator when the nested component is in a loading state.

    Args:
        loading_id (str): The unique identifier for the `dcc.Loading` component.
        component_id (str): The unique identifier for the `dcc.Graph` component.

    Returns:
        dcc.Loading: A Dash Loading component containing a Graph, styled to occupy full width.
    """
    return dcc.Loading(
        id=loading_id,
        type="dot",
        children=[
            dcc.Graph(id=component_id)
        ],
        fullscreen=False,
        parent_style={
            "width": "100%",
        },
    )