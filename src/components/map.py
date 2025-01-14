from dash import dcc, html
import plotly.express as px

from src.utils.get_data import get_cleaned_data
from src.utils.map_functions import get_temperature_by_department

# Fonction pour créer une carte centrée sur la France
def create_map(df):
    df = get_temperature_by_department(df)
    # Création de la figure avec Plotly
    return html.Div([
        html.H1("Carte Choroplèthe des Températures Moyennes par Département"),
        dcc.Graph(
            id='temperature-map',
            figure=px.scatter_geo(df,
                                  lat='Latitude',
                                  lon='Longitude',
                                  color='Température Moyenne (°C)',
                                  hover_name='department (name)',
                                  hover_data=['Température Moyenne (°C)', 'Latitude', 'Longitude'],
                                  title='Températures Moyennes par Département',
                                  color_continuous_scale='Viridis',
                                  projection="natural earth")  # Projection de la carte
        )
    ])