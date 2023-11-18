#%%
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import plotly.express as px

#%%
#Exemple avec données pour Mtp Près d'Arènes et NO2 - Données téléchargées

Mtp = pd.read_csv("Donnees_pour_test.csv")

# Extraction renvoie un dataframe composé des dates et des valeurs relevées pour la station choisie, pour tous les polluants

def extraction(donnees,station) :
    df = donnees.loc[(donnees["nom_station"] == station),["nom_poll","valeur","date_debut"]]
    df["date_debut"] = pd.to_datetime(df["date_debut"], format = '%Y/%m/%d %H:%M:%S%z')
    df = df.rename(columns={'date_debut': 'Date'})
    return df

# test
# print(extraction(Mtp,"Montpellier - Prés d Arènes Urbain"))

# table renvoie un dataframe composé des colonnes : dates et tous les différents polluants en parallèle

def table(donnees,station) :
    data = extraction(donnees,station)
    Poll = data["nom_poll"].unique()
    df = data.loc[data["nom_poll"] == Poll[0],["valeur", "Date"]]
    df = df.rename(columns={'valeur': Poll[0]})
    for i in range(1,len(Poll)) :
        p = Poll[i]
        d = data.loc[data["nom_poll"] == p,["valeur", "Date"]]
        d = d.rename(columns={'valeur': p})
        df = pd.merge(df, d, on = "Date")
    df = df.sort_values(by=['Date'], ascending=[True])
    return df.set_index(["Date"])

# test
# print(extrac_multi(Mtp,"Montpellier - Prés d Arènes Urbain", ["NO2","NOX"]))

#%%

# Trace sur un même graphique les courbes des rélevés pour les polluants (à cocher)



def Trace_px(donnees,station) :
    df = table(donnees,station)
    fig = px.line(df, width=1000, height=500,
     title = "Concentration - " + station,
     labels=dict(value='Concentration (µg/m³)', variable='Polluant'))
    fig.show()


# test
# Trace_px(Mtp,"Montpellier - Prés d Arènes Urbain")




# %%
