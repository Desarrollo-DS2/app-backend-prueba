"""
Configuraciones para entorno de producción.

Este módulo contiene configuraciones específicas para el entorno de producción,
incluyendo la configuración de la base de datos.
"""

import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}