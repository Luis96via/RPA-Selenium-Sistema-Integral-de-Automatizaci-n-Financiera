#!/bin/bash

echo "🐼 Instalando pandas en PythonAnywhere..."

# Intentar instalar pandas con wheels pre-compilados
echo "Intentando instalar pandas con wheels..."
python3 -m pip install --only-binary=all pandas==2.1.4

# Si falla, intentar con una versión más reciente
if [ $? -ne 0 ]; then
    echo "Falló pandas 2.1.4, intentando con versión más reciente..."
    python3 -m pip install --only-binary=all pandas
fi

# Verificar instalación
echo "Verificando instalación de pandas..."
python3 -c "import pandas; print('✅ Pandas instalado:', pandas.__version__)"

echo "✅ Instalación de pandas completada!" 