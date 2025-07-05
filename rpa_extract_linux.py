import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from captcha_solver import solve_captcha
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_chrome_driver():
    """Configura Chrome para Linux/PythonAnywhere"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Sin interfaz gráfica
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        logger.error(f"Error al configurar Chrome: {e}")
        # Fallback: intentar sin opciones específicas
        try:
            driver = webdriver.Chrome()
            return driver
        except Exception as e2:
            logger.error(f"Error crítico al iniciar Chrome: {e2}")
            raise

def main():
    """Función principal del RPA optimizada para Linux"""
    driver = None
    try:
        logger.info("Iniciando RPA en modo Linux...")
        
        # Configurar Chrome
        driver = setup_chrome_driver()
        driver.implicitly_wait(10)
        
        # Aquí va tu lógica de RPA específica
        # (Reemplaza con tu código actual de rpa_extract.py)
        
        logger.info("RPA completado exitosamente en Linux")
        
    except Exception as e:
        logger.error(f"Error en RPA: {e}")
        raise
    finally:
        if driver:
            driver.quit()
            logger.info("Driver de Chrome cerrado")

if __name__ == "__main__":
    main() 