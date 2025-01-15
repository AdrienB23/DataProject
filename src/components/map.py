import json

from dash import dcc, html
import plotly.express as px

from config import CONFIG
from src.utils.map_functions import get_temperature_by_region

# Fonction pour créer une carte centrée sur la France
def create_map(df):
    """
      Generates a choropleth map of average temperatures by department.

      Parameters:
          df (pd.DataFrame): DataFrame containing temperature data with a column named
                             'Température Moyenne (°C)' and department codes.
          geojson_url (str): URL or file path to the GeoJSON data for the departments.

      Returns:
          html.Div: A Dash HTML Div containing the map and title.
      """
    df = get_temperature_by_region(df)
    # Création de la figure avec Plotly
    with open(CONFIG['GEO_JSON']['REGIONS'], 'r', encoding='utf-8') as file:
        geojson = json.load(file)
    fig = px.choropleth(
        df,
        geojson=geojson,
        locations='region (code)', # Column in DataFrame
        featureidkey='properties.code',  # Key in GeoJSON
        color='Température Moyenne (°C)',
        color_continuous_scale="Viridis",
        range_color=(10, 16),
        labels={'Température Moyenne (°C)': 'Average Temp (°C)'}
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        title="Carte Choroplèthe des Températures Moyennes par Region"
    )
    return html.Div([
        html.H1("Carte Choroplèthe des Températures Moyennes par Régions"),
        dcc.Graph(id='temperature-map', figure=fig)
    ])