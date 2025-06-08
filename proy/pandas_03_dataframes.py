"""
Dataframe: es un array bidimensional (la tabla completa)
"""

import pandas as pd

# Dataframe a partir de un diccionario con etiquetas por default mediante número de índice

datos = {
  "calorias": [420, 380, 390],
  "duracion": [50, 40, 45]
}

df = pd.DataFrame(datos)

print(df)

print(df.loc[0])      # devuelve fila 0

print(df.loc[[0, 1]]) # devuelve fila 0 y 1

# Dataframe a partir de un diccionario con etiquetas definidas

df = pd.DataFrame(datos, index = ["dia1", "dia2", "dia3"])

print(df) 

print(df.loc['dia2'])      # devuelve fila con etiqueta 'dia2'

# Dataframe a partir de un archivo csv (archivos separadas por comas)

df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos.csv')

print(df.to_string())      # muestra el df completo 

print(df)                  # invoca al método __str__ (mostrando por default las primeras 5 filas y las últimas 5 filas)

pd.options.display.max_rows = 9999  # aumento número de filas a mostrar

print(df)

# Dataframe a partir de un archivo json (texto simple con formato de un objeto, mismo formato que los diccionarios de Python)

df = pd.read_json('/Users/ppando/Materias/python/proy/pandas_datos.json')

print(df.to_string())      # muestra el df completo 