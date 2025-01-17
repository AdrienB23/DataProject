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
    print("erruer")
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

if __name__ == "__main__":
    result = temperature_min_max_year(get_cleaned_data(), 2024, "france métropolitaine")
    print(f"Température minimale : {result[0][0]}°C à {result[0][1]}")
    print(f"Température maximale : {result[1][0]}°C à {result[1][1]}")