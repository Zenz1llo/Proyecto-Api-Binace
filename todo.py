import requests # type: ignore

response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&limit=1000&startTime=1609459200000&endTime=1611187140000')
data = response.json() 

import pandas as pd

# Tus datos (solo un fragmento para el ejemplo)
datos = [
    [1609459200000, '28923.63000000', '29017.50000000', '28913.12000000', '28975.65000000', '182.88987800', 1609459499999, '5300786.60064202', 5614, '80.02912900', '2319246.59950932', '0'],
    [1609459500000, '28975.65000000', '28979.53000000', '28846.28000000', '28858.94000000', '214.56810400', 1609459799999, '6201531.66152165', 4928, '113.76133100', '3287213.12042724', '0'],
    # Más datos aquí...
]

columnas = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'timestamp_ms', 'quote_asset_volume', 'num_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
df = pd.DataFrame(datos, columns=columnas)

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

def guardar_datos(tramo_tiempo, nombre_archivo):
    tramo_tiempo.to_csv(nombre_archivo, index=False)
    print(f"Datos guardados en {nombre_archivo}")

inicio = '2023-01-01 00:00:00'  # Cambia esta fecha y hora según lo que necesites
fin = '2023-01-01 00:30:00'     # Cambia esta fecha y hora según lo que necesites

tramo_tiempo = df[(df['timestamp'] >= inicio) & (df['timestamp'] <= fin)]
print(tramo_tiempo)  

guardar_datos(tramo_tiempo, 'datos_btc_tramo_1.csv')