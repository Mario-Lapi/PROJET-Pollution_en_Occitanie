import folium
from folium import plugins
import pandas as pd
import math

# Créer une carte focus sur la région
m = folium.Map(location=[43.6000,1.4400], zoom_start=8,tiles='CartoDB Positron', attr='CartoDB Positron')

# Découper la carte en départements 
geojson_url = 'https://france-geojson.gregoiredavid.fr/repo/regions/occitanie/departements-occitanie.geojson'
folium.GeoJson(geojson_url, name='occitanie').add_to(m)

# Créer les poinst chef-lieux que nous utiliserons
    # On donne une localisation centrale à ces points
    # La concentration correspond aux valeurs dans le fichier 'villes.PM10.ccsv'
data = pd.DataFrame({
   'lat':[43.6047, 43.6116, 42.9833, 44.3333, 43.8333, 43.6500, 43.2333, 42.6833, 43.9333, 44.0167],
   'lon':[1.4442, 3.8770, 1.1500, 2.5667, 4.3500, 0.5833, 0.0833, 2.8833, 2.1500, 1.3500],
   'name':['Toulouse', 'Montpellier', 'Saint-Girons', 'Rodez', 'Nîmes', 'Auch', 'Tarbes', 'Perpignan', 'Albi', 'Montauban'],
   'value':[16.0, 17.2, 11.9, 11.2, 14.4, 13.1, 13.2, 20.9, 13.5, 14.0]
})

for city in data.itertuples():
    local_deformation = math.cos(city.lat * math.pi / 180)
    folium.Circle(
        location=[city.lat, city.lon],
        popup=city.value,
        tooltip=folium.Tooltip(city.name),
        radius=city.value * 800.0 * local_deformation,
        color='crimson',
        fill=True,
        fill_color='crimson'
    ).add_to(m)


# Enregistrer la carte en tant que fichier HTML
m.save('ma_carte.html')
m