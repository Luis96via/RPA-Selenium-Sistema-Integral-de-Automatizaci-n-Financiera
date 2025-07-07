#!/usr/bin/env python3
"""
Gestor de emails destinatarios desde base de datos
"""

import pymysql
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

def get_db_connection():
    """Obtener conexión a la base de datos"""
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'finanzas_rpa')
    
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset='utf8mb4'
    )

def get_active_emails():
    """Obtener todos los emails activos"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute('''SELECT id, email, nombre, activo 
                         FROM emails_destinatarios 
                         WHERE activo = TRUE 
                         ORDER BY fecha_creacion''')
        
        emails = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return emails
    except Exception as e:
        print(f"Error obteniendo emails: {e}")
        return []

def get_email_list():
    """Obtener lista de emails como string separado por comas"""
    emails = get_active_emails()
    return ','.join([email['email'] for email in emails])

def add_email(email, nombre=None):
    """Agregar nuevo email"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''INSERT INTO emails_destinatarios (email, nombre) 
                         VALUES (%s, %s)''', (email, nombre))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return True
    except pymysql.IntegrityError:
        print(f"El email {email} ya existe")
        return False
    except Exception as e:
        print(f"Error agregando email: {e}")
        return False

def remove_email(email_id):
    """Eliminar email (marcar como inactivo)"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''UPDATE emails_destinatarios 
                         SET activo = FALSE 
                         WHERE id = %s''', (email_id,))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return True
    except Exception as e:
        print(f"Error eliminando email: {e}")
        return False

def update_email(email_id, email, nombre=None):
    """Actualizar email existente"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''UPDATE emails_destinatarios 
                         SET email = %s, nombre = %s 
                         WHERE id = %s''', (email, nombre, email_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return True
    except Exception as e:
        print(f"Error actualizando email: {e}")
        return False

def get_all_emails():
    """Obtener todos los emails (activos e inactivos)"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute('''SELECT id, email, nombre, activo, fecha_creacion 
                         FROM emails_destinatarios 
                         ORDER BY fecha_creacion''')
        
        emails = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return emails
    except Exception as e:
        print(f"Error obteniendo todos los emails: {e}")
        return [] 