from src.utils.data_loader import df_cleaned
from src.utils.indicators_functions import calculate_wind_averages
from dash import html, callback
from dash.dependencies import Input, Output

@callback(
    Output('wind-stats', 'children'),
    [Input('slider-year', 'value'),
    Input('country-dropdown', 'value'),]
)
def update_windrose(year, region):
    try:
        # Obtenir les données de vent
        wind_speed, wind_direction = calculate_wind_averages(df_cleaned, year, region)

        stats = html.Div(
            [
                html.H2(f"{get_cardinal_direction(wind_direction)}", title="Direction cardinale", style={"font-weight": "bold"}),
                html.H2(f"{wind_speed:.2f} m/s", title="Vitesse moyenne"),
            ],
            style={
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "center",
                "alignItems": "center",
                "textAlign": "center",
                "height": "100%",
            },
        )

    except Exception as e:
        stats = html.Div([
            html.H4("Erreur"),
            html.P(str(e))
        ])

    return stats

def get_cardinal_direction(degrees):
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                  'S', 'SSO', 'SO', 'OSO', 'O', 'ONO', 'NO', 'NNO']
    index = round(degrees / (360 / len(directions))) % len(directions)
    return directions[index]