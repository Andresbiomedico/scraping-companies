import pandas as pd
import logging

from core.exceptions import FileOperationError

logger = logging.getLogger(__name__)


class DataProcessor:
    """Clase para procesar datos."""

    @staticmethod
    def read_excel_file(filepath):
        """Lee un archivo Excel y lo convierte a DataFrame."""
        try:
            df = pd.read_excel(filepath)
            logger.info(f"Archivo Excel leído correctamente: {filepath}")
            return df
        except Exception as e:
            logger.error(f"Error al leer archivo Excel {filepath}: {e}")
            raise FileOperationError(f"Error al leer archivo Excel: {str(e)}")

