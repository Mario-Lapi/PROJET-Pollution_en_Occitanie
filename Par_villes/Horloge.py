#%%

import pandas as pd
import calendar
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from Month import *

#%%
data = pd.read_csv("Mesure_horaire_(30j)_Region_Occitanie_Polluants_Reglementaires.csv")

station = 'Montpellier - Prés d Arènes Urbain'

df = table(data, station)

df["jour_semaine"] = df.index.day_of_week
df["heure"] = df.index.hour
df_semaine = df.loc[(df["jour_semaine"] < 5 ),:]
df_semaine = df_semaine.drop('jour_semaine', axis = 1)

df_semaine_polar = (
    df_semaine.groupby(["heure"])
    .mean()
    .reset_index()
)

df_semaine_polar = df_semaine_polar.astype({"heure": str}, copy=False)


fig = px.line_polar(
    df_semaine_polar,
    r="NO2",
    theta="heure",
    # color="jour_semaine",
    # line_close=True,
    range_r=[0, 50],
    # start_angle=0,
    # # color_discrete_sequence=colors,
    # template="seaborn",
    # title="Daily accident profile: weekday effect?",
)
fig.show()

# df_polar["jour_semaine"] = df_polar["jour_semaine"].apply(lambda x: calendar.day_abbr[x])


# n_colors = 8  # 7 days, but 8 colors help to have weekends days' color closer
# colors = px.colors.sample_colorscale(
#     "mrybm", [n / (n_colors - 1) for n in range(n_colors)]
# )

# for i in df_semaine_polar.columns[1:] :
#     fig_add = px.line_polar(
#         df_semaine_polar,
#         r=i,
#         theta="heure",
#     # color="jour_semaine",
#     # line_close=True,
#         range_r=[0, 50],
#     # start_angle=0,
#     # # color_discrete_sequence=colors,
#     # template="seaborn",
#     # title="Daily accident profile: weekday effect?",
#         fig.show()
#     )





# %%
