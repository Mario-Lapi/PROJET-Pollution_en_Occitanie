import pandas as pd
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
file_path = './donnees-synop-essentielles-omm (1).csv'
df = pd.read_csv(file_path, sep=';', parse_dates=['Date'], dayfirst=True)

# Selecting relevant columns for correlation
# Assuming 'Température' for temperature, 'Humidité' for humidity, and 'Pression au niveau mer' for atmospheric pressure
relevant_columns = ['Température', 'Humidité', 'Pression au niveau mer']
df = df[relevant_columns].dropna()

# Pairplot to visualize the relationships between variables
sns.pairplot(df, diag_kind='kde')
plt.savefig("meteo.png")
plt.show()