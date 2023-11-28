import folium
from IPython.display import IFrame
from folium import plugins

# Créer une carte
m = folium.Map(location=[43.6000,1.4400], zoom_start=8,tiles='CartoDB Positron', attr='CartoDB Positron')

geojson_url = 'https://france-geojson.gregoiredavid.fr/repo/regions/occitanie/departements-occitanie.geojson'
folium.GeoJson(geojson_url, name='occitanie').add_to(m)

# Ajouter des points de couleur à la carte
points_interet = [
    {'location': [43.6047, 1.4442], 'popup': 'Toulouse'},
    {'location': [43.6116, 3.8770], 'popup': 'Montpellier'},
    {'location': [42.9833, 1.1500], 'popup': 'Saint-Girons'},
    {'location': [44.3333, 2.5667], 'popup': 'Rodez'},
    {'location': [43.8333, 4.3500], 'popup': 'Nîmes'},
    {'location': [43.6500, 0.5833], 'popup': 'Auch'},
    {'location': [43.2333, 0.0833], 'popup': 'Tarbes'},
    {'location': [42.6833, 2.8833], 'popup': 'Perpignan'},
    {'location': [43.9333, 2.1500], 'popup': 'Albi'},
    {'location': [44.0167, 1.3500], 'popup': 'Montauban'}
]

#Fonction pour définir la taille du point selon le taux de pollution
def diam(point):
    return 5000

#for point in points_interet:
    folium.Circle(
        location=point['location'],
        radius=diam(point),
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.5,
        popup=point['popup']
    ).add_to(m)

l=[]
for point in points_interet:
    # Vérifier que le point a des coordonnées valides
    if isinstance(point['location'], list) and len(point['location']) == 2:
        folium.Marker(
            location=point['location'],
            popup=point['popup'],
            icon=folium.Icon(color='red')
        ).add_to(m)
        l.append(point['location'])
plugins.HeatMap(l, name=None, min_opacity=0.5, max_zoom=18, radius=5000, blur=15, gradient=None, overlay=True, control=True, show=True).add_to(m)


# Enregistrer la carte en tant que fichier HTML
m.save('ma_carte.html')

#on va utiliser le pm10 seulement, points sur les chefs lieu, station "urbain"
#Kenewy s'occupe du traitement de données
#délimiter les départements aussi et rendre visible les chefs lieux qu'on va étudier
#faire des points plus jolis (type "difusuion" ?)