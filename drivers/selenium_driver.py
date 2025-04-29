
from seleniumbase import Driver
import time
import logging

from config.settings import (
    HEADLESS, INCOGNITO, DISABLE_GPU, NO_SANDBOX, REMOTE_DEBUG,
    WINDOW_SIZE, DIAN_URL, RECONNECT_TIME
)
from core.exceptions import WebDriverInitError

logger = logging.getLogger(__name__)


class SeleniumDriverManager:
    """Clase para gestionar el driver de Selenium."""

    @staticmethod
    def create_driver():
        """Crea y configura un driver de Selenium usando SeleniumBase."""
        try:
            logger.info("🛠️ Creando navegador SeleniumBase...")
            driver = Driver(
                uc=True,
                headless=HEADLESS,
                incognito=INCOGNITO,
                disable_gpu=DISABLE_GPU,
                no_sandbox=NO_SANDBOX,
                remote_debug=REMOTE_DEBUG,
                window_size=WINDOW_SIZE
            )

            logger.info("🌎 Intentando abrir página DIAN...")
            driver.uc_open_with_reconnect(DIAN_URL, reconnect_time=RECONNECT_TIME)
            return driver

        except Exception as e:
            logger.error(f"Error al inicializar el WebDriver: {e}")
            raise WebDriverInitError(f"No se pudo inicializar el WebDriver: {str(e)}")