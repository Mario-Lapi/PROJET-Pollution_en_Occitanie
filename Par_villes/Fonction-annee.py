#%%

import pandas as pd
import plotly.graph_objects as go
from Month import *

#%%

# Création du dataframe pour affichage des minimum, maximum et moyenne par jour

def resume(data, station):
    df = extraction(data, station)
    df = df.set_index(["Date"])
    df["mois"] = df.index.date
    df.rename(columns={"nom_poll": "Polluants"}, inplace=True)
    df_moy = (
        df.groupby(["Polluants", "mois"]).agg(min = ("valeur", min), max = ("valeur", max), moyenne = ("valeur", 'mean'))
        .reset_index()
    )
    return df_moy

# Pour gestion de la transparence des couleurs

def hex_rgba(hex, transparency):
    col_hex = hex.lstrip('#')
    col_rgb = list(int(col_hex[i:i+2], 16) for i in (0, 2, 4))
    col_rgb.extend([transparency])
    areacol = tuple(col_rgb)
    return areacol

# Trace les valeurs minimales, maximales, moyennes ainsi que le seuil de référence

def trace_resume(data, station) :
    df = resume(data, station)
    fig = go.Figure()
    colors = px.colors.qualitative.Plotly
    rgba = [hex_rgba(c, transparency=0.2) for c in colors]
    c =0
    for i in df["Polluants"].unique() : 
        c +=1
        new_col = colors[c]
        col_fond = rgba[c]
        df_poll = df[(df.Polluants == i)]
        x = df_poll["jour"]
        fig.add_traces(go.Scatter(
            x = x,
            y = df_poll["moyenne"],
            mode = 'lines',
            name = i,
            legendgroup = i,
            line = dict(color=new_col, width=2.5)
        )
        )
        fig.add_traces(go.Scatter(
            name = 'Upper Bound',
            x = x,
            y = df_poll["max"],
            legendgroup = i,
            showlegend=False,
            line=dict(width=0)
        )
        )
        fig.add_traces(go.Scatter(
            name = 'Lower Bound',
            x = x,
            y = df_poll["min"],
            fill = 'tonexty',
            legendgroup = i,
            showlegend=False,
            line=dict(width=0),
            fillcolor= 'rgba'+str(col_fond),
        )
        )
        if i == 'PM2.5' :
            fig.add_traces(go.Scatter(
                line=dict(color=new_col, dash='dot'),
                x = x,
                y = [5]*len(x),
                # line_color = new_col,
                legendgroup = i,
                showlegend=False,
            ))
        if i == 'PM10' :
            fig.add_traces(go.Scatter(
                line=dict(color=new_col, dash='dot'),
                x = x,
                y = [15]*len(x),
                # line_color = new_col,
                legendgroup = i,
                showlegend=False,
            ))
        if i == 'O3' :
            fig.add_traces(go.Scatter(
                line=dict(color=new_col, dash='dot'),
                x = x,
                y = [60]*len(x),
                # line_color = new_col,
                legendgroup = i,
                showlegend=False,
            ))
        if i == 'NO2' :
            fig.add_traces(go.Scatter(
                line=dict(color=new_col, dash='dot'),
                x = x,
                y = [10]*len(x),
                # line_color = new_col,
                legendgroup = i,
                showlegend=False,
            ))
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Concentration (µg/m³)",
        title_text = "Concentrations minimale, maximale, moyenne journalières et seuils de référence (OMS)"
    )
    fig.show()




# # Pour test :
# data = pd.read_csv("Mesure_horaire_(30j)_Region_Occitanie_Polluants_Reglementaires.csv")
# station = 'Montpellier - Prés d Arènes Urbain'
# resume(data,station)
# trace_resume(data, station)


# %%
