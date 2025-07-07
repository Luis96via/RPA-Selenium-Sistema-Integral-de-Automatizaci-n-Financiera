#!/usr/bin/env python3
"""
Script para limpiar y organizar los logs del RPA
"""

import re
import json
from datetime import datetime

def clean_log_message(message):
    """Limpiar y organizar mensajes de log"""
    
    # Eliminar mensajes técnicos innecesarios
    if any(tech_msg in message for tech_msg in [
        'package:', 'plugin_name:', 'AUTHENTICATION_PLUGIN_CLASS:',
        'DevTools listening', 'WARNING:', 'ERROR:', 'Created TensorFlow',
        'Attempting to use a delegate', 'Registration response error'
    ]):
        return None
    
    # Limpiar mensajes de eliminación de archivos
    if 'Archivo eliminado:' in message:
        return None
    
    # Limpiar líneas de separación duplicadas
    if message.strip() in ['', '================================================================================', '+-----------------------------------------------------------------------------+']:
        return None
    
    # Simplificar mensajes de éxito
    if '[OK]' in message:
        # Extraer solo la parte importante
        if 'completado exitosamente' in message:
            return message.replace('[OK] ', '✓ ').replace(' completado exitosamente', ' completado')
        return message.replace('[OK] ', '✓ ')
    
    # Simplificar mensajes de login y datos
    if 'Login exitoso' in message:
        return '✓ Login exitoso'
    if 'Datos guardados' in message:
        return '✓ Datos guardados correctamente'
    if 'Tasas de cambio obtenidas' in message:
        return '✓ Tasas de cambio obtenidas'
    if 'Tasas de cambio guardadas' in message:
        return '✓ Tasas guardadas'
    
    # Simplificar mensajes de email
    if 'Intentando enviar email' in message:
        return 'Enviando email...'
    if 'Desde:' in message:
        return None  # No mostrar el remitente
    if 'Archivo Excel adjuntado' in message:
        return '✓ Archivo adjuntado'
    if 'Conectando a Gmail' in message:
        return 'Conectando...'
    if 'Autenticando' in message:
        return 'Autenticando...'
    if 'Enviando email' in message:
        return 'Enviando...'
    if 'Email enviado exitosamente' in message:
        return '✓ Email enviado exitosamente'
    
    # Simplificar mensajes de correo enviado
    if 'Correo enviado exitosamente' in message and 'con el resumen' in message:
        return '✓ Reporte enviado por email'
    
    # Simplificar resumen financiero
    if 'Resumen Financiero' in message:
        return 'RESUMEN FINANCIERO'
    if 'Campo' in message and 'Valor' in message:
        return '─' * 50
    if 'Fecha de generación' in message:
        fecha = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', message)
        if fecha:
            return f"Fecha: {fecha.group()}"
    if 'Balance total en USD' in message:
        balance = re.search(r'\d{1,3}(?:,\d{3})*\.\d{2}', message)
        if balance:
            return f"Balance Total: ${balance.group()} USD"
    if 'Total Ingresos en USD' in message:
        ingresos = re.search(r'\d{1,3}(?:,\d{3})*\.\d{2}', message)
        if ingresos:
            return f"Total Ingresos: ${ingresos.group()} USD"
    if 'Total Gastos en USD' in message:
        gastos = re.search(r'\d{1,3}(?:,\d{3})*\.\d{2}', message)
        if gastos:
            return f"Total Gastos: ${gastos.group()} USD"
    if 'Número de transacciones' in message:
        trans = re.search(r'\d+', message)
        if trans:
            return f"Transacciones: {trans.group()}"
    if 'Ingresos' in message and '|' in message and not 'Total' in message:
        ingresos = re.search(r'\d+', message)
        if ingresos:
            return f"Ingresos: {ingresos.group()}"
    if 'Gastos' in message and '|' in message and not 'Total' in message:
        gastos = re.search(r'\d+', message)
        if gastos:
            return f"Gastos: {gastos.group()}"
    
    # Simplificar mensajes finales
    if 'Flujo completo finalizado' in message:
        return '✓ Proceso completado exitosamente'
    if 'Todos los reportes están generados' in message:
        return '✓ Reportes generados y enviados'
    
    # Si no coincide con ningún patrón, devolver el mensaje original
    return message

def process_logs(log_data):
    """Procesar logs y devolver versión limpia"""
    cleaned_logs = []
    
    for log_entry in log_data:
        if isinstance(log_entry, dict) and 'message' in log_entry:
            message = log_entry['message']
            cleaned = clean_log_message(message)
            if cleaned:
                cleaned_logs.append({
                    'message': cleaned,
                    'timestamp': log_entry.get('timestamp', '')
                })
    
    return cleaned_logs

# Ejemplo de uso
if __name__ == "__main__":
    # Este script se puede usar para procesar logs existentes
    print("🧹 Script de limpieza de logs")
    print("Usar en conjunto con el sistema RPA para logs más limpios") 