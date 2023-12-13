import pandas as pd

df_temperature = pd.read_csv('donnees-synop-essentielles-omm (2).csv')
print(df_temperature.head())

df_polluants = pd.read_csv('Mesure_annuelle_Region_Occitanie_Polluants_Principaux (1) (1).csv')
print(df_polluants.head())

import matplotlib.pyplot as plt

# Filter the temperature data for Montpellier
montpellier_temp = df_temperature[df_temperature['Nom'] == 'MONTPELLIER']

# Filter the pollutant data for Montpellier and for the pollutant 'O3' which stands for Ozone
montpellier_ozone = df_polluants[(df_polluants['nom_com'] == 'MONTPELLIER') & (df_polluants['nom_poll'] == 'O3')]

# Convert date columns to datetime
montpellier_temp['Date'] = pd.to_datetime(montpellier_temp['Date'], format='%Y%m%d%H%M%S')
montpellier_ozone['date_debut'] = pd.to_datetime(montpellier_ozone['date_debut'])

# Group the data by date and calculate mean temperature and ozone levels
montpellier_temp_grouped = montpellier_temp.groupby(montpellier_temp['Date'].dt.date).agg({'Température':'mean'})
montpellier_ozone_grouped = montpellier_ozone.groupby(montpellier_ozone['date_debut'].dt.date).agg({'valeur':'mean'})

# Merge the two datasets on the date
montpellier_merged = pd.merge(montpellier_temp_grouped, montpellier_ozone_grouped, left_index=True, right_index=True, how='inner')

# Plotting
plt.figure(figsize=(14,7))
plt.title('Daily Mean Temperature and Ozone Levels in Montpellier')
plt.plot(montpellier_merged.index, montpellier_merged['Température'], label='Mean Temperature (°C)', color='blue')
plt.plot(montpellier_merged.index, montpellier_merged['valeur'], label='Ozone Level', color='red')

plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
