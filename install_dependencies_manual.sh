#!/bin/bash

echo "🚀 Instalando dependencias manualmente en PythonAnywhere..."

# Actualizar pip primero
echo "📦 Actualizando pip..."
python3 -m pip install --upgrade pip

# Instalar dependencias una por una
echo "🐍 Instalando dependencias Python..."

echo "Instalando selenium..."
python3 -m pip install selenium==4.15.2

echo "Instalando requests..."
python3 -m pip install requests==2.31.0

echo "Instalando pandas (versión compatible con Python 3.13)..."
python3 -m pip install pandas==2.2.0

echo "Instalando mysql-connector-python..."
python3 -m pip install mysql-connector-python==8.2.0

echo "Instalando openpyxl..."
python3 -m pip install openpyxl==3.1.2

echo "Instalando python-dotenv..."
python3 -m pip install python-dotenv==1.0.0

echo "Instalando flask..."
python3 -m pip install flask==3.0.0

echo "Instalando rich..."
python3 -m pip install rich==13.7.0

echo "Instalando beautifulsoup4..."
python3 -m pip install beautifulsoup4==4.12.2

echo "Instalando lxml..."
python3 -m pip install lxml==4.9.3

echo "✅ Instalación de dependencias completada!"

# Verificar instalación
echo "🔍 Verificando instalación..."
python3 -c "import selenium; print('✅ Selenium:', selenium.__version__)"
python3 -c "import requests; print('✅ Requests:', requests.__version__)"
python3 -c "import pandas; print('✅ Pandas:', pandas.__version__)"
python3 -c "import flask; print('✅ Flask:', flask.__version__)"

echo "📋 Próximos pasos:"
echo "1. Configurar base de datos MySQL"
echo "2. Crear archivo .env con credenciales"
echo "3. Configurar aplicación web en PythonAnywhere"
echo "4. Editar archivo WSGI"
echo ""
echo "📖 Ver deploy_instructions.md para más detalles" 