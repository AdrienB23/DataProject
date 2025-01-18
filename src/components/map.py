import json

import pandas as pd
from dash import html, callback, Output, Input
import plotly.express as px

from config import CONFIG
from src.components.create_loading import create_loading
from src.components.dropdown_dom_tom import create_dropdown_tom_tom
from src.components.indicators import create_indicators
from src.components.year_slider import year_slider
from src.utils.map_functions import get_temperature_by_region
from src.utils.data_loader import df_cleaned

# Fonction pour créer une carte centrée sur la France
def create_map_layout():
    """
    Crée la mise en page de la carte avec un slider d'année.
    Parameters:
        df (pd.DataFrame): DataFrame contenant les données de température.
    Returns:
        html.Div: Composant Dash contenant le slider et la carte.
    """
    return html.Div(
        className="component-container",
        children=[
            html.H1("Carte Choroplèthe des Températures Moyennes par Régions"),
            year_slider('map-slider-year'),
            create_dropdown_tom_tom(),
            html.Div(
                className="map-container",
                children=[
                    create_loading("loading-map", "temperature-map"),
                    create_indicators()
                ]
            ),
        ]
    )


# Callback pour mettre à jour la carte
@callback(
    Output('temperature-map', 'figure'),
    [
        Input('map-slider-year', 'value'),
        Input('country-dropdown', 'value'),
    ]
)
def update_map(selected_year, selected_region):
    """
    Met à jour la carte en fonction de l'année sélectionnée.
    Parameters:
        selected_year (int): Année sélectionnée par le slider.
        :param selected_region:
    Returns:
        plotly.graph_objs._figure.Figure: Carte mise à jour.

    """
    # Filtrer les données en fonction de l'année
    filtered_df = get_temperature_by_region(df_cleaned , selected_year)
    filtered_df['Code Région'] = filtered_df['Code Région'].apply(lambda x: f"{int(x):02}")
    region_config = {
        "France Métropolitaine": {
            "center": {"lat": 46.603354, "lon": 1.888334},
            "zoom": 15,
            "range_color": (10, 17)
        },
        "Martinique": {
            "center": {"lat": 14.641528, "lon": -61.024174},
            "zoom": 70,
            "range_color": (24, 28)
        },
        "Guadeloupe": {
            "center": {"lat": 16.265, "lon": -61.551},
            "zoom": 70,
            "range_color": (24, 28)
        },
        "La Réunion": {
            "center": {"lat": -21.135, "lon": 55.536},
            "zoom": 50,
            "range_color": (20, 26)
        },
        "Guyane": {
            "center": {"lat": 4.938, "lon": -52.33},
            "zoom": 30,
            "range_color": (26, 27)
        }
    }
    with open(CONFIG['GEO_JSON']["REGIONS"], 'r', encoding='utf-8') as file:
        geojson = json.load(file)

    # Créer la figure avec Plotly
    fig = px.choropleth(
        filtered_df,
        geojson=geojson,
        locations='Code Région',  # Colonne contenant les codes régionaux
        featureidkey='properties.code',  # Clé dans le GeoJSON
        color='Température Moyenne (°C)',
        color_continuous_scale="RdYlBu_r",
        range_color=region_config.get(selected_region, {}).get('range_color', (10, 17)),
        hover_data={
            'Code Région': False,
            'Région': True,
            'Température Moyenne (°C)': ':.1f',
            'Température Minimum (°C)': ':.1f',
            'Température Maximum (°C)': ':.1f'
        }
    )

    # Configuration de la vue selon la région sélectionnée
    if selected_region in region_config:
        config = region_config[selected_region]
        fig.update_geos(
            fitbounds=None,  # Désactive l'ajustement automatique
            visible=False,
            center=config['center'],
            projection_scale=config['zoom'],
            showland=True,
            landcolor="lightgray",
            showocean=True,
            oceancolor="lightblue"
        )
    else:
        # Vue par défaut centrée sur la France métropolitaine
        default_config = region_config["France Métropolitaine"]
        fig.update_geos(
            fitbounds=None,
            visible=False,
            center=default_config['center'],
            projection_scale=default_config['zoom'],
            showland=True,
            landcolor="lightgray",
            showocean=True,
            oceancolor="lightblue"
        )
    fig.update_layout(
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
        title=f"Températures Moyennes - {selected_region} ({selected_year})",
        title_x=0.5,  # Centre le titre
        height=600,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    return fig
