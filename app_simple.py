from flask import Flask, render_template, jsonify, request
import subprocess
import threading
import queue
import time
import os
import sys
from datetime import datetime

app = Flask(__name__)

# Variables globales
output_queue = queue.Queue()
rpa_running = False
rpa_process = None

def run_rpa():
    """Ejecuta el RPA y envía la salida a la cola"""
    global rpa_running, rpa_process
    
    if rpa_running:
        return
    
    rpa_running = True
    output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] [START] Iniciando RPA...")
    
    try:
        # Configurar el entorno
        env = os.environ.copy()
        env['PYTHONUNBUFFERED'] = '1'
        
        # Ejecutar el RPA
        rpa_process = subprocess.Popen(
            [sys.executable, 'main_web_final.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1,
            env=env
        )
        
        # Leer la salida en tiempo real
        while True:
            line = rpa_process.stdout.readline()
            if not line and rpa_process.poll() is not None:
                break
            if line:
                cleaned_line = line.strip()
                if cleaned_line:
                    output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] {cleaned_line}")
        
        # Esperar a que termine
        return_code = rpa_process.wait()
        
        if return_code == 0:
            output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] [OK] RPA completado exitosamente!")
            output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] [SUCCESS] Proceso finalizado con éxito.")
        else:
            output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] [ERROR] RPA terminó con código de error: {return_code}")
            
    except Exception as e:
        output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] [ERROR] Error: {str(e)}")
    finally:
        rpa_running = False
        rpa_process = None
        output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] [END] Proceso RPA finalizado.")

@app.route('/')
def index():
    return render_template('index_simple.html')

@app.route('/start_rpa', methods=['POST'])
def start_rpa():
    """Inicia el RPA"""
    global rpa_running
    
    if rpa_running:
        return jsonify({'status': 'error', 'message': 'RPA ya está ejecutándose'})
    
    # Limpiar la cola
    while not output_queue.empty():
        output_queue.get()
    
    # Iniciar RPA en thread separado
    thread = threading.Thread(target=run_rpa)
    thread.daemon = True
    thread.start()
    
    return jsonify({'status': 'success', 'message': 'RPA iniciado'})

@app.route('/stop_rpa', methods=['POST'])
def stop_rpa():
    """Detiene el RPA"""
    global rpa_running, rpa_process
    
    if rpa_running and rpa_process:
        rpa_process.terminate()
        output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] [STOP] RPA detenido por el usuario")
        rpa_running = False
        return jsonify({'status': 'success', 'message': 'RPA detenido'})
    
    return jsonify({'status': 'error', 'message': 'RPA no está ejecutándose'})

@app.route('/get_output')
def get_output():
    """Obtiene la salida acumulada"""
    output_lines = []
    while not output_queue.empty():
        try:
            line = output_queue.get_nowait()
            output_lines.append(line)
        except queue.Empty:
            break
    
    return jsonify({
        'output': output_lines,
        'is_running': rpa_running
    })

@app.route('/clear_output', methods=['POST'])
def clear_output():
    """Limpia la salida"""
    while not output_queue.empty():
        output_queue.get()
    return jsonify({'status': 'success', 'message': 'Salida limpiada'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 