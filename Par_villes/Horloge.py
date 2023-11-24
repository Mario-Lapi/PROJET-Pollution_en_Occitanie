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
data = pd.read_csv("Mesure_horaire_(30j)_Region_Occitanie_Polluants_Reglementaires.csv")

station = 'Montpellier - Prés d Arènes Urbain'

# Créer le dataframe pour affichage horaire en semaine

def semaine(data, station):
    df = extraction(data, station)
    df = df.set_index(["Date"])
    df["jour_semaine"] = df.index.day_of_week
    df_semaine = df.loc[(df["jour_semaine"] < 5 ),:]
    df_semaine = df_semaine.drop('jour_semaine', axis = 1)
    return df_semaine

# Créer le dataframe pour affichage horaire en weekend

def weekend(data, station):
    df = extraction(data, station)
    df = df.set_index(["Date"])
    df["jour_semaine"] = df.index.day_of_week
    df_weekend = df.loc[(df["jour_semaine"] >4 ),:]
    df_weekend = df_weekend.drop('jour_semaine', axis = 1)
    return df_weekend

# Trace les données horaires en polar

def Horloge(df) :
    df.rename(columns={"nom_poll": "Polluants"}, inplace=True)
    df["heure"] = df.index.hour
    df_polar = (
        df.groupby(["Polluants","heure"])["valeur"]
        .mean()
        .reset_index()
    )
    df_polar = df_polar.astype({"heure": str}, copy=False)
    fig = px.line_polar(
        df_polar,
        r="valeur",
        theta="heure",
        color="Polluants",
        # line_close=True,
        range_r=[0, 60],
    )
    return fig

# Affichage en semaine

def Horloge_semaine(data, station):
    fig = Horloge(semaine(data, station))
    fig.update_layout(title="Pollution horaire en semaine")
    fig.show()

# Affichage en weekend

def Horloge_weekend(data, station):
    fig = Horloge(weekend(data, station))
    fig.update_layout(title="Pollution horaire en weekend")
    fig.show()




# %%
