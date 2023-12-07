import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Load the CSV file into a DataFrame
file_path = './Mesure_annuelle_Region_Occitanie_Polluants_Principaux (1).csv'
df = pd.read_csv(file_path, encoding='UTF-8-SIG')

# Filter the DataFrame for PM10 pollutant
pm10_data = df[df['nom_poll'] == 'PM10']

# Group by department and calculate the mean value of PM10
pm10_mean_by_dept = pm10_data.groupby('nom_dept')['valeur'].mean().reset_index()

# Sort the departments by the mean PM10 value
pm10_mean_by_dept_sorted = pm10_mean_by_dept.sort_values('valeur', ascending=False)

# Plotting
plt.figure(figsize=(10, 8))
sns.barplot(x='valeur', y='nom_dept', data=pm10_mean_by_dept_sorted, palette='viridis')
plt.title('Average PM10 Levels by Department in Occitanie')
plt.xlabel('Average PM10 Concentration (ug/m^3)')
plt.ylabel('Department')
plt.tight_layout()
plt.savefig("graph.png")
plt.show()
