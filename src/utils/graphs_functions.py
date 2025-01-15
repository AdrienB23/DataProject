import plotly.graph_objects as go
import pandas as pd

def create_global_temperature(df):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce", utc=True)
    if df["Date"].isnull().any():
        raise ValueError("Certaines valeurs dans la colonne 'Date' ne peuvent pas être converties en datetime.")
    df["Jour"] = df["Date"].dt.date
    temperature_avg_per_day = df.groupby("Jour")["Température (°C)"].mean().reset_index()
    trace = go.Scatter(
        x=temperature_avg_per_day["Jour"], 
        y=temperature_avg_per_day["Température (°C)"],
        mode="lines",
        name="",
        hovertemplate="<b>Température %{y:.1f}°C</b><br>" + 
            "Date : %{x}"
    )

    data = [trace]
    layout = go.Layout(
        title={"text" : "Température France", "x": 0.5},
        xaxis={"title" : {"text" : "Date"}},
        yaxis={"title" : {"text" : "Température (°C)"}},
        template="plotly_white",
    )

    fig = go.Figure(data=data, layout=layout)
    return fig

def create_rainfall_region(df):
    regions_metropolitan = [
        "Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Bretagne",
        "Centre-Val de Loire", "Corse", "Grand Est", "Hauts-de-France",
        "Île-de-France", "Normandie", "Nouvelle-Aquitaine", "Occitanie",
        "Pays de la Loire", "Provence-Alpes-Côte d'Azur"
    ]

    df["Catégorie Région"] = df["region (name)"].apply(
        lambda x: "Régions Métropolitaines" if x in regions_metropolitan else x
    )

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
            name="",
            hovertemplate="<b>Catégorie : %{text}</b><br>Année : %{x}<br>Précipitations : %{y:.1f} mm",
            text=data["Catégorie Région"]
        )
        traces.append(trace)    

    layout = go.Layout(
        title={"text" : "Moyenne des précipitations annuelles par catégorie", "x": 0.5},
        xaxis={"title" : {"text" : "Date"}},
        yaxis={"title" : {"text" : "Précipitation (mm)"}},
    )

    fig = go.Figure(data=traces, layout=layout)
    return fig
    