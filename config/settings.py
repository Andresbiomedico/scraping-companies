# Configuraciones del proyecto
import os

# URLs
DIAN_URL = ""

# Configuraciones del navegador
HEADLESS = False
INCOGNITO = True
DISABLE_GPU = True
NO_SANDBOX = True
REMOTE_DEBUG = True
WINDOW_SIZE = "1920,1080"

# Configuraciones de archivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "data", "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "output")

DEFAULT_INPUT_FILE = os.path.join(INPUT_DIR, "companies_dian.xlsx")
DEFAULT_OUTPUT_JSON = os.path.join(OUTPUT_DIR, "data.json")
DEFAULT_OUTPUT_EXCEL = os.path.join(OUTPUT_DIR, "data.xlsx")

# Configuraciones de tiempos
WAIT_TIME_BETWEEN_REQUESTS = 2
CAPTCHA_CHECK_INTERVAL = 2
RECONNECT_TIME = 6