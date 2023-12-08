import pandas as pd
# Load the CSV file into a DataFrame
import pandas as pd
from tqdm.notebook import tqdm

tqdm.pandas()

# Load the CSV file into a DataFrame using the correct delimiter
file_path = 'donnees-synop-essentielles-omm (3).csv'
df = pd.read_csv(file_path, delimiter=';')
print(df.head())  # Exemple : affiche les premières lignes pour vérification
   
# Display the first few rows of the dataframe
df.head()

import matplotlib.pyplot as plt

# Convert 'Date' to datetime and sort the DataFrame by date
# It's important for time series data to be in the correct order
# We use 'coerce' to handle any invalid parsing

# First, let's ensure the 'Date' column is in datetime format
# We'll also sort the data by 'Date'
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.sort_values('Date')

# Now, let's plot the 'Pression au niveau mer' over time
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Pression au niveau mer'], label='Pression au niveau mer')
plt.title('Variation de la Pression au niveau de la mer au fil du temps')
plt.xlabel('Date')
plt.ylabel('Pression au niveau mer (Pa)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graph.png")
plt.show()
