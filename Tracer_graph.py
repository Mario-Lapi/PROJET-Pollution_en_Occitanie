#%%
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import plotly.express as px

#%%
#Exemple avec données pour Mtp Près d'Arènes et NO2 - Données téléchargées

Mtp = pd.read_csv("Donnees_pour_test.csv")

# Extraction renvoie un dataframe composé des dates et des valeurs relevées pour la station et le polluant choisis 

def extraction(donnees,station,polluant) :
    extrait = donnees.loc[(donnees["nom_station"] == station) & (donnees["nom_poll"] == polluant),["valeur","date_debut"]]
    Dates = extrait["date_debut"]
    Dates = pd.to_datetime(Dates, format = '%Y/%m/%d %H:%M:%S%z')
    Valeurs = extrait["valeur"]
    data = {
        'Dates': Dates,
        polluant: Valeurs
    }
    df = pd.DataFrame(data)
    df = df.sort_values(by=['Dates'], ascending=[True])
    return df

# test
# print(extraction(Mtp,"Montpellier - Prés d Arènes Urbain", "NO2"))

# extrac_multi renvoie un dataframe composé des colonnes : dates et les différents polluants en parallèle

def extrac_multi(donnees,station,list_pol) :
    df = extraction(donnees,station,list_pol[0])
    for i in range(1,len(list_pol)) :
        df = pd.merge(df, extraction(donnees,station,list_pol[i]), on = "Dates")
    return df.set_index(["Dates"])

# test
# print(extrac_multi(Mtp,"Montpellier - Prés d Arènes Urbain", ["NO2","NOX"]))

#%%

# Trace sur un même graphique les courbes des rélevés pour la liste des pollunants choisis

def Trace(donnees,station,list_poll) :
    plt.figure(figsize=(20, 8))
    df = extrac_multi(donnees,station,list_poll).set_index(["Dates"])
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())  # ticks tous les jours
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.xticks(rotation=45)  # Pivoter les labels
    plt.xlabel('Dates')
    plt.ylabel('Relevé (en $\mu g/m^3$)') 
    plt.plot(df)
    plt.legend(df)
    plt.title("Concentration - " + station) 
    plt.tight_layout()
    plt.show()


# test
# Trace(Mtp,"Montpellier - Prés d Arènes Urbain", ["NO2","PM10"])



# %%
