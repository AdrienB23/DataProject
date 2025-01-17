from dash import html
from src.components.main_component import create_main
from src.components.footer import create_footer
from src.components.header import create_header

layout = html.Div(
    className="page-container",
    children=[
        create_header(),
        create_main(),
        create_footer()
    ]
)
