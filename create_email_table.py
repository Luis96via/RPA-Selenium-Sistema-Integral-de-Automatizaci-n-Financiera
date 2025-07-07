#!/usr/bin/env python3
"""
Script para crear la tabla de emails destinatarios
"""

import pymysql
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

def create_email_table():
    """Crear tabla para emails destinatarios"""
    
    # Configuración de conexión desde variables de entorno
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'finanzas_rpa')
    
    print("📧 Creando tabla de emails destinatarios...")
    
    try:
        # Conectar a la base de datos
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset='utf8mb4'
        )
        cursor = conn.cursor()
        
        # Crear tabla emails_destinatarios
        cursor.execute('''CREATE TABLE IF NOT EXISTS emails_destinatarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(100) NOT NULL UNIQUE,
            nombre VARCHAR(100),
            activo BOOLEAN DEFAULT TRUE,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;''')
        
        # Insertar email por defecto si la tabla está vacía
        cursor.execute('SELECT COUNT(*) FROM emails_destinatarios')
        count = cursor.fetchone()[0]
        
        if count == 0:
            cursor.execute('''INSERT INTO emails_destinatarios (email, nombre) 
                             VALUES (%s, %s)''', 
                         ('luis96via@gmail.com', 'Usuario Principal'))
            print("✅ Email por defecto agregado")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✅ Tabla emails_destinatarios creada/verificada")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = create_email_table()
    if success:
        print("🎉 ¡Tabla de emails creada exitosamente!")
    else:
        print("❌ Error al crear la tabla") 