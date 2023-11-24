# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

#Extrait des données pour Mtp Près d'Arènes et NO2 - Données téléchargées

Mtp = pd.read_csv("Donnees_pour_test.csv")
Mtp_PA_NO2 = Mtp.loc[(Mtp["nom_station"]=="Montpellier - Prés d Arènes Urbain") & (Mtp["nom_poll"]=="NO2"),["valeur","date_debut"]]
Date = Mtp_PA_NO2["date_debut"]
Releve = Mtp_PA_NO2["valeur"]


# Création du DatFrame

data = {
    'Date': Date,
    'Valeur1': Releve
}
df = pd.DataFrame(data)
df = df.sort_values(by=['Date'], ascending=[True])
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d %H:%M:%S%z')

# Création du graphique avec les dates en abscisse et les valeurs en ordonnée

plt.figure(figsize=(20, 6))
plt.plot(df['Date'], df['Valeur1'], label='Valeur1',ls='-')

# Spécifiez les emplacements des ticks (ici, tous les jours)
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Faites pivoter les labels des dates pour une meilleure lisibilité
plt.xticks(rotation=45)

# Ajouter des étiquettes aux axes et un titre
plt.xlabel('Dates')
plt.ylabel('Relevé (en $\mu g/m^3$)')
plt.title('Concentration en $NO_2$ - Montpellier Près d\'Arènes')

# Afficher le graphique
plt.tight_layout()
plt.show()

#
#
#
#
#
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import plotly.express as px

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
# print(table(Mtp,"Montpellier - Prés d Arènes Urbain"))

# Trace sur un même graphique les courbes des rélevés pour les polluants (à cocher)



def Trace_px(donnees,station) :
    df = table(donnees,station)
    fig = px.line(df, width=1000, height=500,
     title = "Concentration - " + station,
     labels=dict(value='Concentration (µg/m³)', variable='Polluant'))
    fig.show()


# test
Trace_px(Mtp,"Montpellier - Prés d Arènes Urbain")

#
#
#
#