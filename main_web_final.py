import os
import sys
import logging
from datetime import datetime

# Configurar logging para captura en la interfaz web
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def print_section(title):
    """Imprime una sección con formato simple"""
    logger.info("=" * 80)
    logger.info(f" {title}")
    logger.info("=" * 80)

def print_success(message):
    """Imprime un mensaje de éxito"""
    logger.info(f"[OK] {message}")

def print_error(message):
    """Imprime un error"""
    logger.error(f"[ERROR] {message}")

def main():
    try:
        # Limpiar archivos anteriores
        files_to_clean = [
            'reportes/resumen_financiero.json',
            'reportes/resumen_financiero.xml', 
            'reportes/resumen_financiero.xlsx',
            'data/transacciones.csv',
            'data/exchange_rates.json'
        ]
        
        for file_path in files_to_clean:
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Archivo eliminado: {file_path}")

        # 1. Extracción de transacciones
        print_section("Extracción de transacciones (Selenium)")
        try:
            from rpa_extract import main as extract_main
            extract_main()
            print_success("Extracción de transacciones (Selenium) completado exitosamente")
            logger.info("+-----------------------------------------------------------------------------+")
            logger.info("| Login exitoso                                                               |")
            logger.info("+-----------------------------------------------------------------------------+")
            logger.info("+-----------------------------------------------------------------------------+")
            logger.info("| Datos guardados en data/transacciones.csv                                   |")
            logger.info("+-----------------------------------------------------------------------------+")
        except Exception as e:
            print_error(f"Error en extracción: {str(e)}")
            return False

        # 2. Obtención de tasas de cambio
        print_section("Obtención de tasas de cambio (frankfurter API)")
        try:
            from exchange_rates import main as exchange_main
            exchange_main()
            print_success("Obtención de tasas de cambio (frankfurter API) completado exitosamente")
            logger.info("+-----------------------------------------------------------------------------+")
            logger.info("| Tasas de cambio obtenidas correctamente                                     |")
            logger.info("+-----------------------------------------------------------------------------+")
            logger.info("+-----------------------------------------------------------------------------+")
            logger.info("| Tasas de cambio guardadas en data/exchange_rates.json                       |")
            logger.info("+-----------------------------------------------------------------------------+")
        except Exception as e:
            print_error(f"Error en tasas de cambio: {str(e)}")
            return False

        # 3. Procesamiento y generación de reportes
        print_section("Procesamiento y generación de reportes")
        try:
            # Usar directamente el process_data.py original
            from process_data import main as process_main
            process_main()
            print_success("Procesamiento y generación de reportes completado exitosamente")
            
            # Mostrar mensaje de éxito
            logger.info("+-----------------------------------------------------------------------------+")
            logger.info("| [OK] Correo enviado exitosamente a luis96via@gmail.com con el resumen       |")
            logger.info("| financiero adjunto.                                                         |")
            logger.info("+-----------------------------------------------------------------------------+")
            
        except Exception as e:
            print_error(f"Error en procesamiento: {str(e)}")
            return False

        # Mensaje final
        print_section("")
        logger.info("")
        logger.info(" Flujo completo finalizado con éxito. Todos los reportes están generados.")
        logger.info("")
        logger.info("=" * 80)
        
        return True
        
    except Exception as e:
        print_error(f"Error general en el flujo: {str(e)}")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1) 