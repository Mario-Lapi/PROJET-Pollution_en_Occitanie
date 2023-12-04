
#%%
<<<<<<< HEAD
=======

>>>>>>> faa0f0216343fbf98ce35ad9dd7ad15883c642ab
import requests
import pandas as pd
import matplotlib.pyplot as plt

def tracegraph(url, selected_attributes, city_name):
    # Fonction pour récupérer les données de pollution
    def get_pollution_data(url, selected_attributes, city_name):
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            features = data.get('features', [])
            city_data = [feature['properties'] for feature in features if feature['properties']['nom_com'] == city_name]
            city_data = [entry for entry in city_data if entry.get('valeur') is not None]
            
            for entry in city_data:
                entry['date_debut'] = pd.to_datetime(entry['date_debut'], unit='ms')
            
            df = pd.DataFrame(city_data, columns=selected_attributes)
            return df
        else:
            print(f"Erreur de requête avec le code {response.status_code}")
            return None
    
    # Appel de la fonction pour récupérer les données
    city_data_frame = get_pollution_data(url, selected_attributes, city_name)

    # Convertir la colonne 'valeur' en un type numérique
    city_data_frame['valeur'] = pd.to_numeric(city_data_frame['valeur'], errors='coerce')

    # Grouper par mois et par polluant, calculer la moyenne
    average_data = city_data_frame.groupby(['nom_poll', city_data_frame['date_debut'].dt.to_period("M")])['valeur'].mean().reset_index()

    # Tracer des courbes pour chaque polluant
    plt.figure(figsize=(10, 6))
    for pollutant in average_data['nom_poll'].unique():
        data = average_data[average_data['nom_poll'] == pollutant]
        plt.plot(data['date_debut'].dt.to_timestamp(), data['valeur'], label=pollutant, marker='o')

    plt.title(f'Moyenne de concentration des polluants à {city_name} par mois ')
    plt.xlabel('Date')
    plt.ylabel('Moyenne de Concentration en μg/m3')
    plt.legend()
    plt.show()

# %%
