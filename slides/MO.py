import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'Mesure_annuelle_Region_Occitanie_Polluants_Principaux (1) (1).csv'
df = pd.read_csv(file_path, delimiter=';')
print(df.head())