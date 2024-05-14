import requests # type: ignore

response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&limit=1000&startTime=1609459200000&endTime=1611187140000.')
data = response.json()  # Esto convierte los datos en formato JSON en un diccionario de Python