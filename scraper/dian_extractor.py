from selenium.webdriver.common.by import By
import time
import logging
import pandas as pd

from config.settings import WAIT_TIME_BETWEEN_REQUESTS
from core.constants import ELEMENT_IDS, NIT_COLUMN, XPATH_EXPRESSIONS
from core.models import CompanyData
from core.exceptions import DataExtractionError
from scraper.captcha import CaptchaSolver
from scraper.page_interactions import PageInteractions
from utils.file_operations import FileHandler
from utils.data_processing import DataProcessor

logger = logging.getLogger(__name__)


class DianExtractor:
    """Clase principal para extraer datos de la DIAN."""

    def __init__(self, driver, input_file_path, output_file_path):
        self.driver = driver
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.page_interactions = PageInteractions(driver)
        self.captcha_solver = CaptchaSolver(driver)
        self.file_handler = FileHandler()

    def extract_company_data(self, nit):
        """Extrae los datos de una empresa basado en su NIT."""
        try:
            if self.page_interactions.check_company_not_registered():
                logger.info(f"❗ NIT {nit}: No está inscrito en el RUT")
                return CompanyData(nit=nit, estado="No está inscrito en el RUT")

            # Extraer todos los campos relevantes
            company_data = CompanyData(
                nit=nit,
                dv=self.page_interactions.get_element_text(By.ID, ELEMENT_IDS['dv']),
                razon_social=self.page_interactions.get_element_text(By.ID, ELEMENT_IDS['razon_social']),
                primer_apellido=self.page_interactions.get_element_text(By.ID, ELEMENT_IDS['primer_apellido']),
                segundo_apellido=self.page_interactions.get_element_text(By.ID, ELEMENT_IDS['segundo_apellido']),
                name=self.page_interactions.get_element_text(By.ID, ELEMENT_IDS['primer_nombre']),
                otro_nombre=self.page_interactions.get_element_text(By.ID, ELEMENT_IDS['otros_nombres']),
                fecha_actualizacion=self.page_interactions.get_element_text(By.XPATH, XPATH_EXPRESSIONS['fecha']),
                estado=self.page_interactions.get_element_text(By.ID, ELEMENT_IDS['estado']),
                observacion=self.page_interactions.get_element_text(By.XPATH, XPATH_EXPRESSIONS['observacion'])
            )

            logger.info(f"✅ NIT {nit}: Datos extraídos correctamente")
            return company_data

        except Exception as e:
            logger.error(f"Error al extraer datos para NIT {nit}: {e}")
            raise DataExtractionError(f"Error al extraer datos para NIT {nit}: {str(e)}")

    def process_single_company(self, nit):
        """Procesa una única empresa."""
        try:
            # Limpiar campo NIT por si había uno previo
            self.page_interactions.clear_input_field(ELEMENT_IDS['nit_input'])

            # Rellenar campo NIT
            self.page_interactions.fill_input_field(ELEMENT_IDS['nit_input'], str(nit))

            # Resolver captcha
            self.captcha_solver.solve_captcha()

            # Hacer clic en botón de búsqueda
            self.page_interactions.click_button(ELEMENT_IDS['search_button'])

            # Esperar a que cargue la página
            time.sleep(WAIT_TIME_BETWEEN_REQUESTS)

            # Extraer datos
            company_data = self.extract_company_data(nit)

            # Guardar datos
            self.file_handler.save_json_data(company_data.to_dict(), self.output_file_path)

            # Limpiar para la próxima búsqueda
            self.page_interactions.clear_input_field(ELEMENT_IDS['nit_input'])

            return company_data

        except Exception as e:
            logger.error(f"Error al procesar NIT {nit}: {e}")
            # Crear un objeto de datos mínimo para registrar el error
            error_data = CompanyData(nit=nit, estado=f"Error: {str(e)}")
            self.file_handler.save_json_data(error_data.to_dict(), self.output_file_path)
            return error_data

    def process_companies_from_file(self):
        """Procesa todas las empresas desde un archivo Excel."""
        try:
            # Leer archivo Excel
            df = DataProcessor.read_excel_file(self.input_file_path)
            total_companies = len(df)

            logger.info(f"Procesando {total_companies} empresas del archivo {self.input_file_path}")

            for index, row in df.iterrows():
                nit = row[NIT_COLUMN]
                logger.info(f"Procesando NIT {nit} ({index + 1}/{total_companies})")

                company_data = self.process_single_company(nit)

                # Pausa entre requests para evitar bloqueos
                time.sleep(WAIT_TIME_BETWEEN_REQUESTS)

            logger.info(f"✅ Proceso completado. Datos guardados en {self.output_file_path}")

        except Exception as e:
            logger.error(f"Error al procesar archivo de empresas: {e}")
            raise