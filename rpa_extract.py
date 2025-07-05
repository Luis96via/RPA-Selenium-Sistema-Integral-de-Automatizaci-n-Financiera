import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import requests
from captcha_solver import resolver_captcha_desde_imagen
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich import box

# Configuración
LOGIN_URL = 'https://web-transactions.netlify.app/'
USER_EMAIL = 'usuario@empresa.com'
USER_PASSWORD = 'Rpa2025!'
CSV_OUTPUT = 'data/transacciones.csv'

console = Console()

def iniciar_driver():
    options = Options()
    # No usar headless para simular usuario real
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()  # Abrir ventana maximizada
    return driver


def escribir_como_humano(element, texto):
    for letra in texto:
        element.send_keys(letra)
        time.sleep(random.uniform(0.05, 0.18))  # Pausa entre teclas


def resolver_captcha_con_api_propia(driver):
    driver.save_screenshot('data/full.png')
    # No mostrar print de screenshot ni OCR
    return resolver_captcha_desde_imagen('data/full.png')


def error_login_visible(driver):
    try:
        error_div = driver.find_element(By.ID, 'login-error')
        # Verifica si está visible y su estilo contiene 'display: block'
        visible = error_div.is_displayed()
        style = error_div.get_attribute('style')
        return visible and ('display: block' in style)
    except Exception:
        return False

def intentar_captcha_texto(driver, wait, login_button, max_retries=6):
    for intento in range(max_retries):
        time.sleep(2)
        driver.save_screenshot('data/full.png')
        captcha_text = resolver_captcha_desde_imagen('data/full.png')
        captcha_input = driver.find_element(By.ID, 'captcha-input')
        captcha_input.clear()
        escribir_como_humano(captcha_input, captcha_text)
        time.sleep(0.3)
        login_button.click()
        time.sleep(2)
        if error_login_visible(driver):
            if intento < max_retries - 1:
                continue
            else:
                raise Exception('No se pudo resolver el captcha de texto tras varios intentos.')
        break

def intentar_captcha_imagen(driver, wait, login_button, max_retries=6):
    for intento in range(max_retries):
        wait.until(lambda d: d.find_element(By.ID, 'captcha-image-grid').is_displayed())
        time.sleep(2)
        driver.save_screenshot('data/full.png')
        api_url = 'https://ai-captcha-resolver-luisvr.netlify.app/.netlify/functions/extract-text'
        with open('data/full.png', 'rb') as f:
            response = requests.post(api_url, files={'file': ('data/full.png', f, 'image/png')}, data={'type': 'image-grid'})
        result = response.json()
        if 'indices' in result:
            indices = result['indices']
        elif 'text' in result:
            indices = [int(x) for x in result['text'].replace(' ', '').split(',') if x.isdigit()]
        else:
            indices = []
        grid = driver.find_element(By.ID, 'captcha-image-grid')
        divs = grid.find_elements(By.XPATH, './div')
        for idx in indices:
            if 1 <= idx <= len(divs):
                divs[idx-1].click()
                time.sleep(0.2)
        time.sleep(0.3)
        login_button.click()
        time.sleep(2)
        if error_login_visible(driver):
            if intento < max_retries - 1:
                continue
            else:
                raise Exception('No se pudo resolver el captcha de imágenes tras varios intentos.')
        break

def intentar_captcha_logica(driver, wait, login_button, max_retries=6):
    for intento in range(max_retries):
        wait.until(lambda d: d.find_element(By.ID, 'captcha-logic-input').is_displayed() and d.find_element(By.ID, 'captcha-logic-input').is_enabled())
        time.sleep(2)
        driver.save_screenshot('data/full.png')
        logic_answer = resolver_captcha_respuesta_logica('data/full.png')
        logic_input = driver.find_element(By.ID, 'captcha-logic-input')
        logic_input.clear()
        escribir_como_humano(logic_input, logic_answer)
        time.sleep(0.3)
        login_button.click()
        time.sleep(2)
        if error_login_visible(driver):
            if intento < max_retries - 1:
                continue
            else:
                raise Exception('No se pudo resolver el captcha de lógica tras varios intentos.')
        break

def login(driver):
    wait = WebDriverWait(driver, 15)
    driver.get(LOGIN_URL)
    # 1. Ingresar email y password
    email_input = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-btn')
    ActionChains(driver).move_to_element(email_input).click().perform()
    escribir_como_humano(email_input, USER_EMAIL)
    ActionChains(driver).move_to_element(password_input).click().perform()
    escribir_como_humano(password_input, USER_PASSWORD)
    time.sleep(0.3)
    login_button.click()

    # 2. Captcha de texto (con reintentos)
    wait.until(lambda d: d.find_element(By.ID, 'captcha-input').is_displayed() and d.find_element(By.ID, 'captcha-input').is_enabled())
    intentar_captcha_texto(driver, wait, login_button)

    # 3. Captcha de imágenes (con reintentos)
    intentar_captcha_imagen(driver, wait, login_button)

    # 4. Captcha de lógica (con reintentos)
    intentar_captcha_logica(driver, wait, login_button)

    # 5. Esperar dashboard y continuar
    wait.until(EC.visibility_of_element_located((By.ID, 'transactions-table')))
    console.print(Panel("Login exitoso", style=Style(color="white", bgcolor="#2a5298"), box=box.ROUNDED))
    return True

# Helpers para los nuevos captchas

def resolver_captcha_indices_imagen(imagen_path):
    api_url = 'https://ai-captcha-resolver-luisvr.netlify.app/.netlify/functions/extract-text'  # Usa el mismo endpoint
    with open(imagen_path, 'rb') as f:
        response = requests.post(api_url, files={'file': (imagen_path, f, 'image/png')}, data={'type': 'image-grid'})
    try:
        result = response.json()
        # Espera una respuesta tipo {'indices': [1,4,6]} o '1,4,6'
        if 'indices' in result:
            return result['indices']
        if 'text' in result:
            return [int(x) for x in result['text'].replace(' ', '').split(',') if x.isdigit()]
        return []
    except Exception as e:
        console.print(Panel(f"Error resolviendo captcha de imágenes: {e}", style="bold red", box=box.ROUNDED))
        return []

def resolver_captcha_respuesta_logica(imagen_path):
    api_url = 'https://ai-captcha-resolver-luisvr.netlify.app/.netlify/functions/extract-text'  # Usa el mismo endpoint
    with open(imagen_path, 'rb') as f:
        response = requests.post(api_url, files={'file': (imagen_path, f, 'image/png')}, data={'type': 'logic'})
    try:
        result = response.json()
        if 'text' in result:
            return result['text'].strip()
        return ''
    except Exception as e:
        console.print(Panel(f"Error resolviendo captcha de lógica: {e}", style="bold red", box=box.ROUNDED))
        return ''

def extraer_tabla(driver):
    # Scroll a la tabla para simular navegación
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(random.uniform(0.3, 0.7))
    rows = driver.find_elements(By.CSS_SELECTOR, '#transactions-table tbody tr')
    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        if len(cols) == 5:
            fecha = cols[0].text.strip()
            descripcion = cols[1].text.strip()
            tipo = cols[2].text.strip()
            moneda = cols[3].text.strip()
            monto = cols[4].text.strip().replace(',', '')
            data.append({
                'Fecha': fecha,
                'Descripción': descripcion,
                'Tipo': tipo,
                'Moneda': moneda,
                'Monto': monto
            })
            # Simula tiempo de lectura humana
            time.sleep(random.uniform(0.1, 0.25))
    return data


def guardar_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    console.print(Panel(f"Datos guardados en {filename}", style=Style(color="white", bgcolor="#2a5298"), box=box.ROUNDED))


def main():
    driver = iniciar_driver()
    try:
        login(driver)
        data = extraer_tabla(driver)
        guardar_csv(data, CSV_OUTPUT)
        # Espera un poco antes de cerrar para simular usuario
        time.sleep(random.uniform(1.5, 2.5))
    finally:
        driver.quit()


if __name__ == '__main__':
    main() 