#%%

import pandas as pd
import calendar
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from Month import *

#%%


# Créer le dataframe pour affichage des moyennes par jour

def resume(data, station):
    df = extraction(data, station)
    df = df.set_index(["Date"])
    df["jour"] = df.index.date
    df.rename(columns={"nom_poll": "Polluants"}, inplace=True)
    df_moy = (
        df.groupby(["Polluants", "jour"])["valeur"]
        .mean()
        .reset_index()
    )
    return df_moy

def set_values(row, value):
    return value[row]

def ajout_norme(df):
    map_dictionary = {'NO2': 10, 'PM10': 15, 'PM2.5': 5, 'O3': 60, 'NO': 0, 'NOX': 0}
    df["Seuil"] = df["Polluants"].apply(set_values, args=(map_dictionary,))
    return df


# Trace les données moyennes

def trace_resume(data, station) :
    df = ajout_norme(resume(data, station))
    df.rename(columns={"valeur": "Concentration moyenne (µg/m³)"}, inplace=True)
    fig = px.line(
        df,
        x = "jour",
        y = ["Concentration moyenne (µg/m³)","Seuil"],
        color="Polluants",
    )
    n = df["Polluants"].nunique()
    for i in range(n):
        fig['data'][2*i+1]['line']['dash'] = 'dot'
    fig.update_layout(
        xaxis_title="Date", yaxis_title="Concentration moyenne et seuil de référence (µg/m³)"
    )
    # fig.update_yaxes(minallowed=0)
    fig.show()

# Pour test :
# data = pd.read_csv("Mesure_horaire_(30j)_Region_Occitanie_Polluants_Reglementaires.csv")
# station = 'Montpellier - Prés d Arènes Urbain'
# resume(data,station)
# trace_resume(data, station)



# %%
