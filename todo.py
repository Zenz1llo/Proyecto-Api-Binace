import requests # type: ignore

response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m&limit=1000&startTime=1609459200000&endTime=1611187140000.')
data = response.json() 
import pandas as pd # type: ignore

df = pd.DataFrame(data)










df.to_csv('datos_de_api.csv', index=False)
df.to_excel('datos_de_api.xlsx', index=False)