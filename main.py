import argparse
import logging
import os
import sys

from config.settings import (
    DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_JSON, DEFAULT_OUTPUT_EXCEL,
    INPUT_DIR, OUTPUT_DIR
)
from core.exceptions import DianScraperError
from drivers.selenium_driver import SeleniumDriverManager
from scraper.dian_extractor import DianExtractor
from utils.file_operations import FileHandler


# Configuración de logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('dian_scraper.log', encoding='utf-8')
        ]
    )


def parse_arguments():
    parser = argparse.ArgumentParser(description='Scraper de datos de empresas desde la DIAN')
    parser.add_argument('--input', type=str, default=DEFAULT_INPUT_FILE,
                        help=f'Ruta al archivo Excel de entrada (default: {DEFAULT_INPUT_FILE})')
    parser.add_argument('--output-json', type=str, default=DEFAULT_OUTPUT_JSON,
                        help=f'Ruta al archivo JSON de salida (default: {DEFAULT_OUTPUT_JSON})')
    parser.add_argument('--output-excel', type=str, default=DEFAULT_OUTPUT_EXCEL,
                        help=f'Ruta al archivo Excel de salida (default: {DEFAULT_OUTPUT_EXCEL})')
    parser.add_argument('--convert-only', action='store_true',
                        help='Solo convertir JSON existente a Excel sin hacer scraping')

    return parser.parse_args()


def ensure_directories():
    """Asegura que los directorios necesarios existan."""
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("🚀 Iniciando DIAN Scraper")

    driver = None
    ensure_directories()
    args = parse_arguments()

    logger.info(f"Argumentos: {args}")
    try:
        file_handler = FileHandler()

        if args.convert_only:
            logger.info(f"Modo conversión: Convirtiendo {args.output_json} a {args.output_excel}")
            file_handler.convert_json_to_excel(args.output_json, args.output_excel)
            logger.info("✅ Conversión completada exitosamente")
            return

        driver = SeleniumDriverManager.create_driver()

        extractor = DianExtractor(
            driver=driver,
            input_file_path=args.input,
            output_file_path=args.output_json
        )
        # Proceso de scraping para cada uno de los nits del archvio de excel
        logger.info(f"Modo scraping: Procesando empresas desde {args.input}")
        extractor.process_companies_from_file()

        # Convertir JSON a Excel al final
        logger.info(f"Convirtiendo resultados a Excel: {args.output_excel}")
        file_handler.convert_json_to_excel(args.output_json, args.output_excel)

        logger.info("✅ Proceso completado exitosamente")

    except DianScraperError as e:
        logger.error(f"Error en el scraper: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        sys.exit(1)
    finally:
        # Cerrar el driver si existe
        if driver is not None:
            try:
                driver.quit()
                logger.info("🔒 WebDriver cerrado correctamente")
            except Exception as e:
                logger.error(f"Error al cerrar el WebDriver: {e}")


if __name__ == "__main__":
    main()
