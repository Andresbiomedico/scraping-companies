# Scraping-Companies

Scraper de datos de empresas basado en Selenium.

---

## 📁 Estructura del Proyecto

- `config/settings.py`: Configuración variables de entorno.
- `core/exceptions.py`: Definición de excepciones personalizadas.
- `drivers/selenium_driver.py`: Creación y manejo del WebDriver de Selenium.
- `scraper/dian_extractor.py`: Lógica principal de extracción de datos.
- `utils/file_operations.py`: Utilidades para manejar archivos (lectura y conversión entre formatos).
- `main.py`: Punto de entrada principal al programa.

---

## 📚 Requisitos

- Python 3.11+
- Selenium
- Otros paquetes que se pueden definir en `requirements.txt`.

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## 🔧 Funcionamiento

### 1. Configuración Inicial

Antes de ejecutar el programa, debes realizar los siguientes pasos:

1. **Configurar la URL objetivo:**
   - En `config/settings.py`, asigna la URL de la página web de la DIAN o sitio de interés a la variable correspondiente.

2. **Agregar el archivo de entrada:**
   - Coloca el archivo de Excel con los NITs en la carpeta `data/input/`.
   - Configura el nombre del archivo de entrada en `config/settings.py` modificando `DEFAULT_INPUT_FILE` si es necesario.

### 2. Argumentos de Ejecución

Puedes controlar el comportamiento del scraper mediante argumentos de línea de comandos:

| Argumento        | Descripción                                                                      | Valor por defecto        |
|------------------|----------------------------------------------------------------------------------|--------------------------|
| `--input`        | Ruta al archivo Excel de entrada con los NITs de las empresas.                   | `input/empresas.xlsx`    |
| `--output-json`  | Ruta donde se guardará el archivo JSON con los resultados del scraping.          | `output/resultados.json` |
| `--output-excel` | Ruta donde se guardará la conversión de resultados a Excel.                      | `output/resultados.xlsx` |
| `--convert-only` | Si se establece, solo convierte un JSON existente a Excel sin realizar scraping. | -                        |

Ejemplo de uso:

```bash
python main.py --input data/empresas.xlsx --output-json output/datos.json --output-excel output/datos.xlsx
```

Para convertir un JSON existente a Excel sin hacer scraping:

```bash
python main.py --convert-only --output-json output/datos.json --output-excel output/datos.xlsx
```

### 3. Proceso de Scraping

1. Se carga el WebDriver de Selenium.
2. Se abre el archivo de entrada Excel y se extraen los NITs.
3. Para cada NIT, se navega a la página de la DIAN y se extrae la información correspondiente.
4. Los resultados se almacenan en un archivo JSON.
5. Al finalizar, el JSON se convierte automáticamente a un archivo Excel.

---

## 📈 Logging

Se generan logs tanto en consola como en el archivo `dian_scraper.log`, ubicando errores, advertencias, y eventos
informativos sobre el progreso de la ejecución.

---

## 🛡️ Manejo de Errores

- **ScraperError**: Errores controlados relacionados al proceso de scraping.
- **Exception**: Errores inesperados generales.

En ambos casos, el scraper intentará cerrar el WebDriver correctamente antes de finalizar la ejecución.

---


## 💎 Autor

Proyecto desarrollado por aaristiDev.

---

© 2025 - Todos los derechos reservados.