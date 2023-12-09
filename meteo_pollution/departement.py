
import pandas as pd

# Spécifiez le chemin vers votre fichier CSV
file_path = '../Mesure_annuelle_Region_Occitanie_Polluants_Principaux (1).csv'

# Lisez le fichier CSV en utilisant Pandas
df = pd.read_csv(file_path, sep=';', parse_dates=['Date'], dayfirst=True)

# Utilisez le dataframe 'df' pour effectuer des opérations ou des manipulations de données


selected_cities = ['Rodez', 'Nîmes', 'Toulouse', 'Auch', 'Montpellier', 'Tarbes', 'Perpignan', 'Albi', 'Montauban', 'Saint-Girons']
df_selected_cities_pm10 = df_polluants[(df_polluants['nom_com'].isin(selected_cities)) & (df_polluants['nom_poll'] == 'PM10')]
# Selecting the relevant columns
df_selected_cities_pm10 = df_selected_cities_pm10[['nom_com', 'code_station', 'valeur']]

# Save the filtered data to a CSV file
df_selected_cities_pm10.to_csv('/mnt/data/Selected_Cities_PM10_Data.csv', index=False)

# Display the head of the filtered dataframe
tqdm.pandas(desc='Displaying the head of the filtered dataframe')
print(df_selected_cities_pm10.head())