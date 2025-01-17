from dash import html

def create_footer():
    return html.Footer([
        html.P('© 2025 - Dashboard Demo', className='text-center')
    ])