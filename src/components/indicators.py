from dash import dcc, html, callback, Output, Input
from src.utils.indicators_functions import temperature_min_max_year, calculate_wind_averages, get_cardinal_direction
from src.utils.data_loader import df_cleaned
def create_indicators():
    """
    Creates a container with weather indicators for the dashboard.

    This function generates an HTML `<div>` element that contains multiple 
    weather indicators

    Returns:
        html.Div: A container element holding the weather indicators
    """
    return html.Div(
        className="indicator-container",
        children=[
            create_indicator_elem(  
                "Temperature Max",
                "loading-max",
                html.Div(
                    className="result-container",
                    children=[
                        html.H2(id='temp-max'),
                        html.H4(id='temp-max-loc'),
                    ]
                )
            ),
            create_indicator_elem(  
                "Temperature Min",
                "loading-max",
                html.Div(
                    className="result-container",
                    children=[
                        html.H2(id='temp-min'),
                        html.H4(id='temp-min-loc'),
                    ]
                )
            ),
            create_indicator_elem("Rose des Vents", "loading-windrose", html.H2(id='wind-stats'))
        ]

    )

def create_indicator_elem(title, loading_id, loading_children):
    """
    Creates an indicator element with a title and a loading component.

    Args:
        title (str): The title or label of the weather indicator.
        loading_id (str): The ID for the loading component.
        loading_children (html.Div or html.H2): The children content to be displayed inside the loading component.

    Returns:
        html.Div: A container element that holds the indicator's title and the loading component.
    """
    return html.Div(
        className="indicator-elem",
        children=[
            html.H3(title),
            dcc.Loading(
                id=loading_id,
                type="dot",
                children=loading_children
            )
        ]
    )

# Callback pour mettre à jour les indicateurs
@callback(
    [
        Output('temp-max', 'children'),
        Output('temp-min', 'children'),
        Output('temp-max-loc', 'children'),
        Output('temp-min-loc', 'children'),
    ],
    [
        Input('map-slider-year', 'value'),
        Input('country-dropdown', 'value'),
    ]
)
def update_indicators(selected_year, selected_region):
    """
    Updates weather indicators based on the selected year and region.

    Args:
        selected_year (int or str): The year for which the weather data is requested.
        selected_region (str): The region for which the weather data is requested.

    Returns:
        tuple: A tuple containing four values:
            - max_text (str): Formatted maximum temperature in °C.
            - min_text (str): Formatted minimum temperature in °C.
            - max_text_loc (str): Location corresponding to the maximum temperature.
            - min_text_loc (str): Location corresponding to the minimum temperature.
        
        If data is unavailable or an error occurs, returns:
            - ("N/A", "N/A") or ("Error", "Error").
    """
    if not selected_year or not selected_region or df_cleaned is None:
        return "N/A", "N/A"

    try:
        (temp_min, loc_min), (temp_max, loc_max) = temperature_min_max_year(df_cleaned, selected_year,
                                                                            selected_region)
        # Formatage des résultats
        max_text = f"{temp_max:.1f}°C"
        min_text = f"{temp_min:.1f}°C"
        max_text_loc = f"{loc_max}"
        min_text_loc = f"{loc_min}"
        return max_text, min_text, max_text_loc, min_text_loc

    except Exception as e:
        print(f"Erreur: {str(e)}")
        return "Erreur", "Erreur"

@callback(
    Output('wind-stats', 'children'),
    [Input('map-slider-year', 'value'),
    Input('country-dropdown', 'value'),]
)
def update_windrose(year, region):
    """
    Updates the wind statistics (speed and direction) based on the selected year and region.

    Args:
        year (int or str): The year for which the wind data is requested.
        region (str): The region for which the wind data is requested.

    Returns:
        html.Div: An HTML `<div>` containing the wind statistics (direction and speed) 
        or an error message if data cannot be fetched.
    """
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