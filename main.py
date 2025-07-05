import subprocess
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich import box
from rich.style import Style

console = Console()

# Archivos a limpiar antes de ejecutar el flujo
to_delete = [
    'reportes/resumen_financiero.json',
    'reportes/resumen_financiero.xml',
    'reportes/resumen_financiero.xlsx',
    'data/transacciones.csv',
    'data/exchange_rates.json'
]
for f in to_delete:
    if os.path.exists(f):
        try:
            os.remove(f)
            console.print(f"Archivo eliminado: {f}")
        except Exception as e:
            console.print(f"No se pudo eliminar {f}: {e}")

scripts = [
    ("Extracción de transacciones (Selenium)", "rpa_extract.py"),
    ("Obtención de tasas de cambio (frankfurter API)", "exchange_rates.py"),
    ("Procesamiento y generación de reportes", "process_data.py")
]

for descripcion, script in scripts:
    console.print(Panel(f"{descripcion}", style=Style(color="white", bgcolor="#2a5298"), box=box.ROUNDED))
    try:
        result = subprocess.run([sys.executable, script], check=True, capture_output=True, text=True)
        if result.returncode == 0:
            console.print(f":white_check_mark: [bold green]{descripcion} completado exitosamente[/bold green]")
            console.print(result.stdout)
        else:
            console.print(f":x: [bold red]{descripcion} falló[/bold red]")
        # Si quieres mostrar detalles solo en error, descomenta:
        # if result.stderr:
        #     console.print(Panel(result.stderr, style="red"))
    except subprocess.CalledProcessError as e:
        console.print(f":x: [bold red]Error ejecutando {script}[/bold red]")
        console.print(Panel(e.stdout, style="red"))
        console.print(Panel(e.stderr, style="red"))
        sys.exit(1)

console.print(Panel("\nFlujo completo finalizado con éxito. Todos los reportes están generados.", style=Style(color="white", bgcolor="#2a5298"), box=box.ROUNDED)) 