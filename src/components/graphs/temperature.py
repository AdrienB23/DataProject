import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

def create_temperature(df, region):
    # Faire températures par région
    print(df["region (name)"].unique())
    region = df.query("`region (name)`=='" + region + "'")
    trace = go.Scatter(
        x=region["Date"],
        y=region["Température (°C)"],
        mode="markers"
    )
    data = [trace]
    layout = go.Layout(
        title={"text" : "Température France"},
        xaxis={"title" : {"text" : "Date"}},
        yaxis={"title" : {"text" : "Température (°C)"}}
    )
    fig = go.Figure(data=data, layout=layout)

    # global_temps = list()
    # years = list()
    # for date in df["Date"]:
    #     global_temp=0
    #     for departement in df["department (name)"]:
    #         temp = df.query("`department (name)` == @departement && Date == " + str(date))
    #         print()
    #         global_temp += int(temp["Température (°C)"])
    #     print(global_temp)
    #     global_temps.append(global_temp)
    
    # df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%dT%H:%M:%S%z")
    # temp2024 = df.assign(Year=df['Date'].astype(str).str[:4]).query("Year == '2024'")
    # for date in df["Date"]:
    #     date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
    #     year = date_obj.year
    #     if (years.count(year) == 0):
    #         years.append(year)
    # print(years)
    return fig