#!/usr/bin/env python3
"""
Script para ejecutar el sistema completo RPA
Incluye creación de tabla de emails y inicio de la aplicación Flask
"""

import os
import sys
import subprocess
from create_email_table import create_email_table

def main():
    print("🚀 Iniciando Sistema RPA - Gestión Dinámica de Emails")
    print("=" * 60)
    
    # 1. Crear tabla de emails si no existe
    print("📧 Verificando tabla de emails...")
    if create_email_table():
        print("✅ Tabla de emails configurada correctamente")
    else:
        print("❌ Error al crear tabla de emails")
        return False
    
    # 2. Verificar que existe el archivo de la app
    if not os.path.exists('app_simple.py'):
        print("❌ Error: No se encuentra app_simple.py")
        return False
    
    # 3. Verificar que existe el template
    if not os.path.exists('templates/index_simple.html'):
        print("❌ Error: No se encuentra templates/index_simple.html")
        return False
    
    # 4. Verificar que existe el gestor de emails
    if not os.path.exists('email_manager.py'):
        print("❌ Error: No se encuentra email_manager.py")
        return False
    
    print("✅ Todos los archivos necesarios están presentes")
    print("🌐 Iniciando aplicación Flask...")
    print("📱 La interfaz estará disponible en: http://localhost:8000")
    print("⚙️  Usa el ícono de configuración (⚙️) para gestionar emails")
    print("=" * 60)
    
    # 5. Ejecutar la aplicación Flask
    try:
        subprocess.run([sys.executable, 'app_simple.py'], check=True)
    except KeyboardInterrupt:
        print("\n👋 Sistema detenido por el usuario")
    except Exception as e:
        print(f"❌ Error ejecutando la aplicación: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 