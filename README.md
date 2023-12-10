# Pollution en Occitanie

## Résumé

"Pollution en Occitanie" est un projet de visualisation de données de pollution atmosphérique dans les zones urbaines de la région Occitanie sur les cinq dernières années. Les polluants observés sont :

- Les oxydes d'azote (NOx), regroupant le monoxyde et le dioxyde d'azote (NO et NO2)
- L'ozone (O3)
- Les particules fines (PM10 et PM2.5)

 Les données de pollution sont fournies par : 

- Occitanie pollution datasets: [Atmo Occitanie](https://data-atmo-occitanie.opendata.arcgis.com/pages/liste-des-flux)

Elles sont mises en relation avec des données météorologiques fournies par : 

- Weather forecast: [SYNOP data](https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/api/?sort=date)


## Site internet

Le site est accessible à partir de l'URL suivant :

<https://cmottier.github.io/PROJET-Pollution_en_Occitanie/>


## Descriptif

Le site contient différents objets de visualisation permettant les observations suivantes :

- Comparaison géographique de différentes villes de dix départements de la région Occitanie (données manquantes pour trois départements).
- Comparaison temporelle des concentrations des principaux polluants au sein des chefs-lieux des départements. 

## Modules Python utilisés


Voici les modules Python utilisés pour ce projet :

- Pandas : manipulations de Dataframe
- Matplotlib, Plotly, Seaborn, tqdm : création de graphiques intéractifs
- Folium : création de carte
- Requests : importation de données en ligne

## Modules Python créés

Pour les graphiques :

- Horloge.py : moyennes de concentrations par heures
- Month_resume.py : résumé des données journalières sur un mois
- Month.py : représentation des données horaires sur un mois
- Tracegraph.py : concentratitons mensuelles sur un an
- meteo_pollution : relation entre la meteo et la pollution de l'air

  Pour la carte : 
- Carte.py : construction de la carte intéractive

Ils sont regroupés dans le dossier PollutionEnOccitanie. 

## Auteurs

- Khadidiatou Kenewy DIALLO : [khadidiatou-kenewy.diallo@etu.umontpellier.fr](mailto:khadidiatou-kenewy.diallo@etu.umontpellier.fr),
- Mario LAPI : [mario.lapi@etu.umontpellier.fr](mailto:mario.lapi@etu.umontpellier.fr),
- Jeanne MANNEQUIN : [jeanne.mannequin@etu.umontpellier.fr](mailto:jeanne.mannequin@etu.umontpellier.fr),
- Camille MOTTIER : [camille.mottier@etu.umontpellier.fr](mailto:camille.mottier@etu.umontpellier.fr).