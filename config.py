import os
CONFIG = {
    'DEBUG': True,
    'DATA_PATH': {
        'RAW': os.path.join('data', 'raw', 'donnees-synop-essentielles-omm.csv'),
        'CLEANED': os.path.join('data', 'cleaned', 'clean_data.csv')
    },
    'APP_HOST': '127.0.0.1',
    'APP_PORT': 8050
}