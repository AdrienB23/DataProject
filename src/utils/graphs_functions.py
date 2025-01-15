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