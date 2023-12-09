import matplotlib.pyplot as plt
import pandas as pd

# Lecture des données de pollution (O3) et de température
df_pollutant = pd.read_csv('Mesure_horaire_(30j)_Region_Occitanie_Polluants_Reglementaires (1).csv')
df_temperature = pd.read_csv('donnees-synop-essentielles-omm (4).csv', delimiter=';')

# Filtrage des données pour O3 et Montpellier
montpellier_o3 = df_pollutant[(df_pollutant['nom_poll'] == 'O3') & (df_pollutant['nom_com'] == 'MONTPELLIER')]
montpellier_o3['date_debut'] = pd.to_datetime(montpellier_o3['date_debut'], utc=True)

# Filtrage et conversion des données de température pour Montpellier
montpellier_temp = df_temperature[df_temperature["ID OMM station"] == 7643]
montpellier_temp['Date'] = pd.to_datetime(montpellier_temp['Date'], utc=True)

# Fusion des données sur la base des dates
merged_data = pd.merge(montpellier_o3, montpellier_temp, left_on='date_debut', right_on='Date')

# Sélection des colonnes pertinentes
merged_data = merged_data[['date_debut', 'valeur', 'Température']]

# Conversion de la température de Kelvin en Celsius
merged_data['Température_Celsius'] = merged_data['Température'] - 273.15

# Création du graphique
plt.figure(figsize=(12, 6))
plt.scatter(merged_data['Température_Celsius'], merged_data['valeur'])
plt.title('Corrélation entre la concentration d\'O3 et la température à Montpellier')
plt.xlabel('Température (°C)')
plt.ylabel('Concentration d\'O3 (μg/m³)')
plt.grid(True)
plt.savefig("c.png")
plt.show()
