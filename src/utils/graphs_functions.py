import plotly.graph_objects as go
import pandas as pd

# Define global regions for metropolitan areas
REGIONS_METROPOLITAN = [
    "Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Bretagne",
    "Centre-Val de Loire", "Corse", "Grand Est", "Hauts-de-France",
    "Île-de-France", "Normandie", "Nouvelle-Aquitaine", "Occitanie",
    "Pays de la Loire", "Provence-Alpes-Côte d'Azur"
]

def create_global_temperature(df, max)-> go.Figure:
    """
    Creates a temperature graph for France, showing either maximum or minimum temperatures by year.

    Args:
        df (pd.DataFrame): The dataframe containing temperature data with 'Date' and 'Température (°C)' columns.
        max (bool): If True, shows the maximum temperature; if False, shows the minimum temperature.

    Returns:
        go.Figure: The Plotly figure with the temperature graph.

    Raises:
        ValueError: If the 'Date' column cannot be converted to datetime.
    """
    # Convert 'Date' to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
    if df["Date"].isnull().any():
        raise ValueError("Certaines valeurs dans la colonne 'Date' ne peuvent pas être converties en datetime.")
    # Create additional columns for year and day
    df["Année"] = df["Date"].dt.year
    df["Jour"] = df["Date"].dt.date

    # Calculate the daily average temperature
    temperature_avg_per_day = df.groupby("Jour")["Température (°C)"].mean().reset_index()
    temperature_avg_per_day["Année"] = pd.to_datetime(temperature_avg_per_day["Jour"]).dt.year
    # Calculate max or min temperature per year
    if max:
        temperature_extreme_per_year = (
            temperature_avg_per_day.groupby("Année")["Température (°C)"]
            .max()
            .reset_index()
        )
    else:
        temperature_extreme_per_year = (
            temperature_avg_per_day.groupby("Année")["Température (°C)"]
            .min()
            .reset_index()
        )
    # Create a scatter plot trace
    trace = go.Scatter(
        x=temperature_extreme_per_year["Année"], 
        y=temperature_extreme_per_year["Température (°C)"],
        mode="markers+lines",
        name="",
        hovertemplate="<b>Température %{y:.1f}°C</b><br>" + 
            "Date : %{x}"
    )

    data = [trace]
    # Layout configuration
    layout = go.Layout(
        title={"text" : "Température France", "x": 0.5},
        xaxis={"title" : {"text" : "Date"}, "fixedrange": True},
        yaxis={"title" : {"text" : "Température (°C)"}, "fixedrange": True},
        template="plotly_white",
    )
    fig = go.Figure(data=data, layout=layout)
    # Return the figure

    return fig

def create_rainfall_graph(df) -> go.Figure:
    """
        Creates a graph of average rainfall by region category over the years.

        Args:
            df (pd.DataFrame): The dataframe containing rainfall data with 'Date', 'region (name)', and 'Précipitations dans les 24 dernières heures' columns.

        Returns:
            go.Figure: The Plotly figure with the rainfall graph.

        Raises:
            ValueError: If the 'Date' column cannot be converted to datetime.
    """
    # Classify regions into 'Régions Métropolitaines' or others
    df["Catégorie Région"] = df["region (name)"].apply(
        lambda x: "Régions Métropolitaines" if x in REGIONS_METROPOLITAN else x
    )
    
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
    if df["Date"].isnull().any():
        raise ValueError("Certaines valeurs dans la colonne 'Date' ne peuvent pas être converties en datetime.")
    df["Année"] = df["Date"].dt.year

    rain_avg_per_year = (
        df.groupby(["Année", "Catégorie Région"])["Précipitations dans les 24 dernières heures"]
        .mean()
        .reset_index()
    )

    traces = [] 
    for category, data in rain_avg_per_year.groupby("Catégorie Région"):
        trace = go.Scatter(
            x=data["Année"],
            y=data["Précipitations dans les 24 dernières heures"],
            mode="lines+markers",
            text=data["Catégorie Région"],
            hovertemplate="<b>Catégorie : %{text}</b><br>" +
                "Année : %{x}<br>" +
                "Précipitations : %{y:.1f} mm",
            name=category,
        )
        traces.append(trace)    

    layout = go.Layout(
        title={"text" : "Moyenne des Précipitations par Catégorie de Région", "x": 0.5},
        xaxis={"title" : {"text" : "Date"}, "fixedrange": True},
        yaxis={"title" : {"text" : "Précipitation (mm)"}, "fixedrange": True},
        template="plotly_white",
    )

    fig = go.Figure(data=traces, layout=layout)
    return fig

def create_wind_graph(df, year) -> go.Figure:
    """
        Creates a graph of average wind speed by region category for a given year.

        Args:
            df (pd.DataFrame): The dataframe containing wind data with 'Date', 'region (name)', and 'Vitesse du vent moyen 10 mn' columns.
            year (int): The year for which to calculate the average wind speed.

        Returns:
            go.Figure: The Plotly figure with the wind speed graph.

        Raises:
            ValueError: If the 'Date' column cannot be converted to datetime.
    """
    df["Catégorie Région"] = df["region (name)"].apply(
        lambda x: "Régions Métropolitaines" if x in REGIONS_METROPOLITAN else x
    )
    
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
    if df["Date"].isnull().any():
        raise ValueError("Certaines valeurs dans la colonne 'Date' ne peuvent pas être converties en datetime.")
    # Filter data for the specified year
    df["Année"] = df["Date"].dt.year
    df_year = df[df["Année"] == year]
    
    # Calculate average wind speed by region category
    wind_avg_by_category = (
        df_year.groupby("Catégorie Région")["Vitesse du vent moyen 10 mn"]
        .mean()
        .reset_index()
    )
    
    wind_avg_by_category = wind_avg_by_category.sort_values(
        by="Vitesse du vent moyen 10 mn", ascending=True
    )
    
    trace = go.Bar(
        x=wind_avg_by_category["Vitesse du vent moyen 10 mn"],
        y=wind_avg_by_category["Catégorie Région"],
        orientation="h",
        name="",
        hovertemplate="<b>Catégorie : %{y}</b><br>" +
                "Vitesse : %{x:.1f} m/s",
    )   

    layout = go.Layout(
        title=f"Vitesse Moyenne des Vents par Catégorie de Région en {year}",
        xaxis={"title": "Vitesse Moyenne (m/s)", "fixedrange": True},
        yaxis={"title": "Catégorie de Région", "fixedrange": True},
        template="plotly_white",
        
    )
    
    fig = go.Figure(data=[trace], layout=layout)
    return fig