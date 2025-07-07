#!/usr/bin/env python3
"""
Aplicación Flask simple para RPA - Sistema Integral de Automatización Financiera
Con gestión dinámica de emails desde base de datos y logs limpios
"""

from flask import Flask, render_template, jsonify, request
import subprocess
import threading
import queue
import time
import os
import sys
from email_manager import get_all_emails, add_email, remove_email, update_email
from clean_logs import clean_log_message

app = Flask(__name__)

# Variables globales para el estado del RPA
rpa_process = None
rpa_running = False
output_queue = queue.Queue()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index_simple.html')

@app.route('/api/status')
def get_status():
    """Obtener estado actual del RPA"""
    return jsonify({
        'running': rpa_running,
        'timestamp': time.strftime('%H:%M:%S')
    })

@app.route('/api/start', methods=['POST'])
def start_rpa():
    """Iniciar el proceso RPA"""
    global rpa_process, rpa_running
    
    if rpa_running:
        return jsonify({'error': 'RPA ya está ejecutándose'}), 400
    
    try:
        # Limpiar cola de salida
        while not output_queue.empty():
            output_queue.get()
        
        # Configurar el entorno
        env = os.environ.copy()
        env['PYTHONUNBUFFERED'] = '1'
        
        # Ejecutar el RPA
        rpa_process = subprocess.Popen(
            [sys.executable, 'main_web_simple.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1,
            env=env
        )
        
        rpa_running = True
        
        # Thread para leer la salida
        def read_output():
            global rpa_running
            while rpa_running and rpa_process:
                line = rpa_process.stdout.readline()
                if line:
                    # Limpiar el mensaje antes de enviarlo
                    cleaned_message = clean_log_message(line.strip())
                    if cleaned_message:
                        output_queue.put({
                            'message': cleaned_message,
                            'timestamp': time.strftime('%H:%M:%S')
                        })
                else:
                    break
            rpa_running = False
        
        threading.Thread(target=read_output, daemon=True).start()
        
        return jsonify({
            'message': 'RPA iniciado correctamente',
            'status': 'running'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stop', methods=['POST'])
def stop_rpa():
    """Detener el proceso RPA"""
    global rpa_process, rpa_running
    
    if not rpa_running:
        return jsonify({'error': 'RPA no está ejecutándose'}), 400
    
    try:
        rpa_running = False
        if rpa_process:
            rpa_process.terminate()
            rpa_process.wait(timeout=5)
        
        return jsonify({
            'message': 'RPA detenido correctamente',
            'status': 'stopped'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/output')
def get_output():
    """Obtener salida del RPA (streaming)"""
    def generate():
        while rpa_running:
            try:
                # Obtener mensajes de la cola
                while not output_queue.empty():
                    message = output_queue.get_nowait()
                    yield f"data: {message}\n\n"
                
                time.sleep(0.1)
            except queue.Empty:
                time.sleep(0.1)
    
    return app.response_class(
        generate(),
        mimetype='text/plain'
    )

@app.route('/api/clear', methods=['POST'])
def clear_output():
    """Limpiar la salida del RPA"""
    global output_queue
    
    while not output_queue.empty():
        output_queue.get()
    
    return jsonify({'message': 'Salida limpiada'})

# Nuevas rutas para gestión de emails
@app.route('/api/emails', methods=['GET'])
def get_emails():
    """Obtener todos los emails configurados"""
    try:
        emails = get_all_emails()
        return jsonify({'emails': emails})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/emails', methods=['POST'])
def add_new_email():
    """Agregar nuevo email"""
    try:
        data = request.get_json()
        email = data.get('email')
        nombre = data.get('nombre', '')
        
        if not email:
            return jsonify({'error': 'Email es requerido'}), 400
        
        success = add_email(email, nombre)
        if success:
            return jsonify({'message': 'Email agregado correctamente'})
        else:
            return jsonify({'error': 'Error al agregar email'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/emails/<int:email_id>', methods=['DELETE'])
def delete_email(email_id):
    """Eliminar email"""
    try:
        success = remove_email(email_id)
        if success:
            return jsonify({'message': 'Email eliminado correctamente'})
        else:
            return jsonify({'error': 'Error al eliminar email'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/emails/<int:email_id>', methods=['PUT'])
def update_existing_email(email_id):
    """Actualizar email existente"""
    try:
        data = request.get_json()
        email = data.get('email')
        nombre = data.get('nombre', '')
        
        if not email:
            return jsonify({'error': 'Email es requerido'}), 400
        
        success = update_email(email_id, email, nombre)
        if success:
            return jsonify({'message': 'Email actualizado correctamente'})
        else:
            return jsonify({'error': 'Error al actualizar email'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False) 