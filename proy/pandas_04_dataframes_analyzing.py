import pandas as pd

df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos.csv')

print(df.head())     # visualización de las primeras 5 filas (default)
print(df.head(10))   # visualización de las primeras 10 filas

print(df.tail())     # visualización de las últimas 5 filas (default)
print(df.tail(10))   # visualización de las últimas 10 filas

print(df.info())     # información sobre el conjunto de los datos
                     # 169 filas y 4 columnas
                     # nombre de cada columna con el tipo de dato
                     # valores vacios o nulos en calorias 

print(df.describe()) # muestra estadísticas de las columnas numéricas