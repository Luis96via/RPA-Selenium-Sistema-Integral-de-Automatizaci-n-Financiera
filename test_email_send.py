#!/usr/bin/env python3
"""
Script para probar el envío de emails con detalle completo
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from email_manager import get_email_list

def test_email_send():
    """Probar envío de email con detalle completo"""
    
    print("🧪 Probando envío de email...")
    print("=" * 60)
    
    # Cargar variables de entorno
    load_dotenv()
    remitente = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')
    destinatario = get_email_list()
    
    print(f"📧 Remitente: {remitente}")
    print(f"📧 Destinatarios: {destinatario}")
    print(f"📧 Contraseña: {'✅ Configurada' if password else '❌ NO CONFIGURADA'}")
    
    if not remitente or not password:
        print("❌ Faltan credenciales de email")
        return False
    
    # Crear mensaje de prueba
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = "🧪 Prueba de Email - Sistema RPA"
    
    # Cuerpo del mensaje
    body = """
    <html>
    <body>
        <h2>🧪 Prueba de Email</h2>
        <p>Este es un email de prueba para verificar que el sistema de envío funciona correctamente.</p>
        <p><strong>Fecha:</strong> {}</p>
        <p><strong>Destinatarios:</strong> {}</p>
        <hr>
        <p><em>Sistema RPA - Luis Viña</em></p>
    </body>
    </html>
    """.format("2025-07-05", destinatario)
    
    msg.attach(MIMEText(body, 'html'))
    
    try:
        print("🔐 Conectando a Gmail...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        
        print("🔑 Autenticando...")
        server.login(remitente, password)
        
        print("📤 Enviando email...")
        text = msg.as_string()
        server.sendmail(remitente, destinatario.split(','), text)
        
        print("✅ Email enviado exitosamente!")
        server.quit()
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Error de autenticación: {e}")
        print("💡 Verifica que:")
        print("   - EMAIL_USER sea tu correo Gmail completo")
        print("   - EMAIL_PASS sea una contraseña de aplicación (no tu contraseña normal)")
        print("   - Tengas habilitada la verificación en 2 pasos en Gmail")
        return False
        
    except smtplib.SMTPRecipientsRefused as e:
        print(f"❌ Error con destinatarios: {e}")
        return False
        
    except smtplib.SMTPServerDisconnected as e:
        print(f"❌ Error de conexión: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

if __name__ == "__main__":
    success = test_email_send()
    if success:
        print("\n🎉 ¡Prueba de email exitosa!")
    else:
        print("\n❌ Prueba de email fallida") 