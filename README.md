# Dashboard d'Analyse de Données

## User Guide

### Prérequis
- Python 3.8 ou supérieur
- Gestionnaire de paquets pip

### Installation
1. Cloner le dépôt
   ```bash
   git clone https://github.com/AdrienB23/DataProject.git
   cd DataProject
   .\.env\Scripts\activate
   ```
   
2. Si vous rencontrez des problèmes liés au téléchargement du fichier csv,:
- Rendez-vous sur [opendatasoft](https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/export/?sort=date&location=2,-0.52734,-0.17578&basemap=jawg.light&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJ0YyIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiNGRjUxNUEifV0sInhBeGlzIjoiZGF0ZSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImRvbm5lZXMtc3lub3AtZXNzZW50aWVsbGVzLW9tbSIsIm9wdGlvbnMiOnsic29ydCI6ImRhdGUifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D)
- Téléchargez le fichier en csv 
- Placez le fichier dans le dossier data/raw/

2. Créer un environnement virtuel
   ```bash
   python -m venv .env
   ```

3. Activer l'environnement virtuel
   - Windows :
     ```bash
     .env\Scripts\activate
     ```

4. Installer les dépendances
   ```bash
   pip install -r requirements.txt
   ```

### Lancement du Dashboard
1. Nettoyer les données : (Prérequis)
   ```bash
   python -m src.utils.clean_data
   ```
2. Lancer l'application :
   ```bash
   python main.py
   ```
4. Ouvrir votre navigateur à l'adresse : http://localhost:8050

## Data

### Source des données
Les données utilisées dans ce dashboard proviennent de [Source](https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/table/?sort=date&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJ0YyIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiNGRjUxNUEifV0sInhBeGlzIjoiZGF0ZSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImRvbm5lZXMtc3lub3AtZXNzZW50aWVsbGVzLW9tbSIsIm9wdGlvbnMiOnsic29ydCI6ImRhdGUifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D&location=2,-0.52734,-0.17578&basemap=jawg.light).

### Structure des données
- Données brutes (`data/raw/donnees-synop-essentielles-omm.csv`) :
  - Format : CSV
  - Période : 2010 - 2024

- Données nettoyées (`data/cleaned/clean_data.csv`) :
- Suppressions des colonnes inutilisées : 
   "Pression au niveau mer",
   "Variation de pression en 3 heures",
   "Point de rosée",
   "Visibilité horizontale",
   "Nebulosité totale",
   "Temps présent",
   "Temps passé 1",
   "Temps passé 2",
   "Nébulosité  des nuages de l' étage inférieur",
   "Hauteur de la base des nuages de l'étage inférieur",
   "Type des nuages de l'étage inférieur",
   "Type des nuages de l'étage moyen",
   "Type des nuages de l'étage supérieur",
   "Pression station",
   "Niveau barométrique",
   "Géopotentiel",
   "Variation de pression en 24 heures",
   "Hauteur totale de la couche de neige, glace, autre au sol",
   "Hauteur de la neige fraîche",
   "Periode de mesure de la neige fraiche",
   "Phénomène spécial 1",
   "Phénomène spécial 2",
   "Phénomène spécial 3",
   "Phénomène spécial 4",
   "Nébulosité couche nuageuse 1",
   "Type nuage 1",
   "Hauteur de base 1",
   "Nébulosité couche nuageuse 2",
   "Type nuage 2",
   "Hauteur de base 2",
   "Nébulosité couche nuageuse 3",
   "Type nuage 3",
   "Hauteur de base 3",
   "Nébulosité couche nuageuse 4",
   "Type nuage 4",
   "Hauteur de base 4",
   "Type de tendance barométrique",
   "Temps passé 1",
   "Temps présent",
   'Température minimale sur 12 heures (°C)',
   'Température minimale sur 24 heures (°C)',
   'Température maximale sur 12 heures (°C)',
   'Température maximale sur 24 heures (°C)',
   'Température minimale du sol sur 12 heures (en °C)',
   'Etat du sol',
   'Précipitations dans la dernière heure',
   'Précipitations dans les 3 dernières heures',
   'Précipitations dans les 6 dernières heures',
   'Précipitations dans les 12 dernières heures',
   'Altitude',
   "Température minimale sur 12 heures",
   "Température minimale sur 24 heures",
   "Température maximale sur 24 heures",
   "Température minimale du sol sur 12 heures",
   "Méthode de mesure Température du thermomètre mouillé",
   "Température du thermomètre mouillé",
   "Periode de mesure de la rafale",
   "Type de tendance barométrique.1",
   "Temps passé 1.1",
   "Temps présent.1",

### Architecture du Code

```
data_project/
├── config.py              # Configuration globale
├── data/                  # Données
├── src/                   # Code source
│   ├── components/        # Composants réutilisables
│   ├── pages/             # Pages du dashboard
│   └── utils/             # Fonctions utilitaires
```

### Ajouter une Nouvelle Page

1. Créer un nouveau fichier dans `src/pages/`
   ```python
   # src/pages/new_page.py
   from dash import html, dcc
   from ..components import create_header, create_footer

   layout = html.Div([
       create_header(),
       # Votre contenu ici
       create_footer()
   ])
   ```

2. Ajouter la route dans `main.py`
   ```python
   from src.pages import new_page

   @app.callback(
       Output('page-content', 'children'),
       [Input('url', 'pathname')]
   )
   def display_page(pathname):
       if pathname == '/new':
           return new_page.layout
   ```
   
### Ajouter un nouveau graphique

1. Créer une nouvelle fonction dans `src/utils/graphs_functions.py`
   ```python
   import plotly.graph_objects as go
   import pandas as pd
   def create_graph(df):
      traces = [go.Scatter(
         # Votre Trace ici
      )]

      layout = go.Layout(
         # Votre Layout ici
      )

      fig = go.Figure(data=traces, layout=layout)
      return fig
   ```

2. Créer un nouveau fichier dans `src/components/graphs`
   ```python
   from dash import html, dcc
   from src.utils.data_loader import df_cleaned
   from src.utils.graphs_functions import create_graph
   def create_layout():
      fig = create_graph()
      return html.Div(
         children=[
            # Votre contenue ici

            dcc.Graph(
               figure=fig
            )
         ]
    )
   ```

3. Ajouter le composant dans `src/components/main_component.py`
```python
   from src.components.graphs import create_layout
   from dash import html
   def create_main() -> html.Main:
      return html.Main([
         create_layout()
         # Les autres graphiques/Map ici
      ])
```

## Rapport d'analyse

1. Tendance Générale
L'analyse des températures moyennes, des précipitations et de la vitesse du vent sur la période 2010-2024 révèle des tendances marquées dans chaque catégorie.

- Températures : Les températures maximales et minimales ont montré une tendance à la hausse dans la plupart des régions. Cette tendance au réchauffement est observée globalement, bien que plus prononcée dans certaines régions comme Occitanie ou Provence-Alpes-Côte d'Azur, où les hausses sont plus significatives comparativement aux autres régions.

- Précipitations : Des périodes de sécheresses suivit de périodes très humides sont observés dans certaines régions, comme en Guyane ou encore à la Réunion, tandis que d'autres régions ont montré une stabilité relative dans les précipitations..

- Vitesse du vent : La vitesse moyenne du vent a montré une certaine variation, mais sans tendance nette d'augmentation ou de diminution.

### Métriques clés et leur évolution

- Température maximale moyenne en 2010 : 22,7 °C, en 2024 : 24,5 °C.
- Température minimale moyenne en 2010 : 4,8 °C, en 2024 : 6,4 °C.

- Précipitation Guadeloupe : 2010 : 4.8 mm, 2024 : 3.3 mm.
- Précipitation Régions Métropolitaines : 2010 : 2,1 mm, 2024 : 2,2 mm.

- Vitesse du vent Régions Métropolitaines : 2010 : 3,7 m/s, 2024 : 3,8 m/s.

2. Points Saillants

- Observation 1 : Températures Maximales : Les températures maximales ont montré une hausse significative de plus de 2 °C dans des régions comme Occitanie et Provence-Alpes-Côte d'Azur entre 2010 et 2024. Cette tendance pourrait être liée à l'intensification des phénomènes climatiques extrêmes et à des changements dans les conditions locales, notamment l'urbanisation et l'amplification de l'effet d'îlot de chaleur urbain.

- Observation 2 : Précipitations : En Guyane et La Réunion, des périodes de sécheresse sont suivies de précipitations, créant des conditions de gestion des ressources en eau particulièrement difficiles. D’autres régions, comme en France Métropolitaine, connaissent des précipitations plus constantes tout au long de l'année.

- Observation 3 : Vitesse du Vent : Aucune variation notable n'a été observée concernant la vitesse du vent. Les tendances sont globalement constantes, mais aucune tendance à la hausse ou à la baisse n'a été observée.

3. Recommandations

- Recommandation 1 : Gestion de l'Eau : Compte tenu de la baisse des précipitations, il est recommandé de mettre en place des politiques de gestion de l'eau plus strictes, comme en Martinique. Des investissements dans des infrastructures de stockage d'eau et des technologies d'irrigation efficaces seraient bénéfiques.

- Recommandation 2 : Stratégies d'Agriculture Adaptée au Climat : Avec la hausse des températures, il est crucial d'adopter des pratiques agricoles plus résistantes à la chaleur et à la sécheresse. L'agriculture durable devrait être encouragée, en particulier en Martinique.

- Recommandation 3 : Adaptation aux cyclones : Même si la vitesse moyenne du vent reste stable, les régions côtières, notamment La Réunion et Guadeloupe, doivent continuer à renforcer leurs infrastructures et à se préparer aux cyclones, qui peuvent entraîner des rafales de vent beaucoup plus fortes, parfois destructrices.

## Copyright

Je déclare sur l'honneur que le code fourni a été produit par nous-même (Léo Dessertenne et Adrien Baffioni), à l'exception des éléments suivants :

1. Module de nettoyage des données (src/utils/clean_data.py, lignes 15-20)
   - Source : [Documentation Pandas](https://pandas.pydata.org/docs/)
   - Utilisation des fonctions de base de pandas pour le nettoyage

2. Layout de base Dash (src/components/layout.py, lignes 10-25)
   - Source : [Documentation Dash](https://dash.plotly.com/)
   - Structure de base recommandée pour les applications Dash

Toute ligne non déclarée ci-dessus est réputée être produite par les auteurs du projet.