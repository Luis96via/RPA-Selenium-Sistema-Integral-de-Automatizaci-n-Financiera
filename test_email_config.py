#!/usr/bin/env python3
"""
Script para probar la configuración de emails
"""

import os
from dotenv import load_dotenv
from email_manager import get_email_list, get_active_emails

def test_email_config():
    """Probar configuración de emails"""
    
    print("🔍 Verificando configuración de emails...")
    print("=" * 50)
    
    # 1. Verificar variables de entorno
    load_dotenv()
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    
    print(f"📧 EMAIL_USER: {'✅ Configurado' if email_user else '❌ NO CONFIGURADO'}")
    print(f"🔑 EMAIL_PASS: {'✅ Configurado' if email_pass else '❌ NO CONFIGURADO'}")
    
    if not email_user or not email_pass:
        print("\n⚠️  PROBLEMA: Faltan variables de entorno para email")
        print("📝 Crea o edita el archivo .env con:")
        print("EMAIL_USER=tu_correo@gmail.com")
        print("EMAIL_PASS=tu_password_aplicacion")
        return False
    
    # 2. Verificar emails en base de datos
    print("\n📊 Emails en base de datos:")
    try:
        emails = get_active_emails()
        if emails:
            for email in emails:
                print(f"  ✅ {email['email']} ({email['nombre']})")
        else:
            print("  ❌ No hay emails activos en la base de datos")
            return False
    except Exception as e:
        print(f"  ❌ Error accediendo a base de datos: {e}")
        return False
    
    # 3. Verificar lista de emails
    print(f"\n📋 Lista de emails para envío: {get_email_list()}")
    
    # 4. Verificar archivo de reporte
    if os.path.exists('reportes/resumen_financiero.xlsx'):
        print("✅ Archivo de reporte existe")
    else:
        print("❌ Archivo de reporte no existe")
    
    print("\n" + "=" * 50)
    print("🎯 Configuración lista para envío de emails")
    return True

if __name__ == "__main__":
    test_email_config() 