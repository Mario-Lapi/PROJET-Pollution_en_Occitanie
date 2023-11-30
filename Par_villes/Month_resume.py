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

# Trace les données moyennes

def trace_resume(data, station) :
    df = resume(data, station)
    df.rename(columns={"valeur": "Concentration moyenne (µg/m³)"}, inplace=True)
    fig = px.line(
        df,
        x = "jour",
        y = "Concentration moyenne (µg/m³)",
        color="Polluants",
        width = 700
    )
    return fig

# Pour test :
data = pd.read_csv("Mesure_horaire_(30j)_Region_Occitanie_Polluants_Reglementaires.csv")
station = 'Montpellier - Prés d Arènes Urbain'
resume(data,station)
trace_resume(data, station)



# %%
