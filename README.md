# ETL-CDE: Proceso ETL con Playwright Scraper

Este repositorio contiene un proceso ETL (Extract, Transform, Load) implementado con Playwright como herramienta de scraping para la extracción de datos de sitios web específicos.

## Instalación

### Requisitos previos
- Python 3.x instalado
- Gestor de paquetes Python `pip`

### Pasos de instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/CNoctis/ETL-CDE
    ```
   
2. Accede al directorio del repositorio:
    ```bash
    cd ETL-CDE
    ```

3. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

4. Instala las dependencias necesarias de playwright:
    ```bash
    playwright install
    ```

## Uso

Para ejecutar el proceso ETL, sigue estos pasos:

1. Asegúrate de estar en el directorio raíz del repositorio.

2. Ejecuta el archivo `__init__.py`:
    ```bash
    python __init__.py
    ```

Este comando iniciará el proceso ETL que incluye las siguientes etapas:
- **Scraper:** El scraper utilizando Playwright extraerá datos de los sitios web especificados.
- **Extract:** El proceso de extración se centra en utilizar los datos ofrecidos por el scraper
- **Transform:** Los datos obtenidos se procesarán y transformarán según las necesidades del proyecto
- **Load:** Los datos transformados se cargarán en el destino especificado, como una base de datos, archivo CSV, etc.


## Contribución

¡Estamos abiertos a contribuciones! Si deseas colaborar en este proyecto, siéntete libre de enviar pull requests con mejoras, correcciones de errores o nuevas funcionalidades.

Si encuentras problemas o tienes sugerencias para mejorar, por favor, crea un issue en el repositorio para que podamos abordarlo.
