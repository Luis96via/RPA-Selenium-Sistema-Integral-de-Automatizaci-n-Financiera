# 🚀 Deploy RPA en PythonAnywhere

## 📋 Pasos para Deploy

### 1. Crear cuenta en PythonAnywhere
- Ve a: https://www.pythonanywhere.com/
- Click en "Create a Beginner account"
- Registro con email (NO necesita tarjeta de crédito)

### 2. Subir archivos al servidor

#### Opción A: Git (Recomendado)
```bash
# En PythonAnywhere Console
git clone https://github.com/tuusuario/rpa-selenium.git
cd rpa-selenium
```

#### Opción B: Upload manual
- Ve a "Files" en PythonAnywhere
- Sube todos los archivos del proyecto

### 3. Instalar dependencias
```bash
# En PythonAnywhere Console
cd rpa-selenium
pip3 install --user -r requirements.txt
```

### 4. Configurar base de datos MySQL
- Ve a "Databases" en PythonAnywhere
- Crea nueva base de datos: `finanzas_rpa`
- Usuario: tu username de PythonAnywhere
- Contraseña: la que configures

### 5. Configurar variables de entorno
Crear archivo `.env` en la raíz del proyecto:
```env
EMAIL_USER=tu_correo@gmail.com
EMAIL_PASS=tu_password_aplicacion
EMAIL_TO=luis96via@gmail.com,luisdev96via@gmail.com
```

### 6. Configurar aplicación web
- Ve a "Web" en PythonAnywhere
- Click en "Add a new web app"
- Selecciona "Flask"
- Python version: 3.9
- Source code: `/home/tuusuario/rpa-selenium`
- Working directory: `/home/tuusuario/rpa-selenium`
- WSGI configuration file: `/var/www/tuusuario_pythonanywhere_com_wsgi.py`

### 7. Editar WSGI file
Reemplazar contenido con:
```python
#!/usr/bin/env python3
import sys
import os

path = '/home/tuusuario/rpa-selenium'
if path not in sys.path:
    sys.path.append(path)

os.environ['PYTHONPATH'] = path

from app_simple import app as application
```

### 8. Configurar Chrome/Selenium
```bash
# Instalar Chrome
sudo apt-get update
sudo apt-get install -y chromium-browser

# Descargar ChromeDriver
wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE
wget https://chromedriver.storage.googleapis.com/$(cat LATEST_RELEASE)/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
```

### 9. Modificar código para Linux
En `rpa_extract.py`, cambiar:
```python
# De:
driver = webdriver.Chrome()

# A:
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
```

### 10. Reiniciar aplicación
- Ve a "Web" en PythonAnywhere
- Click en "Reload"

## 🌐 URL de tu aplicación
`https://tuusuario.pythonanywhere.com`

## ✅ Verificación
1. Abre la URL
2. Deberías ver la interfaz del RPA
3. Prueba ejecutar el RPA
4. Verifica que los correos se envíen

## 🔧 Troubleshooting

### Error de permisos
```bash
chmod +x chromedriver
```

### Error de dependencias
```bash
pip3 install --user --upgrade pip
pip3 install --user -r requirements.txt
```

### Error de base de datos
- Verificar credenciales en `process_data.py`
- Asegurar que la BD existe

### Error de Chrome
- Verificar que Chrome esté instalado
- Usar modo headless en Selenium

## 📞 Soporte
Si tienes problemas, revisa:
- Logs en "Web" > "Log files"
- Console de PythonAnywhere
- Configuración de variables de entorno 