#%%

import pandas as pd
import calendar
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from Month import *

#%%
"""
Module permettant la construction des graphes en forme d'horloge permettant les comparaisons horaires
L'extraction des données se fait grâce au module Month
"""

# Semaine crée le dataframe pour l'affichage horaire en semaine (extraction des jours de semaine)

def semaine(data, station):
    df = extraction(data, station)
    df = df.set_index(["Date"])
    df["jour_semaine"] = df.index.day_of_week
    df_semaine = df.loc[(df["jour_semaine"] < 5 ), : ]
    df_semaine = df_semaine.drop('jour_semaine', axis = 1)
    return df_semaine

# Weekend crée le dataframe pour l'affichage horaire en weekend (extraction des jours du weekend)

def weekend(data, station):
    df = extraction(data, station)
    df = df.set_index(["Date"])
    df["jour_semaine"] = df.index.day_of_week
    df_weekend = df.loc[(df["jour_semaine"] >4 ), : ]
    df_weekend = df_weekend.drop('jour_semaine', axis = 1)
    return df_weekend

# Horloge trace la moyenne des données horaires en polar

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
        # line_close=True,  retourne une erreur dûe au format des dataframe
    )
    return fig

# Horloge_semaine affiche le graphique pour les jours de semaine

def Horloge_semaine(data, station):
    fig = Horloge(semaine(data, station))
    fig.update_layout(title="Concentration moyenne horaire en semaine, au cours du dernier mois")
    fig.show()

# Horloge_weekend affiche le graphique pour les jours de weekend

def Horloge_weekend(data, station):
    fig = Horloge(weekend(data, station))
    fig.update_layout(title="Concentration moyenne horaire en weekend, au cours du dernier mois")
    fig.show()




# %%
