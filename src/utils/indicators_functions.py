import pandas as pd
import numpy as np

from src.utils.get_data import get_cleaned_data

# Constants for regions and territories
NON_METROPOLITAN_TERRITORIES = [
    'guyane', 'martinique', 'guadeloupe', 'la réunion', 'mayotte',
    'saint-pierre-et-miquelon', 'saint-barthélemy', 'saint-martin',
    'wallis-et-futuna', 'polynésie française', 'nouvelle-calédonie',
    'terres australes et antarctiques françaises'
]

def check_required_columns(data, required_columns):
    """
    Checks if all required columns are present in the DataFrame.

    Parameters:
    - data (pd.DataFrame): The DataFrame to check.
    - required_columns (list): List of required columns.

    Returns:
    - None: Raises a ValueError if any required columns are missing.
    """
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {', '.join(missing_columns)}")

def filter_data_by_year(data, year):
    """
    Filters the data for a specific year.

    Parameters:
    - data (pd.DataFrame): The DataFrame to filter.
    - year (int): The year to filter by.

    Returns:
    - pd.DataFrame: The filtered DataFrame.
    """
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Année'] = data['Date'].dt.year
    filtered_data = data[data['Année'] == year]

    if filtered_data.empty:
        raise ValueError(f"No data found for the year {year}")

    return filtered_data


def filter_data_by_region(data, region):
    """
    Filters the data based on the specified region.

    Parameters:
    - data (pd.DataFrame): The DataFrame to filter.
    - region (str): The region to filter by (e.g., 'france métropolitaine').

    Returns:
    - pd.DataFrame: The filtered DataFrame for the specified region.
    """
    if region.lower() == 'france métropolitaine':
        # Exclude non-metropolitan territories
        working_data = data[~(
                data['region (name)'].str.lower().isin(NON_METROPOLITAN_TERRITORIES) |
                data['communes (name)'].str.lower().str.contains('|'.join(NON_METROPOLITAN_TERRITORIES))
        )]
        if working_data.empty:
            raise ValueError("No data found for France Métropolitaine")
    else:
        # Filter for the specified region
        working_data = data[data['region (name)'].str.lower() == region.lower()]
        if working_data.empty:
            raise ValueError(f"No data found for the region {region}")

    return working_data


def get_min_max_temperature(working_data):
    """
    Finds the minimum and maximum temperatures along with their respective regions.

    Parameters:
    - working_data (pd.DataFrame): The DataFrame containing the filtered data.

    Returns:
    - tuple: ((min temperature, region of min), (max temperature, region of max))
    """
    idx_min = working_data['Température (°C)'].idxmin()
    idx_max = working_data['Température (°C)'].idxmax()

    temp_min = working_data.loc[idx_min, 'Température (°C)']
    temp_max = working_data.loc[idx_max, 'Température (°C)']

    loc_min = f"{working_data.loc[idx_min, 'region (name)']}"
    loc_max = f"{working_data.loc[idx_max, 'region (name)']}"

    return (temp_min, loc_min), (temp_max, loc_max)


def temperature_min_max_year(data, year, region):
    """
    Calculates the minimum and maximum temperatures for a given region and year,
    and returns the regions where these temperatures were measured.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the weather data.
    - year (int): The year for which to calculate the temperatures.
    - region (str): The region for which to calculate the temperatures
                    (e.g., guyane, martinique, guadeloupe, france métropolitaine).

    Returns:
    - tuple: ((min temperature, region of min), (max temperature, region of max))
    """
    required_columns = ['Date', 'Température (°C)', 'region (name)', 'communes (name)']

    # Check if required columns are present
    check_required_columns(data, required_columns)

    # Filter data by year
    filtered_data = filter_data_by_year(data, year)

    # Filter data by region
    working_data = filter_data_by_region(filtered_data, region)

    # Get min and max temperatures
    return get_min_max_temperature(working_data)

def calculate_average_wind_speed(data):
    """
    Calculates the average wind speed from the given data.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing wind speed data.

    Returns:
    - float: The average wind speed.
    """
    return data['Vitesse du vent moyen 10 mn'].mean()
def calculate_average_wind_direction(data):
    """
    Calculates the average wind direction from the given data, considering the circular nature of directions.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing wind direction data.

    Returns:
    - float: The average wind direction in degrees.
    """
    # Convert wind directions to radians
    angles_rad = np.radians(data['Direction du vent moyen 10 mn'])

    # Calculate the x and y components
    x = np.mean(np.cos(angles_rad))
    y = np.mean(np.sin(angles_rad))

    # Calculate the average direction in degrees
    return np.degrees(np.arctan2(y, x)) % 360
def calculate_wind_averages(data, year, region):
    """
    Calculates the annual average wind speed and direction for a given region.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the weather data.
    - year (int): The year for which to calculate the averages.
    - region (str): The region for which to calculate the averages
                    (e.g., guyane, martinique, guadeloupe, france métropolitaine).

    Returns:
    - tuple: (average wind speed, average wind direction)
    """
    required_columns = ['Date', 'Direction du vent moyen 10 mn', 'Vitesse du vent moyen 10 mn', 'region (name)', 'communes (name)']

    # Check if required columns are present
    check_required_columns(data, required_columns)

    # Filter data by year
    filtered_data = filter_data_by_year(data, year)

    # Filter data by region
    working_data = filter_data_by_region(filtered_data, region)

    # Calculate the average wind speed
    avg_speed = calculate_average_wind_speed(working_data)

    # Calculate the average wind direction
    avg_direction = calculate_average_wind_direction(working_data)

    return avg_speed, avg_direction

def get_cardinal_direction(degrees):
    """
       Converts a given angle in degrees to the corresponding cardinal direction.

       Parameters:
       - degrees (float): The angle in degrees.

       Returns:
       - str: The corresponding cardinal direction (e.g., 'N', 'NE', 'E', etc.).
       """
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
