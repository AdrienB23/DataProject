import plotly.graph_objects as go

def create_global_temperature(df):
    temperature_avg_per_date = df.groupby("Date")["Température (°C)"].mean().reset_index()
    trace = go.Scatter(
        x=temperature_avg_per_date["Date"], 
        y=temperature_avg_per_date["Température (°C)"],
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