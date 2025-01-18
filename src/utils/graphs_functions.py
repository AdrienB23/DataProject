import plotly.graph_objects as go
import pandas as pd

global regions_metropolitan
regions_metropolitan = [
    "Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Bretagne",
    "Centre-Val de Loire", "Corse", "Grand Est", "Hauts-de-France",
    "Île-de-France", "Normandie", "Nouvelle-Aquitaine", "Occitanie",
    "Pays de la Loire", "Provence-Alpes-Côte d'Azur"
]

def create_global_temperature(df, max):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
    if df["Date"].isnull().any():
        raise ValueError("Certaines valeurs dans la colonne 'Date' ne peuvent pas être converties en datetime.")
    df["Année"] = df["Date"].dt.year
    df["Jour"] = df["Date"].dt.date

    temperature_avg_per_day = df.groupby("Jour")["Température (°C)"].mean().reset_index()
    temperature_avg_per_day["Année"] = pd.to_datetime(temperature_avg_per_day["Jour"]).dt.year
    
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
    trace = go.Scatter(
        x=temperature_extreme_per_year["Année"], 
        y=temperature_extreme_per_year["Température (°C)"],
        mode="markers+lines",
        name="",
        hovertemplate="<b>Température %{y:.1f}°C</b><br>" + 
            "Date : %{x}"
    )

    data = [trace]
    layout = go.Layout(
        title={"text" : "Température France", "x": 0.5},
        xaxis={"title" : {"text" : "Date"}, "fixedrange": True},
        yaxis={"title" : {"text" : "Température (°C)"}, "fixedrange": True},
        template="plotly_white",
    )

    fig = go.Figure(data=data, layout=layout)
    return fig

def create_rainfall_graph(df):

    df["Catégorie Région"] = df["region (name)"].apply(
        lambda x: "Régions Métropolitaines" if x in regions_metropolitan else x
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

def create_wind_graph(df, year):
    df["Catégorie Région"] = df["region (name)"].apply(
        lambda x: "Régions Métropolitaines" if x in regions_metropolitan else x
    )
    
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
    if df["Date"].isnull().any():
        raise ValueError("Certaines valeurs dans la colonne 'Date' ne peuvent pas être converties en datetime.")
    
    df["Année"] = df["Date"].dt.year
    
    df_year = df[df["Année"] == year]
    
    # Calculer la vitesse moyenne par catégorie
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