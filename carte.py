import folium
import json

m = folium.Map(
    location=[43.5000, 1.3600],
    zoom_start=9,
    tiles=None,
)
folium.Marker(location=[43.5, 1.3], titles='Occitanie').add_to(m)

m
