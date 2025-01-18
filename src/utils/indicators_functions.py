import pandas as pd
import numpy as np

from src.utils.get_data import get_cleaned_data


def temperature_min_max_year(data, year, region):
    """
    Calcule les températures minimales et maximales pour une région et une année spécifiques,
    et renvoie les régions où ces températures ont été mesurées.

    Parameters:
    - data (pd.DataFrame): Le DataFrame contenant les données météorologiques
    - year (int): L'année pour laquelle calculer les températures
    - region (str): La région pour laquelle calculer les températures
                    (guyane, martinique, guadeloupe, france métropolitaine)

    Returns:
    - tuple: ((température minimale, région du min), (température maximale, région du max))
    """
    # Vérification des colonnes nécessaires
    required_columns = ['Date', 'Température (°C)', 'region (name)', 'communes (name)']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Colonnes manquantes : {', '.join(missing_columns)}")

    # Créer une copie pour éviter de modifier le DataFrame original
    work_data = data.copy()

    # Extraire l'année directement de la chaîne de caractères de la date
    work_data['Date'] = pd.to_datetime(work_data['Date'], errors='coerce')

    # Extraire l'année de manière plus efficace
    work_data['Année'] = work_data['Date'].dt.year
    # Filtrer par année
    work_data = work_data[work_data['Année'] == year]

    # Supprimer les lignes où les informations essentielles sont manquantes
    work_data = work_data.dropna(subset=['Température (°C)', 'region (name)', 'communes (name)'])

    if work_data.empty:
        raise ValueError(f"Aucune donnée trouvée pour l'année {year}")

    # Liste complète des territoires non métropolitains
    territoires_non_metro = [
        'guyane',
        'martinique',
        'guadeloupe',
        'la réunion',
        'mayotte',
        'saint-pierre-et-miquelon',
        'saint-barthélemy',
        'saint-martin',
        'wallis-et-futuna',
        'polynésie française',
        'nouvelle-calédonie',
        'terres australes et antarctiques françaises'
    ]

    if region.lower() == 'france métropolitaine':
        # Exclure tous les territoires non métropolitains
        working_data = work_data[
            ~(work_data['region (name)'].str.lower().isin(territoires_non_metro) |
              work_data['communes (name)'].str.lower().str.contains('|'.join(territoires_non_metro)))
        ]
        if working_data.empty:
            raise ValueError("Aucune donnée trouvée pour la France métropolitaine")
    else:
        # Filtrer pour la région spécifique
        working_data = work_data[work_data['region (name)'].str.lower() == region.lower()]
        if working_data.empty:
            raise ValueError(f"Aucune donnée trouvée pour la région {region}")

    # Trouver les températures min et max avec leurs localisations
    idx_min = working_data['Température (°C)'].idxmin()
    idx_max = working_data['Température (°C)'].idxmax()

    temp_min = working_data.loc[idx_min, 'Température (°C)']
    temp_max = working_data.loc[idx_max, 'Température (°C)']

    # Récupérer les informations de localisation
    loc_min = f"{working_data.loc[idx_min, 'region (name)']}"
    loc_max = f"{working_data.loc[idx_max, 'region (name)']}"

    return (temp_min, loc_min), (temp_max, loc_max)

def calculate_wind_averages(data, year, region):
    """
    Calcule les moyennes annuelles de vitesse et direction du vent pour une région donnée.

    Parameters:
    - data (pd.DataFrame): Le DataFrame contenant les données météorologiques
    - year (int): L'année pour laquelle calculer les moyennes
    - region (str): La région pour laquelle calculer les moyennes
                    (guyane, martinique, guadeloupe, france métropolitaine)

    Returns:
    - tuple: (vitesse moyenne, direction moyenne)
    """
    # Vérification des colonnes nécessaires
    required_columns = ['Date', 'Direction du vent moyen 10 mn', 'Vitesse du vent moyen 10 mn', 'region (name)', 'communes (name)']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Colonnes manquantes : {', '.join(missing_columns)}")

    # Créer une copie pour éviter de modifier le DataFrame original
    work_data = data.copy()

    # Extraire l'année directement de la chaîne de caractères de la date
    work_data['Date'] = pd.to_datetime(work_data['Date'], errors='coerce')

    # Extraire l'année de manière plus efficace
    work_data['Année'] = work_data['Date'].dt.year

    # Filtrer par année
    work_data = work_data[work_data['Année'] == year]

    # Supprimer les lignes où les informations essentielles sont manquantes
    work_data = work_data.dropna(subset=['Direction du vent moyen 10 mn', 'Vitesse du vent moyen 10 mn', 'region (name)', 'communes (name)'])

    if work_data.empty:
        raise ValueError(f"Aucune donnée trouvée pour l'année {year}")

    # Liste complète des territoires non métropolitains
    territoires_non_metro = [
        'guyane',
        'martinique',
        'guadeloupe',
        'la réunion',
        'mayotte',
        'saint-pierre-et-miquelon',
        'saint-barthélemy',
        'saint-martin',
        'wallis-et-futuna',
        'polynésie française',
        'nouvelle-calédonie',
        'terres australes et antarctiques françaises'
    ]

    if region.lower() == 'france métropolitaine':
        # Exclure tous les territoires non métropolitains
        working_data = work_data[
            ~(work_data['region (name)'].str.lower().isin(territoires_non_metro) |
              work_data['communes (name)'].str.lower().str.contains('|'.join(territoires_non_metro)))
        ]
        if working_data.empty:
            raise ValueError("Aucune donnée trouvée pour la France métropolitaine")
    else:
        # Filtrer pour la région spécifique
        working_data = work_data[work_data['region (name)'].str.lower() == region.lower()]
        if working_data.empty:
            raise ValueError(f"Aucune donnée trouvée pour la région {region}")

    # Calculer la vitesse moyenne
    avg_speed = working_data['Vitesse du vent moyen 10 mn'].mean()

    # Pour la direction du vent, nous devons utiliser une moyenne circulaire
    # Convertir les angles en radians
    angles_rad = np.radians(working_data['Direction du vent moyen 10 mn'])

    # Calculer les composantes x et y
    x = np.mean(np.cos(angles_rad))
    y = np.mean(np.sin(angles_rad))

    # Calculer la direction moyenne en degrés
    avg_direction = np.degrees(np.arctan2(y, x)) % 360

    return avg_speed, avg_direction

def get_cardinal_direction(degrees):
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                  'S', 'SSO', 'SO', 'OSO', 'O', 'ONO', 'NO', 'NNO']
    index = round(degrees / (360 / len(directions))) % len(directions)
    return directions[index]


if __name__ == "__main__":
    data = get_cleaned_data()
    temp = temperature_min_max_year(data, 2024, "france métropolitaine")
    wind_speed, wind_direction = calculate_wind_averages(data, 2024, "france métropolitaine")
    print(f"Température minimale : {temp[0][0]}°C à {temp[0][1]}")
    print(f"Température maximale : {temp[1][0]}°C à {temp[1][1]}")
    print(f"Vitesse moyenne du vent : {wind_speed:.2f} m/s")
    print(f"Direction moyenne du vent : {wind_direction:.1f}°")
