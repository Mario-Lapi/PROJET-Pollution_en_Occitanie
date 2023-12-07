#%%
import requests
import pandas as pd
import plotly.graph_objects as go

def tracegraph(url, selected_attributes, city_name):
    # Fonction pour récupérer les données de pollution
    def get_pollution_data(url, selected_attributes, city_name):
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            features = data.get('features', [])
            city_data = [feature['properties'] for feature in features if feature['properties']['nom_com'] == city_name]
            city_data = [entry for entry in city_data if entry.get('valeur') is not None]
            
            for entry in city_data:
                entry['date_debut'] = pd.to_datetime(entry['date_debut'], unit='ms')
            
            df = pd.DataFrame(city_data, columns=selected_attributes)
            return df
        else:
            print(f"Erreur de requête avec le code {response.status_code}")
            return None
    
    # Appel de la fonction pour récupérer les données
    city_data_frame = get_pollution_data(url, selected_attributes, city_name)

    # Convertir la colonne 'valeur' en un type numérique
    city_data_frame['valeur'] = pd.to_numeric(city_data_frame['valeur'], errors='coerce')

    # Grouper par mois et par polluant, calculer la moyenne
    average_data = city_data_frame.groupby(['nom_poll', city_data_frame['date_debut'].dt.to_period("M")])['valeur'].mean().reset_index()

    # Créer une figure interactive Plotly
    fig = go.Figure()

    # Tracer des courbes pour chaque polluant
    for pollutant in average_data['nom_poll'].unique():
        data = average_data[average_data['nom_poll'] == pollutant]
        fig.add_trace(go.Scatter(x=data['date_debut'].dt.to_timestamp(), y=data['valeur'], mode='lines+markers', name=pollutant))

    # Configurer la mise en page interactive
    fig.update_layout(title=f'Moyenne de concentration des polluants à {city_name} par mois ',
                      xaxis_title='Date',
                      yaxis_title='Moyenne de Concentration en μg/m3',
                      xaxis=dict(type='date'),
                      xaxis_rangeslider_visible=True)

    # Afficher la figure interactive
    fig.show()



# %%
