from flask import Flask, render_template, jsonify, Response, request
import subprocess
import threading
import queue
import time
import os
import sys
from datetime import datetime

app = Flask(__name__)

# Cola para comunicación entre threads
output_queue = queue.Queue()

class RPAExecutor:
    def __init__(self):
        self.is_running = False
        self.process = None
    
    def run_rpa(self):
        """Ejecuta el RPA y envía la salida a la cola"""
        if self.is_running:
            return
        
        self.is_running = True
        output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando RPA...\n")
        
        try:
            # Configurar el entorno para capturar toda la salida
            env = os.environ.copy()
            env['PYTHONUNBUFFERED'] = '1'  # Forzar salida sin buffer
            env['FORCE_COLOR'] = '1'  # Forzar colores en rich
            
            # Ejecutar el RPA con configuración específica para capturar toda la salida
            self.process = subprocess.Popen(
                [sys.executable, 'main_web.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1,
                env=env,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            
            # Leer la salida en tiempo real
            while True:
                line = self.process.stdout.readline()
                if not line and self.process.poll() is not None:
                    break
                if line:
                    # Limpiar caracteres de control pero mantener el contenido
                    cleaned_line = line.strip()
                    if cleaned_line:
                        output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] {cleaned_line}")
                        # Forzar flush inmediato
                        output_queue.put("")  # Línea vacía para forzar actualización
            
            # Esperar a que termine el proceso
            return_code = self.process.wait()
            
            if return_code == 0:
                output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] ✓ RPA completado exitosamente!\n")
                output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] ✓ Proceso finalizado con éxito. Todos los reportes generados.\n")
            else:
                output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] ✗ RPA terminó con código de error: {return_code}\n")
                
        except Exception as e:
            output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] ✗ Error durante la ejecución: {str(e)}\n")
        finally:
            self.is_running = False
            self.process = None
            output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] Proceso RPA finalizado.\n")

# Instancia global del ejecutor
rpa_executor = RPAExecutor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_rpa', methods=['POST'])
def start_rpa():
    """Inicia el RPA en un thread separado"""
    if rpa_executor.is_running:
        return jsonify({'status': 'error', 'message': 'RPA ya está ejecutándose'})
    
    # Limpiar la cola
    while not output_queue.empty():
        output_queue.get()
    
    # Iniciar RPA en thread separado
    thread = threading.Thread(target=rpa_executor.run_rpa)
    thread.daemon = True
    thread.start()
    
    return jsonify({'status': 'success', 'message': 'RPA iniciado'})

@app.route('/stop_rpa', methods=['POST'])
def stop_rpa():
    """Detiene el RPA si está ejecutándose"""
    if rpa_executor.is_running and rpa_executor.process:
        rpa_executor.process.terminate()
        output_queue.put(f"[{datetime.now().strftime('%H:%M:%S')}] RPA detenido por el usuario\n")
        rpa_executor.is_running = False
        return jsonify({'status': 'success', 'message': 'RPA detenido'})
    
    return jsonify({'status': 'error', 'message': 'RPA no está ejecutándose'})

@app.route('/status')
def get_status():
    """Obtiene el estado actual del RPA"""
    return jsonify({
        'is_running': rpa_executor.is_running,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/stream')
def stream():
    """Stream de salida en tiempo real usando Server-Sent Events"""
    def generate():
        while True:
            try:
                # Obtener salida de la cola con timeout
                output = output_queue.get(timeout=1)
                yield f"data: {output}\n\n"
            except queue.Empty:
                # Enviar heartbeat para mantener la conexión
                yield f"data: \n\n"
    
    return Response(generate(), mimetype='text/event-stream')

@app.route('/clear_output', methods=['POST'])
def clear_output():
    """Limpia la salida de la terminal"""
    while not output_queue.empty():
        output_queue.get()
    return jsonify({'status': 'success', 'message': 'Salida limpiada'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 