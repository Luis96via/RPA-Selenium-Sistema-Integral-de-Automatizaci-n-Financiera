import requests
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich import box

console = Console()

def resolver_captcha_desde_imagen(imagen_path):
    """
    Envía una imagen PNG al endpoint OCR propio y devuelve el texto extraído.
    En el futuro, aquí se puede agregar lógica para distintos tipos de captcha.
    """
    api_url = 'https://ai-captcha-resolver-luisvr.netlify.app/.netlify/functions/extract-text'
    with open(imagen_path, 'rb') as f:
        response = requests.post(api_url, files={'file': (imagen_path, f, 'image/png')})
    try:
        result = response.json()
        captcha = result.get('text', '').strip()
        return captcha
    except Exception as e:
        console.print(Panel(f"No se pudo extraer texto del captcha: {e}", style="bold red", box=box.ROUNDED))
        return '' 