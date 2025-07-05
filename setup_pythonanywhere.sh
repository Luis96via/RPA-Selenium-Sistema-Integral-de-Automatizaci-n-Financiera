#!/bin/bash

# Script de configuración automática para PythonAnywhere
# Ejecutar en la consola de PythonAnywhere

echo "🚀 Configurando RPA en PythonAnywhere..."

# 1. Actualizar sistema
echo "📦 Actualizando sistema..."
sudo apt-get update

# 2. Instalar Chrome
echo "🌐 Instalando Chrome..."
sudo apt-get install -y chromium-browser

# 3. Descargar ChromeDriver
echo "🔧 Descargando ChromeDriver..."
wget -q https://chromedriver.storage.googleapis.com/LATEST_RELEASE
CHROME_VERSION=$(cat LATEST_RELEASE)
wget -q https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
unzip -q chromedriver_linux64.zip
chmod +x chromedriver
rm chromedriver_linux64.zip LATEST_RELEASE

# 4. Instalar dependencias Python
echo "🐍 Instalando dependencias Python..."
pip3 install --user --upgrade pip
pip3 install --user -r requirements.txt

# 5. Crear directorios necesarios
echo "📁 Creando directorios..."
mkdir -p data
mkdir -p reportes

# 6. Configurar permisos
echo "🔐 Configurando permisos..."
chmod +x chromedriver
chmod 755 data/
chmod 755 reportes/

echo "✅ Configuración completada!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Configurar base de datos MySQL"
echo "2. Crear archivo .env con credenciales"
echo "3. Configurar aplicación web en PythonAnywhere"
echo "4. Editar archivo WSGI"
echo ""
echo "📖 Ver deploy_instructions.md para más detalles" 