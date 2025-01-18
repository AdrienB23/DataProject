from dash import html

def create_footer() -> html.Footer:
    """
    Creates a footer component for the Dashboard.

    Returns:
        html.Footer: A Dash HTML Footer component with styled text.
    """
    return html.Footer([
        html.P('© 2025 - Dashboard Demo. Tous droits réservés.', className='text-center')
    ])