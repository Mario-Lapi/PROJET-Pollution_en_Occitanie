import folium
from folium import plugins
import csv

# Créer une carte focus sur la région
m = folium.Map(location=[43.6000,1.4400], zoom_start=8,tiles='CartoDB Positron', attr='CartoDB Positron')

# Découper la carte en départements 
geojson_url = 'https://france-geojson.gregoiredavid.fr/repo/regions/occitanie/departements-occitanie.geojson'
folium.GeoJson(geojson_url, name='occitanie').add_to(m)

# Créer les poinst chef-lieux que nous utiliserons
    # On donne une localisation centrale à ces points
    # La concentration correspond aux valeurs dans le fichier 'villes.PM10.ccsv'
points_interet = [
    {'location': [43.6047, 1.4442], 'popup': 'Toulouse', 'concentration':16.0},
    {'location': [43.6116, 3.8770], 'popup': 'Montpellier', 'concentration':17.2},
    {'location': [42.9833, 1.1500], 'popup': 'Saint-Girons', 'concentration':11.9},
    {'location': [44.3333, 2.5667], 'popup': 'Rodez', 'concentration':11.2},
    {'location': [43.8333, 4.3500], 'popup': 'Nîmes', 'concentration':14.4},
    {'location': [43.6500, 0.5833], 'popup': 'Auch', 'concentration':13.1},
    {'location': [43.2333, 0.0833], 'popup': 'Tarbes', 'concentration':13.2},
    {'location': [42.6833, 2.8833], 'popup': 'Perpignan', 'concentration':20.9},
    {'location': [43.9333, 2.1500], 'popup': 'Albi', 'concentration':13.5},
    {'location': [44.0167, 1.3500], 'popup': 'Montauban', 'concentration':14.0}
]

# Extraire les coordonnées et les concentrations des points d'intérêt
locations = [point['location'] for point in points_interet]
concentrations = [point['concentration'] for point in points_interet]

#Classe de fonctions pour définir les points selon leur taux de pollution
class Point:
    def __init__(self,locations=list,concentrations=list):
        self.loc=locations
        self.concs=concentrations
    
    def weights(self): # Normaliser les concentrations pour les utiliser comme poids
        max_concs=max(self.concs)
        return[conc/max_concs for conc in self.concs]

l=[]
for point in points_interet:
    # Vérifier que le point a des coordonnées valides
    if isinstance(point['location'], list) and len(point['location']) == 2 :
        # Ajouter les coordonnées à la liste 'l'
        l.append(point['location'])
        folium.map.Marker(
            location=point['location'],
            popup=folium.Popup(point['concentration']),
            tooltip=folium.Tooltip(point['popup']),
        ).add_to(m)

exemple=Point(locations,concentrations)
liste=exemple.weights()
truc=[]
for value in liste:
    value=value*25
    truc.append(value)

plugins.HeatMap(l, name='HeatMap', min_opacity=0.5, max_zoom=18, radius=truc, blur=15, gradient=None, overlay=True, control=True, show=True).add_to(m)

print(l)
print(truc)
for point in points_interet:
    print(point['concentration'])

# Enregistrer la carte en tant que fichier HTML
m.save('ma_carte.html')