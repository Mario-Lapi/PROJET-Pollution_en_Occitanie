import pandas as pd
from tqdm.auto import tqdm
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = '../Mesure_annuelle_Region_Occitanie_Polluants_Principaux (1).csv'
df = pd.read_csv(file_path, encoding='UTF-8-SIG')

# Display the head of the DataFrame
df_head = df.head()
print(df_head)

# Create a pie chart for the distribution of pollution types
pollution_type_counts = df['nom_poll'].value_counts()
plt.figure(figsize=(10, 8))
pollution_type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Pollution Types in Occitanie Region')
plt.ylabel('')  # Hide y-label
plt.savefig("repartition des polluants.png")
plt.show()