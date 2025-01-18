from dash import Dash, dcc, html

from main import app
from src.utils.data_loader import df_cleaned
import pandas as pd

def year_slider(slider_id):
    df_cleaned["Date"] = pd.to_datetime(df_cleaned["Date"], errors="coerce", utc=True)

    if df_cleaned["Date"].isnull().any():
        raise ValueError("Certaines valeurs dans la colonne 'Date' ne peuvent pas être converties en datetime.")

    df_cleaned["Année"] = df_cleaned["Date"].dt.year
    return html.Div([
        dcc.Slider(
            min=int(df_cleaned["Année"].min()),
            max=int(df_cleaned["Année"].max()),
            step=1,
            value=int(df_cleaned["Année"].max()),
            marks={year: str(year) for year in range(2010, 2025)},
            id=slider_id
        ),
    ])