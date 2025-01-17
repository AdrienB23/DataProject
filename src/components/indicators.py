from dash import dcc, html, callback, Output, Input

from src.utils.indicators_functions import temperature_min_max_year

df_global = None
def create_indicators(df):
    global df_global
    df_global = df
    return html.Div(
        className="component-container",
        children=[
            "Temperature Max",
            dcc.Loading(
                id="loading-max",
                type="dot",
                children=[
                    html.H2(id='temp-max'),
                    html.H4(id='temp-max-loc'),
                ]
            ),
            "Temperature Min",
            dcc.Loading(
                id="loading-max",
                type="dot",
                children=[
                    html.H2(id='temp-min'),
                    html.H4(id='temp-min-loc'),
                ]
            )
        ]

    )

# Callback pour mettre à jour les indicateurs
@callback(
    [Output('temp-max', 'children'),
    Output('temp-min', 'children'),
     Output('temp-max-loc', 'children'),
     Output('temp-min-loc', 'children'),],
    [
        Input('slider-year', 'value'),
        Input('country-dropdown', 'value'),
    ]
)
def update_indicators(selected_year, selected_region):
    if not selected_year or not selected_region or df_global is None:
        return "N/A", "N/A"

    try:
        (temp_min, loc_min), (temp_max, loc_max) = temperature_min_max_year(df_global, selected_year,
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