from src.utils.common import get_year_from_date
from src.utils.get_data import get_cleaned_data
import pandas as pd


def get_temperature_by_region(data, year=None):
    """
    Calcule les températures moyennes par région pour une année donnée.

    Parameters:
    - data (pd.DataFrame): Le DataFrame contenant les données météorologiques
    - year (int, optional): L'année pour laquelle calculer les moyennes. Si None, calcule pour toutes les années

    Returns:
    - pd.DataFrame: DataFrame contenant les régions, années et leurs températures moyennes
    """
    # Vérification des colonnes nécessaires
    required_columns = ['Date', 'Température (°C)', 'region (name)', 'region (code)']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Colonnes manquantes : {', '.join(missing_columns)}")

    # Créer une copie pour éviter de modifier le DataFrame original
    work_data = data.copy()

    # Convertir la colonne Date en datetime une seule fois
    work_data['Date'] = pd.to_datetime(work_data['Date'], errors='coerce')

    # Extraire l'année de manière plus efficace
    work_data['Année'] = work_data['Date'].dt.year

    # Filtrer par année si spécifiée
    if year is not None:
        work_data = work_data[work_data['Année'] == year]
        if work_data.empty:
            raise ValueError(f"Aucune donnée trouvée pour l'année {year}")

    # Calcul des statistiques par région et par année
    temperature_by_region = (
        work_data.groupby(['region (name)', 'region (code)', 'Année'])
        .agg({
            'Température (°C)': ['mean', 'min', 'max', 'std', 'count']
        })
        .round(2)
        .reset_index()
    )

    # Aplatir les colonnes multi-index
    temperature_by_region.columns = [
        'Région',
        'Code Région',
        'Année',
        'Température Moyenne (°C)',
        'Température Minimum (°C)',
        'Température Maximum (°C)',
        'Écart-type',
        'Nombre de mesures'
    ]

    # Trier les résultats
    result = temperature_by_region.sort_values(['Année', 'Région'])

    return result

if __name__ == "__main__":
    # Année d'analyse
    YEAR = 2024
    print(f"\nAnalyse des températures pour l'année {YEAR}")
    print("=" * 80)

    # Récupération et analyse des données
    try:
        data = get_cleaned_data()
        result = get_temperature_by_region(data, YEAR)

        # Affichage des résultats
        print(f"\nNombre total de régions analysées : {len(result)}")
        print(f"Colonnes disponibles : {', '.join(result.columns)}")
        print("\nRésultats par région :")
        print("-" * 80)
        print(result.to_string(index=False))
        print("-" * 80)

        # Statistiques globales
        print("\nStatistiques globales:")
        print(f"Température moyenne nationale : {result['Température Moyenne (°C)'].mean():.2f}°C")
        print(f"Région la plus chaude : {result.loc[result['Température Moyenne (°C)'].idxmax(), 'Région']} "
            f"({result['Température Maximum (°C)'].max():.2f}°C)")
        print(f"Région la plus froide : {result.loc[result['Température Moyenne (°C)'].idxmin(), 'Région']} "
            f"({result['Température Minimum (°C)'].min():.2f}°C)")

    except Exception as e:
        print(f"Erreur lors de l'analyse : {str(e)}")
