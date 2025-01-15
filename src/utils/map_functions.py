from src.utils.get_data import get_cleaned_data
import pandas as pd

def get_temperature_by_region(cleaned_data):
    """
    Cette fonction affiche les colonnes du DataFrame et retourne les températures moyennes par région.

    Parameters:
    - cleaned_data (pd.DataFrame): Le DataFrame nettoyé contenant les données.

    Returns:
    - pd.DataFrame: Un DataFrame contenant les régions et leurs températures moyennes.
    """
    # Vérification si les colonnes nécessaires existent
    required_columns = ['region (name)', 'Température (°C)', 'region (code)']
    for col in required_columns:
        if col not in cleaned_data.columns:
            raise ValueError(f"La colonne '{col}' est manquante dans les données nettoyées.")

    # Calcul de la température moyenne par région
    temperature_by_region = (
        cleaned_data.groupby('region (name)')['Température (°C)']
        .mean()
        .reset_index()
        .rename(columns={'Température (°C)': 'Température Moyenne (°C)'})
    )

    # Sélectionner les coordonnées de chaque région
    coordinates_by_region = cleaned_data[['region (name)', 'region (code)']].drop_duplicates()

    # Joindre les coordonnées avec la température
    result = pd.merge(temperature_by_region, coordinates_by_region, on='region (name)', how='left')

    # Afficher chaque ligne
    for index, row in result.iterrows():
        print(f"Region: {row['region (name)']}, "
              f"Température Moyenne: {row['Température Moyenne (°C)']}, "
              f"Code: {row['region (code)']}")
    return result

if __name__ == "__main__":
    get_temperature_by_region(get_cleaned_data())
