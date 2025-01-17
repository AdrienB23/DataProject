import sys
import os
from config import CONFIG
from src.utils.get_data import get_raw_data

# Add the root directory to the search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def clean_data():
    """
        Cleans raw data by dropping unnecessary columns and saves the cleaned data.

        The function retrieves raw data, removes specific columns that are deemed irrelevant,
        and saves the resulting cleaned dataset to the location specified in the CONFIG file.
    """
    df = get_raw_data()
    # Drop unnecessary columns from the dataset
    df.drop([
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
    ], axis=1, inplace=True)

    # Ensure the directory exists before saving the file
    output_dir = os.path.dirname(CONFIG['DATA_PATH']['CLEANED'])
    os.makedirs(output_dir, exist_ok=True)
    # Save the cleaned dataset to the specified output file
    output_file = CONFIG['DATA_PATH']['CLEANED']
    df.to_csv(output_file,
            sep=';',
            index=False,
            encoding='utf-8')

if __name__ == "__main__":
    clean_data()