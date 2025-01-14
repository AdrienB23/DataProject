from dash import html, dcc
from src.components.header import create_header
from src.components.footer import create_footer

def simple_page():
    layout = html.Div([
    html.Div([
        dcc.Graph(id='simple-graph'),
        html.Div(id='simple-stats')
    ])
])
