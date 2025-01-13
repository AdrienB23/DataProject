from dash import html, dcc
from src.components.header import create_header
from src.components.footer import create_footer

layout = html.Div([
    create_header(),
    html.Div([
        dcc.Graph(id='simple-graph'),
        html.Div(id='simple-stats')
    ]),
    create_footer()
])
