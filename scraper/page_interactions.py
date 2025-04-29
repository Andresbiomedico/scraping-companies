from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging

from core.constants import ELEMENT_IDS, XPATH_EXPRESSIONS

logger = logging.getLogger(__name__)


class PageInteractions:
    """Clase para manejar las interacciones con la página web."""

    def __init__(self, driver):
        self.driver = driver

    def get_element_text(self, by, name):
        """Obtiene el texto de un elemento de la página."""
        try:
            element = self.driver.find_element(by, name)
            return element.text
        except NoSuchElementException:
            return None

    def fill_input_field(self, element_id, value):
        """Rellena un campo de entrada."""
        try:
            input_field = self.driver.find_element(By.ID, element_id)
            input_field.send_keys(value)
        except Exception as e:
            logger.error(f"Error al rellenar campo {element_id}: {e}")
            raise

    def clear_input_field(self, element_id):
        """Limpia un campo de entrada."""
        try:
            input_field = self.driver.find_element(By.ID, element_id)
            input_field.clear()
        except Exception as e:
            logger.error(f"Error al limpiar campo {element_id}: {e}")
            raise

    def click_button(self, element_id):
        """Hace clic en un botón."""
        try:
            self.driver.find_element(By.ID, element_id).click()
        except Exception as e:
            logger.error(f"Error al hacer clic en botón {element_id}: {e}")
            raise

    def check_company_not_registered(self):
        """Verifica si la empresa no está inscrita en el RUT."""
        try:
            self.driver.find_element(By.XPATH, XPATH_EXPRESSIONS['not_registered'])
            return True
        except NoSuchElementException:
            return False