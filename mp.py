import pandas as pd
from tqdm.auto import tqdm

tqdm.pandas()

# Load the CSV file with the correct delimiter and skip bad lines
file_path = 'donnees-synop-essentielles-omm (3).csv'
df = pd.read_csv(file_path, delimiter=';')

# Display the head of the dataframe to get an initial sense of the data
print(df.head())
# Re-import pandas and reload the CSV file with the correct delimiter
import pandas as pd
from tqdm.auto import tqdm

tqdm.pandas()


df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Re-run the previous code to plot the graph
# Convert 'Pression station' and 'Niveau barométrique' to numeric, coerce errors to NaN
df['Pression station'] = pd.to_numeric(df['Pression station'], errors='coerce')
df['Niveau barométrique'] = pd.to_numeric(df['Niveau barométrique'], errors='coerce')

# Drop rows where 'Pression station' or 'Niveau barométrique' is NaN after conversion
df.dropna(subset=['Pression station', 'Niveau barométrique', 'Date'], inplace=True)

# Sort the dataframe by date
df.sort_values('Date', inplace=True)

# Plotting both 'Pression station' and 'Niveau barométrique' over time
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Pression station'], label='Pression station')
plt.plot(df['Date'], df['Niveau barométrique'], label='Niveau barométrique', alpha=0.7)
plt.title('Station Pressure and Barometric Level Over Time')
plt.xlabel('Date')
plt.ylabel('Pressure (hPa)')
plt.legend()
plt.grid(True)
plt.show()