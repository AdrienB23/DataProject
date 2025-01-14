from src.utils.get_data import get_cleaned_data
import pandas as pd



def get_temperature_by_department(cleaned_data):
    """
     Cette fonction affiche les colonnes du DataFrame et retourne les températures moyennes par département.

    Parameters:
    - cleaned_data (pd.DataFrame): Le DataFrame nettoyé contenant les données.

    Returns:
    - pd.DataFrame: Un DataFrame contenant les départements et leurs températures moyennes.
    :param cleaned_data:
    :return:
    """
    # Vérification si les colonnes nécessaires existent
    required_columns = ['department (name)', 'Température (°C)', 'Latitude', 'Longitude']
    for col in required_columns:
        if col not in cleaned_data.columns:
            raise ValueError(f"La colonne '{col}' est manquante dans les données nettoyées.")

    # Calcul de la température moyenne par département
    temperature_by_department = (
        cleaned_data.groupby('department (name)')['Température (°C)']
        .mean()
        .reset_index()
        .rename(columns={'Température (°C)': 'Température Moyenne (°C)'})
    )

    # Sélectionner les coordonnées de chaque département
    coordinates_by_department = cleaned_data[['department (name)', 'Latitude', 'Longitude']].drop_duplicates()

    # Joindre les coordonnées avec la température
    result = pd.merge(temperature_by_department, coordinates_by_department, on='department (name)', how='left')

    # Afficher chaque ligne
    for index, row in result.iterrows():
        print(f"Department: {row['department (name)']}, "
              f"Température Moyenne: {row['Température Moyenne (°C)']}, "
              f"Latitude: {row['Latitude']}, "
              f"Longitude: {row['Longitude']}")
    return result

if __name__ == "__main__":

    get_temperature_by_department(get_cleaned_data())