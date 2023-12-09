import pandas as pd

# Load the provided CSV file into a dataframe
df = pd.read_csv('../donnees-synop-essentielles-omm (3).csv')

# Display the head of the dataframe to get an initial sense of the data
print(df.head())
import matplotlib.pyplot as plt

# Convert 'Date' to datetime and sort the dataframe by date
# It's important for time series visualization to have the data sorted by date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df.sort_values('Date', inplace=True)

# Drop rows where 'Nebulosité totale' or 'Date' is NaN after conversion
# This is necessary to avoid errors during plotting
df.dropna(subset=['Nebulosité totale', 'Date'], inplace=True)

# Plotting the total cloud cover ('Nebulosité totale') over time
plt.figure(figsize=(14, 7))
df.plot(x='Date', y='Nebulosité totale', kind='line', ax=plt.gca())
plt.title('Total Cloud Cover Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cloud Cover')
plt.grid(True)
plt.show()