from dash import html

def create_header() -> html.Header:
    """
    Creates an HTML header for a weather dashboard.

    This function generates a `<header>` element

    Returns:
        html.Header: An object representing the HTML header for the dashboard.
    """
    return html.Header([
        html.P("Tableau de Bord Météo", className="header-title"),
    ])