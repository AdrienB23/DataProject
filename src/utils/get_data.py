import pandas as pd
from config import CONFIG

def get_raw_data():
    """Récupère les données brutes"""
    return pd.read_csv(CONFIG['DATA_PATH']['RAW'], sep=';', encoding='utf-8')

def get_cleaned_data():
    """Récupère les données nettoyées"""
    return pd.read_csv(CONFIG['DATA_PATH']['CLEANED'], sep=';', encoding='utf-8')