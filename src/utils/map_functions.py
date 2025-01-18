from src.utils.get_data import get_cleaned_data
import pandas as pd

from src.utils.indicators_functions import check_required_columns


def get_temperature_by_region(data, year=None):
    """
    Calculates the average temperatures by region for a given year.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the weather data.
    - year (int, optional): The year to calculate the averages for. If None, calculates for all years.

    Returns:
    - pd.DataFrame: DataFrame containing regions, years, and their average temperatures along with other statistics.
    """
    required_columns = ['Date', 'Température (°C)', 'region (name)', 'region (code)']
    check_required_columns(data, required_columns)

    work_data = data.copy()
    work_data['Date'] = pd.to_datetime(work_data['Date'], errors='coerce', utc=True) # Convert the 'Date' column to datetime format once
    work_data['Année'] = work_data['Date'].dt.year
    # Filter by the specified year if provided
    if year is not None:
        work_data = work_data[work_data['Année'] == year]
        if work_data.empty:
            raise ValueError(f"Aucune donnée trouvée pour l'année {year}")

    temperature_by_region = calculate_temperature_statistics(work_data)

    # Sort the results by year and region
    result = temperature_by_region.sort_values(['Année', 'Région'])

    return result


def calculate_temperature_statistics(work_data):
    """
       Calculates the temperature statistics (mean, min, max, std, count) for each region and year.

       Parameters:
       - data (pd.DataFrame): The DataFrame containing the data to calculate statistics for.

       Returns:
       - pd.DataFrame: The DataFrame with the calculated temperature statistics.
    """
    # Calculate the statistics (mean, min, max, std, count) by region and year
    temperature_by_region = (
        work_data.groupby(['region (name)', 'region (code)', 'Année'])
        .agg({
            'Température (°C)': ['mean', 'min', 'max', 'std', 'count']
        })
        .round(2)
        .reset_index()
    )
    # Flatten the multi-index columns
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
    return temperature_by_region


if __name__ == "__main__":
    # Année d'analyse
    YEAR = 2024
    print(f"\nAnalyse des températures pour l'année {YEAR}")
    print("=" * 80)

    # Récupération et analyse des données

    data = get_cleaned_data()
    result = get_temperature_by_region(data, YEAR)

    # Affichage des résultats
    print(f"\nNombre total de régions analysées : {len(result)}")
    print(f"Colonnes disponibles : {', '.join(result.columns)}")
    print("\nRésultats par région :")
    print("-" * 80)
    print(result.to_string(index=False))
    print("-" * 80)
