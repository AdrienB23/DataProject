from dash import dcc, html

from src.utils.data_loader import df_cleaned
import pandas as pd

def year_slider(slider_id) -> html.Div:
    """
    Creates a year slider for the dashboard.

    Args:
        slider_id (str): The ID for the slider component.

    Raises:
        ValueError: If there are invalid values in the "Date" column that cannot 
        be converted to datetime.

    Returns:
        html.Div: A container element holding the year slider component.
    """
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