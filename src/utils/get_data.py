import pandas as pd
from config import CONFIG

def get_raw_data()-> pd.DataFrame:
    """
        Retrieves raw data from the specified CSV file in the configuration.

        Returns:
            pd.DataFrame: The raw data loaded into a Pandas DataFrame.
    """
    return pd.read_csv(CONFIG['DATA_PATH']['RAW'], sep=';', encoding='utf-8')


def get_cleaned_data() -> pd.DataFrame:
    """
        Retrieves cleaned data from the specified CSV file in the configuration.

        Returns:
            pd.DataFrame: The cleaned data loaded into a Pandas DataFrame.
    """
    return pd.read_csv(CONFIG['DATA_PATH']['CLEANED'], sep=';', encoding='utf-8')