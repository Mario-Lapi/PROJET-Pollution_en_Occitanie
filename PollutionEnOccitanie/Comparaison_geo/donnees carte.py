import pandas as pd

# Charger le fichier "donnees_annuelles.csv" dans un DataFrame
file_path = 'Mesure_annuelle_Region_Occitanie_Polluants_Principaux(1).csv'  # Mettez le chemin correct vers votre fichier CSV
df = pd.read_csv(file_path)
# Filter the DataFrame for the specified cities and pollutant PM10
selected_cities = ['SAINT-GIRONS', 'RODEZ', 'NIMES', 'TOULOUSE', 'AUCH', 'MONTPELLIER', 'TARBES', 'PERPIGNAN', 'ALBI', 'MONTAUBAN']
selected_pollutant = 'PM10'

# Normalize city names to uppercase to ensure proper matching
selected_cities = [city.upper() for city in selected_cities]

# Apply filters
filtered_df = df[(df['nom_com'].str.upper().isin(selected_cities)) & (df['nom_poll'] == selected_pollutant)]

# Selecting only relevant columns
filtered_df = filtered_df[['nom_com', 'code_station', 'nom_poll', 'valeur']]

# Display the filtered DataFrame
print(filtered_df.head())

# If there are more than 10 rows, let's create a CSV file for the user to download
if len(filtered_df) > 10:
    filtered_df.to_csv('filtered_pollutants_PM10.csv', index=False)
    print('Filtered data saved to file: filtered_pollutants_PM10.csv')