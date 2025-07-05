#!/usr/bin/env python3
"""
Script para inicializar la base de datos usando PyMySQL
para el RPA Sistema Integral de Automatización Financiera
"""

import pymysql
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

def create_database_and_tables():
    """Crear base de datos y tablas si no existen usando PyMySQL"""
    
    # Configuración de conexión desde variables de entorno
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'finanzas_rpa')
    
    print("🚀 Inicializando base de datos con PyMySQL...")
    print(f"📊 Base de datos: {DB_NAME}")
    print(f"👤 Usuario: {DB_USER}")
    print(f"🌐 Host: {DB_HOST}")
    
    try:
        # Conectar sin especificar base de datos para crearla
        conn = pymysql.connect(
            host=DB_HOST, 
            user=DB_USER, 
            password=DB_PASSWORD,
            charset='utf8mb4'
        )
        cursor = conn.cursor()
        
        # Crear base de datos si no existe
        print("📦 Creando base de datos...")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print("✅ Base de datos creada/verificada")
        
        cursor.close()
        conn.close()
        
        # Conectar a la base de datos específica
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset='utf8mb4'
        )
        cursor = conn.cursor()
        
        # Crear tabla tasas_cambio
        print("💰 Creando tabla tasas_cambio...")
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasas_cambio (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fecha DATE NOT NULL,
            moneda VARCHAR(10) NOT NULL,
            tasa DECIMAL(15,8) NOT NULL,
            UNIQUE KEY (fecha, moneda)
        );''')
        print("✅ Tabla tasas_cambio creada/verificada")
        
        # Crear tabla transacciones
        print("💳 Creando tabla transacciones...")
        cursor.execute('''CREATE TABLE IF NOT EXISTS transacciones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fecha DATE NOT NULL,
            descripcion VARCHAR(255),
            tipo VARCHAR(50),
            moneda VARCHAR(10),
            monto DECIMAL(15,2),
            tasa_usd DECIMAL(15,8),
            monto_usd DECIMAL(15,2),
            tasa_id INT,
            FOREIGN KEY (tasa_id) REFERENCES tasas_cambio(id)
        );''')
        print("✅ Tabla transacciones creada/verificada")
        
        # Crear tabla resumen_financiero
        print("📊 Creando tabla resumen_financiero...")
        cursor.execute('''CREATE TABLE IF NOT EXISTS resumen_financiero (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fecha_generacion DATETIME NOT NULL,
            balance_total_usd DECIMAL(15,2),
            total_ingresos_usd DECIMAL(15,2),
            total_gastos_usd DECIMAL(15,2),
            num_transacciones INT,
            num_ingresos INT,
            num_gastos INT
        );''')
        print("✅ Tabla resumen_financiero creada/verificada")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("\n🎉 ¡Base de datos inicializada correctamente!")
        print("📋 Tablas creadas:")
        print("   - tasas_cambio")
        print("   - transacciones") 
        print("   - resumen_financiero")
        
    except pymysql.Error as err:
        print(f"❌ Error de MySQL: {err}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = create_database_and_tables()
    if success:
        print("\n✅ ¡Inicialización completada exitosamente!")
        print("🚀 Ya puedes ejecutar tu aplicación RPA")
    else:
        print("\n❌ Error durante la inicialización")
        print("🔧 Verifica tu archivo .env y la configuración de MySQL") 