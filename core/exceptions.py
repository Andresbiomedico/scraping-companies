
class DianScraperError(Exception):
    """Excepción base para todos los errores del scraper."""
    pass


class WebDriverInitError(DianScraperError):
    """Error al inicializar el WebDriver."""
    pass


class CaptchaSolverError(DianScraperError):
    """Error al resolver el captcha."""
    pass


class DataExtractionError(DianScraperError):
    """Error al extraer datos del sitio web."""
    pass


class FileOperationError(DianScraperError):
    """Error al operar con archivos."""
    pass