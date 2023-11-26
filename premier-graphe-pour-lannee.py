# %%
import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL des données
url = "https://services9.arcgis.com/7Sr9Ek9c1QTKmbwr/arcgis/rest/services/mesures_occitanie_mensuelle_poll_princ/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

# Attributs que vous souhaitez inclure dans le DataFrame final
selected_attributes = ['nom_com', 'nom_poll', 'valeur', 'date_debut']

# Fonction pour récupérer les données pour la ville de Toulouse et les stocker dans un DataFrame
def get_data_for_toulouse(url, selected_attributes):
    # Récupération des données depuis l'URL
    response = requests.get(url)
    
    # Vérification du succès de la requête
    if response.status_code == 200:
        data = response.json()
        
        # Extraction des caractéristiques des données
        features = data.get('features', [])
        
        # Filtrer les données pour la ville de Toulouse
        toulouse_data = [feature['properties'] for feature in features if feature['properties']['nom_com'] == 'TOULOUSE']
        
        # Exclure les lignes où la case 'valeur' est vide
        toulouse_data = [entry for entry in toulouse_data if entry.get('valeur') is not None]
        
        # Convertir le format de la date
        for entry in toulouse_data:
            entry['date_debut'] = pd.to_datetime(entry['date_debut'], unit='ms')  # 'ms' pour les millisecondes
        
        # Création d'un DataFrame à partir des caractéristiques filtrées et sélection des attributs spécifiques
        df = pd.DataFrame(toulouse_data, columns=selected_attributes)
        
        return df
    else:
        print(f"Erreur de requête avec le code {response.status_code}")
        return None

# Appel de la fonction pour obtenir le DataFrame pour la ville de Toulouse avec des attributs sélectionnés et excluant les lignes où 'valeur' est vide
toulouse_data_frame = get_data_for_toulouse(url, selected_attributes)

# Convertir la colonne 'valeur' en un type numérique
toulouse_data_frame['valeur'] = pd.to_numeric(toulouse_data_frame['valeur'], errors='coerce')

# Grouper par mois et par polluant, calculer la moyenne
average_data = toulouse_data_frame.groupby(['nom_poll', toulouse_data_frame['date_debut'].dt.to_period("M")])['valeur'].mean().reset_index()

# Tracer des courbes pour chaque polluant
plt.figure(figsize=(10, 6))
for pollutant in average_data['nom_poll'].unique():
    data = average_data[average_data['nom_poll'] == pollutant]
    plt.plot(data['date_debut'].dt.to_timestamp(), data['valeur'], label=pollutant, marker='o')

plt.title('Moyenne de concentration des polluants à Toulouse par mois')
plt.xlabel('Date')
plt.ylabel('Moyenne de Concentration')
plt.legend()
plt.show()
#ctest