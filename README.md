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

2. Créer un environnement virtuel
   ```bash
   python -m venv .venv
   ```

3. Activer l'environnement virtuel
   - Windows :
     ```bash
     .venv\Scripts\activate
     ```

4. Installer les dépendances
   ```bash
   pip install -r requirements.txt
   ```

### Lancement du Dashboard
1. Placer vos données brutes dans le dossier `data/raw/`
2. Nettoyer les données :
   ```bash
   python -m src.utils.clean_data
   ```
3. Lancer l'application :
   ```bash
   python main.py
   ```
4. Ouvrir votre navigateur à l'adresse : http://localhost:8050

## Data

### Source des données
Les données utilisées dans ce dashboard proviennent de [Source](https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/table/?sort=date&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJ0YyIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiNGRjUxNUEifV0sInhBeGlzIjoiZGF0ZSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImRvbm5lZXMtc3lub3AtZXNzZW50aWVsbGVzLW9tbSIsIm9wdGlvbnMiOnsic29ydCI6ImRhdGUifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D&location=2,-0.52734,-0.17578&basemap=jawg.light). Elles contiennent les informations suivantes :
- Variable 1 : Description et unité
- Variable 2 : Description et unité
- ...

### Structure des données
- Données brutes (`data/raw/rawdata.csv`) :
  - Format : CSV
  - Période : 2010 - 2025

- Données nettoyées (`data/cleaned/cleaneddata.csv`) :
  - Transformations appliquées
  - Variables dérivées créées
  - Traitement des valeurs manquantes

## Developer Guide

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

### Ajouter un Nouveau Graphique

1. Créer une fonction dans le fichier de page approprié :
   ```python
   def create_new_graph(data):
       fig = px.line(data, x='date', y='value')
       return dcc.Graph(
           id='new-graph',
           figure=fig
       )
   ```

2. Intégrer dans le layout :
   ```python
   layout = html.Div([
       create_header(),
       create_new_graph(data),
       create_footer()
   ])
   ```

## Rapport d'analyse

### Principales Conclusions

1. Tendance Générale
   - Description des tendances principales observées
   - Métriques clés et leur évolution

2. Points Saillants
   - Observation 1 avec données à l'appui
   - Observation 2 avec données à l'appui

3. Recommandations
   - Recommandation 1 basée sur l'analyse
   - Recommandation 2 basée sur l'analyse

### Visualisations Clés
Description des visualisations les plus pertinentes et leurs interprétations.

## Copyright

Je déclare sur l'honneur que le code fourni a été produit par nous-même (Léo Dessertenne et Adrien Baffioni), à l'exception des éléments suivants :

1. Module de nettoyage des données (src/utils/clean_data.py, lignes 15-20)
   - Source : [Documentation Pandas](https://pandas.pydata.org/docs/)
   - Utilisation des fonctions de base de pandas pour le nettoyage

2. Layout de base Dash (src/components/layout.py, lignes 10-25)
   - Source : [Documentation Dash](https://dash.plotly.com/)
   - Structure de base recommandée pour les applications Dash

Toute ligne non déclarée ci-dessus est réputée être produite par l'auteur du projet.