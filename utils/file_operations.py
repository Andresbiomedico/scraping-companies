import json
import os
import pandas as pd
import logging

from core.exceptions import FileOperationError

logger = logging.getLogger(__name__)


class FileHandler:
    """Clase para manejar operaciones con archivos."""

    def ensure_directory_exists(self, filepath):
        """Asegura que el directorio para el archivo exista."""
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            logger.debug(f"Directorio creado: {directory}")

    def save_json_data(self, data, filename):
        """Guarda datos en un archivo JSON."""
        try:
            # Asegurar que el directorio existe
            self.ensure_directory_exists(filename)

            # Crear el archivo con una lista vacía si no existe
            if not os.path.exists(filename):
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump([], f, ensure_ascii=False, indent=4)
                logger.debug(f"Archivo JSON creado: {filename}")

            # Abrir el archivo para lectura y escritura
            with open(filename, 'r+', encoding='utf-8') as f:
                try:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):
                        existing_data = [existing_data]
                except json.JSONDecodeError:
                    existing_data = []

                existing_data.append(data)
                f.seek(0)
                json.dump(existing_data, f, ensure_ascii=False, indent=4)
                f.truncate()

            logger.info(f"Datos guardados correctamente en {filename}")
            return True

        except Exception as e:
            logger.error(f"Error al guardar datos JSON: {e}")
            raise FileOperationError(f"Error al guardar datos JSON: {str(e)}")

    def read_json_file(self, filename):
        """Lee datos desde un archivo JSON."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            logger.error(f"Error al leer archivo JSON {filename}: {e}")
            raise FileOperationError(f"Error al leer archivo JSON: {str(e)}")

    def convert_json_to_excel(self, json_file, excel_file):
        """Convierte un archivo JSON a Excel."""
        try:
            # Leer datos JSON
            data = self.read_json_file(json_file)

            # Convertir a DataFrame
            df = pd.DataFrame(data)

            # Asegurar que el directorio existe
            self.ensure_directory_exists(excel_file)

            # Guardar como Excel
            df.to_excel(excel_file, index=False)

            logger.info(f"Archivo Excel creado correctamente: {excel_file}")
            return True

        except Exception as e:
            logger.error(f"Error al convertir JSON a Excel: {e}")
            raise FileOperationError(f"Error al convertir JSON a Excel: {str(e)}")