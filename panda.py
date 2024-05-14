import pandas as pd # type: ignore

# Crear un DataFrame a partir de los datos
df = pd.DataFrame(data) # type: ignore

# Realizar cualquier manipulación necesaria en los datos, como filtrado o limpieza
# Por ejemplo, si los datos tienen una estructura anidada, puedes utilizar funciones de Pandas para expandirlos

# Guardar los datos en un archivo CSV
df.to_csv('datos_de_api.csv', index=False)  # index=False evita que se guarde el índice del DataFrame en el archivo CSV