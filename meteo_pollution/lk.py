import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = '../Mesure_annuelle_Region_Occitanie_Polluants_Principaux (1).csv'
df = pd.read_csv(file_path, encoding='UTF-8-SIG')
print(df.head())
import matplotlib.pyplot as plt
import seaborn as sns

# Filter the DataFrame for PM10 pollutant
pm10_data = df[df['nom_poll'] == 'PM10']

# Group the data by typology and date, and calculate the mean value
pm10_typology = pm10_data.groupby(['typologie', 'date_debut'])['valeur'].mean().reset_index()

# Convert date_debut to datetime for proper plotting
pm10_typology['date_debut'] = pd.to_datetime(pm10_typology['date_debut'])

# Sort the data by date_debut
pm10_typology.sort_values(by='date_debut', inplace=True)

# Plotting
plt.figure(figsize=(15, 7))
sns.lineplot(data=pm10_typology, x='date_debut', y='valeur', hue='typologie', marker='o')
plt.title('Variation of PM10 Levels by Typology Over Time')
plt.xlabel('Date')
plt.ylabel('Mean PM10 Value (ug/m^3)')
plt.xticks(rotation=45)
plt.legend(title='Typology')
plt.tight_layout()
plt.savefig("lk.png")
plt.show()