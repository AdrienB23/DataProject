import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG = {
    'DEBUG': True,
    'DATA_PATH': {
        'RAW': os.path.join(BASE_DIR, 'data', 'raw', 'donnees-synop-essentielles-omm.csv'),
        'CLEANED': os.path.join(BASE_DIR, 'data', 'cleaned', 'clean_data.csv')
    },
    'APP_HOST': '127.0.0.1',
    'APP_PORT': 8050
}