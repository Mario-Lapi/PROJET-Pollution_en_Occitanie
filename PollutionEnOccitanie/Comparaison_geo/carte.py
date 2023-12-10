#%%

import folium
import pandas as pd
import math
import csv

# Créer une carte focus sur la région
m = folium.Map(location=[43.6000,1.4400], zoom_start=8,tiles='CartoDB Positron', attr='CartoDB Positron')

# Découper la carte en départements 
geojson_url = 'https://france-geojson.gregoiredavid.fr/repo/regions/occitanie/departements-occitanie.geojson'
folium.GeoJson(geojson_url, name='occitanie').add_to(m)

# Nom du fichier CSV
nom_fichier_csv = 'Mesure_annuelle_Region_Occitanie_Polluants_Principaux.csv'

# Ouvrir le fichier CSV en mode lecture
with open(nom_fichier_csv, newline='') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    l=[]
    data2=[]
    # Lire les lignes du fichier CSV
    for ligne in lecteur_csv:
        if ligne[3] not in l:
            l.append(ligne[3])
        data2.append(ligne)
# Regrouper les données de façon à les utiliser (une station par ville qui est la moyenne des autres stations sur la même ville)
data=[]
liste=[]
p=0
for ville in l[1:]:
    s=0
    n=0
    for ligne in data2:
        if ligne[3] == ville:
            s+=float(ligne[11])
            n+=1
            if ligne[3] not in liste:
                data.append(ligne)
            liste.append(ville)
    s=s/n
    data[p][11]=s
    p+=1
# Créer un data utilisable par folium
lat=[]
lon=[]
name=[]
value=[]     
for ligne in data:
    lat.append(float(ligne[1]))
    lon.append(float(ligne[0]))
    name.append(ligne[3])
    value.append(float(ligne[11]))
data3 = pd.DataFrame({
   'lat':lat,
   'lon':lon,
   'name':name,
   'value':value
})

#Création de cercles proportionnels à la mesure de pm10 présent par ville
for city in data3.itertuples():
    local_deformation = math.cos(city.lat * math.pi / 180)
    folium.Circle(
        location=[city.lat, city.lon],
        popup=folium.Popup(f"{city.value} µm/m³"),
        tooltip=folium.Tooltip(city.name),
        radius=city.value * 800.0 * local_deformation, #le facteur 800 est choisit arbitrairement
        color='purple',
        fill=True,
        fill_color='purple'
    ).add_to(m)


# Enregistrer la carte en tant que fichier HTML
m.save('ma_carte.html')