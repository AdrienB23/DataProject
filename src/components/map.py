import json

from dash import dcc, html, callback, Output, Input
import plotly.express as px

from config import CONFIG
from src.components.year_slider import year_slider, update_output
from src.utils.map_functions import get_temperature_by_region

df_global = None
# Fonction pour créer une carte centrée sur la France
def create_map_layout(df):
    """
    Crée la mise en page de la carte avec un slider d'année.
    Parameters:
        df (pd.DataFrame): DataFrame contenant les données de température.
    Returns:
        html.Div: Composant Dash contenant le slider et la carte.
    """
    global df_global
    df_global = df
    return html.Div([
        html.H1("Carte Choroplèthe des Températures Moyennes par Régions"),
        year_slider(),
        dcc.Loading(
            id="loading-map",
            type="dot",
            children=[
                dcc.Graph(id='temperature-map')  # Placeholder pour la carte
            ],
            fullscreen=False,
        )
    ])


# Callback pour mettre à jour la carte
@callback(
    Output('temperature-map', 'figure'),
    Input('slider-year', 'value')
)
def update_map(selected_year):
    """
    Met à jour la carte en fonction de l'année sélectionnée.
    Parameters:
        selected_year (int): Année sélectionnée par le slider.
    Returns:
        plotly.graph_objs._figure.Figure: Carte mise à jour.
    """
    # Filtrer les données en fonction de l'année
    filtered_df = get_temperature_by_region(df_global , selected_year)

    # Charger le GeoJSON
    with open(CONFIG['GEO_JSON']['REGIONS'], 'r', encoding='utf-8') as file:
        geojson = json.load(file)

    # Créer la figure avec Plotly
    fig = px.choropleth(
        filtered_df,
        geojson=geojson,
        locations='Code Région',  # Colonne contenant les codes régionaux
        featureidkey='properties.code',  # Clé dans le GeoJSON
        color='Température Moyenne (°C)',
        color_continuous_scale="Viridis",
        range_color=(10, 17),
        labels={'Température Moyenne (°C)': 'Average Temp (°C)'}
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        title=f"Carte des Températures Moyennes pour l'Année {selected_year}"
    )
    return fig