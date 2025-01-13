import pandas as pd
from config import CONFIG
from src.utils.get_data import get_raw_data


def clean_data():
    """Nettoie les données brutes et les sauvegarde"""
    breakpoint()
    df = get_raw_data()
    # Ajouter ici la logique de nettoyage
    df.to_csv(df,
            sep=';',
            na_rep='',
            index=False)



