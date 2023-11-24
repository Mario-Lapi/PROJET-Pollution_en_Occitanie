import folium
from IPython.display import IFrame

# Créer une carte
m = folium.Map(location=[43.6000,1.4400], zoom_start=8,tiles='CartoDB Positron', attr='CartoDB Positron')

geojson_url = 'https://france-geojson.gregoiredavid.fr/repo/regions/occitanie/region-occitanie.geojson'
folium.GeoJson(geojson_url, name='occitanie').add_to(m)

# Ajouter des points de couleur à la carte
points_interet = [
    {'location': [43.6047, 1.4442], 'popup': 'Toulouse'},
    {'location': [43.6116, 3.8770], 'popup': 'Montpellier'}
]

#Fonction pour définir la taille du point selon le taux de pollution
def diam(point):
    return 5000

#Fonction pour définir la couleur du point selon le taux de pollution
def color(point):
    return 'red'

for point in points_interet:
    folium.Circle(
        location=point['location'],
        radius=diam(point),
        color=color(point),
        fill=True,
        fill_color=color(point),
        fill_opacity=0.5,
        popup=point['popup']
    ).add_to(m)

# Enregistrer la carte en tant que fichier HTML
m.save('ma_carte.html')
m

#on va utiliser le pm10 seulement, points sur les chefs lieu, station "urbain"
#Kenewy s'occupe du traitement de données
#délimiter les départements aussi et rendre visible les chefs lieux qu'on va étudier
#faire des points plus jolis (type "difusuion" ?)