#%%
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

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
        'Valeurs': Valeurs
    }
    df = pd.DataFrame(data)
    df = df.sort_values(by=['Dates'], ascending=[True])
    return df
    
# test
# print(extraction(Mtp,"Montpellier - Prés d Arènes Urbain", "NO2"))

# Trace sur un même graphique les courbes des rélevés pour la liste des pollunants choisis

def Trace(donnees,station,list_poll) :
    plt.figure(figsize=(20, 6))
    for i in list_poll :
        df = extraction(donnees,station,i)
        plt.plot(df['Dates'], df['Valeurs'], label=i,ls='-')
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())  # ticks tous les jours
        plt.xticks(rotation=45)  # Pivoter les labels
        plt.xlabel('Dates')
        plt.ylabel('Relevé (en $\mu g/m^3$)') 
        plt.legend()
    plt.title("Concentration - " + station) # à revoir pour adapter
    plt.tight_layout()
    plt.show()


# test
# Trace(Mtp,"Montpellier - Prés d Arènes Urbain", ["NO2","PM10"))

# %%
