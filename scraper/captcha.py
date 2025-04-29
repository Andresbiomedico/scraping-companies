from selenium.webdriver.common.by import By
import time
import logging

from config.settings import CAPTCHA_CHECK_INTERVAL
from core.constants import ELEMENT_IDS
from core.exceptions import CaptchaSolverError

logger = logging.getLogger(__name__)


class CaptchaSolver:
    """Clase para manejar la resolución de captchas."""

    def __init__(self, driver):
        self.driver = driver

    def get_captcha_value(self):
        """Obtiene el valor actual del campo de captcha."""
        try:
            captcha_input = self.driver.find_element(By.NAME, ELEMENT_IDS['captcha'])
            # captcha_input = self.driver.find_element(By.NAME, "cf-turnstile-response")
            return captcha_input.get_attribute("value")
        except Exception as e:
            raise CaptchaSolverError(f"No se pudo obtener el valor del captcha: {str(e)}")

    def solve_captcha(self):
        """Resuelve el captcha usando clicks automáticos."""
        try:
            captcha_value = self.get_captcha_value()
            while captcha_value == "":
                self.driver.uc_gui_click_captcha()
                captcha_value = self.get_captcha_value()
                time.sleep(CAPTCHA_CHECK_INTERVAL)

        except Exception as e:
            logger.error(f"Error al resolver captcha: {e}")
            raise CaptchaSolverError(f"Error al resolver captcha: {str(e)}")