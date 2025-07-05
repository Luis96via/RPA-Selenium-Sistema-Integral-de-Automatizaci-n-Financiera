import requests
from datetime import date
import json
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich import box

API_URL = 'https://api.frankfurter.app/latest'

# Puedes cambiar las monedas según tus necesidades
BASE_CURRENCY = 'USD'
TARGET_CURRENCIES = ['EUR', 'GBP', 'USD']
OUTPUT_FILE = 'data/exchange_rates.json'

console = Console()

def get_exchange_rates(base=BASE_CURRENCY, targets=TARGET_CURRENCIES):
    symbols = ','.join([c for c in targets if c != base])
    params = {'from': base}
    if symbols:
        params['to'] = symbols
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    # Siempre incluye la base con tasa 1.0
    rates = {base: 1.0}
    rates.update(data.get('rates', {}))
    return {
        'date': data.get('date', str(date.today())),
        'base': base,
        'rates': rates
    }


def guardar_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    console.print(Panel(f"Tasas de cambio guardadas en {filename}", style=Style(color="white", bgcolor="#2a5298"), box=box.ROUNDED))


def main():
    try:
        result = get_exchange_rates()
        console.print(Panel("Tasas de cambio obtenidas correctamente", style=Style(color="white", bgcolor="#2a5298"), box=box.ROUNDED))
        guardar_json(result, OUTPUT_FILE)
    except Exception as e:
        console.print(Panel(f"Error al obtener tasas de cambio: {e}", style="bold red", box=box.ROUNDED))


if __name__ == '__main__':
    main() 