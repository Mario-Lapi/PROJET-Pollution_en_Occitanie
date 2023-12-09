





import pandas as pd
from tqdm.auto import tqdm
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'donnees-synop-essentielles-omm (1).csv'
df = pd.read_csv(file_path, sep=';', parse_dates=['Date'], dayfirst=True)

# Convert 'Date' to datetime and sort the DataFrame by 'Date'
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
df.sort_values('Date', inplace=True)

# Plotting temperature over time
plt.figure(figsize=(15, 5))
plt.plot(df['Date'], df['Température'], label='Temperature')
plt.title('Temperature over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature.png")
plt.show() 
