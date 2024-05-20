import pandas as pd
import requests
import time

def es_simbolo_valido(symbol):
    url = 'https://api.binance.com/api/v3/exchangeInfo'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        symbols = [s['symbol'] for s in data['symbols']]
        return symbol in symbols
    else:
        print("Error al verificar el símbolo. Código de estado:", response.status_code)
        return False

def descargar_datos_y_guardar(symbol, interval, start_time, end_time, limit, nombre_archivo):
    url_base = 'https://api.binance.com/api/v3/klines'
    all_data = []

    current_start_time = start_time
    max_limit = 1000  # Límite máximo por solicitud

    while current_start_time < end_time:
        current_limit = min(limit, max_limit)
        url = f"{url_base}?symbol={symbol}&interval={interval}&startTime={current_start_time}&endTime={end_time}&limit={current_limit}"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if not data:
                break  # No hay más datos disponibles
            all_data.extend(data)
            current_start_time = data[-1][0] + 1  # Avanzar el tiempo de inicio al siguiente intervalo
            limit -= current_limit  # Disminuir el límite restante
            if limit <= 0:
                break  # Se ha alcanzado el límite de datos solicitado
            time.sleep(1)  # Esperar 1 segundo para evitar problemas con el límite de solicitudes
        else:
            print("Error al descargar los datos. Código de estado:", response.status_code)
            return
    
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'timestamp_ms', 'quote_asset_volume', 'num_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    df = pd.DataFrame(all_data, columns=columns)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume', 'num_trades']]  # Seleccionar solo las columnas de interés
    df_descripcion = pd.DataFrame({
        'timestamp': ['Inicio del período de tiempo'],
        'open': ['Precio de apertura'],
        'high': ['Precio máximo'],
        'low': ['Precio mínimo'],
        'close': ['Precio de cierre'],
        'volume': ['Volumen de operaciones'],
        'num_trades': ['Número de operaciones']
    })
    df = pd.concat([df_descripcion, df], ignore_index=True)
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos guardados en {nombre_archivo}")

def main():
    # Solicitar al usuario los parámetros necesarios
    symbol = input("Ingrese el símbolo de la criptomoneda (por ejemplo, BTCUSDT): ")
    if not es_simbolo_valido(symbol):
        print("Símbolo inválido. Por favor, ingrese un símbolo válido.")
        return
    
    interval = input("Ingrese el intervalo de tiempo (por ejemplo, 5m, 15m, 1h, 1d): ")
    inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD HH:MM:SS): ")
    fin = input("Ingrese la fecha de fin (YYYY-MM-DD HH:MM:SS): ")
    limit = int(input("Ingrese el número máximo de datos a descargar: "))

    # Convertir las fechas a timestamps en milisegundos
    inicio_ms = int(pd.Timestamp(inicio).timestamp() * 1000)
    fin_ms = int(pd.Timestamp(fin).timestamp() * 1000)

    # Descargar los datos y guardarlos en un archivo CSV
    nombre_archivo = f"datos_{symbol}_{interval}_{inicio.replace(' ', '_')}_a_{fin.replace(' ', '_')}.csv"
    descargar_datos_y_guardar(symbol, interval, inicio_ms, fin_ms, limit, nombre_archivo)

if __name__ == "__main__":
    main()
    
#1ª : 2017-08-17 04:00:00