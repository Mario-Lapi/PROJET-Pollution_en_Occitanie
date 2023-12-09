#%%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


#%%

"""
Module comportant les fonctions d'extraction de données pour la ville choisie
et les fonctions d'étude des données horaires sur 30 jours
"""

# extraction extrait des données les dates et les valeurs relevées pour la station choisie, pour tous les polluants

def extraction(donnees,station) :
    df = donnees.loc[(donnees["nom_station"] == station),["nom_poll","valeur","date_debut"]]
    df["date_debut"] = pd.to_datetime(df["date_debut"], format = '%Y/%m/%d %H:%M:%S%z')
    df = df.rename(columns={'date_debut': 'Date'})
    return df

# table renvoie un dataframe avec en colonnes les dates et tous les différents polluants

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



#%%

# Trace_px affiche sur un même graphique les courbes des concentrations des polluants (à cocher)

def Trace_px(donnees,station) :
    df = table(donnees,station)
    fig = px.line(
        df, 
        width=1000,
        height=500,
        title = "Concentration - " + station,
        labels=dict(value='Concentration (µg/m³)', variable='Polluant')
    )
    fig.show()

# Trace_go affiche les concentrations des différents polluants (à cocher) avec un curseur pour la barre de temps

def Trace_go(donnees,station,ville) :
    data = table(donnees,station)
    fig = go.Figure()
    for i in data.columns :
        fig.add_trace(
            go.Scatter(x=list(data.index), y=list(data[i]), name=i)
        )
    fig.update_layout(
        title_text = "Concentration des polluants à " + ville,
        # labels = dict(y='Concentration (µg/m³)', variable='Polluant')
    ) 
    fig.update_layout(
        yaxis=dict(
            title='Concentration (µg/m³)'
        )
    )
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    fig.show()

