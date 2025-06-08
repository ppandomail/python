"""
La limpieza de datos significa corregir datos erróneos:

                               Duration Date Pulse Maxpulse Calories
. Celdas vacias                (18 45 '18/12/2020' 90 112 NaN), también en la fila 22 y 28
. Datos con formato incorrecto (26 60 2020/12/26 100 120 250.0), date en otro formato
. Datos erróneos               (7 450 '2020/12/08' 104 134 253.3), 30 <= duración <= 60
. Duplicados                   (11 60 '12/12/2020' 100 120 250.7)
                               (12 60 '12/12/2020' 100 120 250.7)
"""

import pandas as pd

# --- CELDAS VACIAS ---

# Estrategia 1: Elimina celdas vacias (con valores NULL)
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
df = df.dropna()                  
print(df.to_string())

# Estrategia 2: Reemplaza celdas vacias con un valor
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
df = df.fillna(130)              
print(df.to_string())

# Estrategia 3: Reemplaza celdas vacias de una columna
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
df = df.fillna({"Calories": 130}) 
print(df.to_string())

# Estrategia 4: Reemplaza celdas vacias con el valor de la media
# media: valor promedio (la suma de todos los valores dividido por el número de valores)
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
media = df['Calories'].mean()
df = df.fillna({"Calories": media}) 
print(df.to_string())

# Estrategia 5: Reemplaza celdas vacias con el valor de la mediana
# mediana: el valor en el medio, después de haber ordenado todos los valores en orden ascendente
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
mediana = df['Calories'].median()
df = df.fillna({"Calories": mediana}) 
print(df.to_string())

# Estrategia 6: Reemplaza celdas vacias con el valor de la moda
# moda: el valor que aparece con mayor frecuencia
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
moda = df['Calories'].mode()[0]
df = df.fillna({"Calories": moda}) 
print(df.to_string())


# --- FORMATO INCORRECTO ---

# Convertir todas las celdas de las columnas al mismo formato (por ej. fecha)
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')                  
print(df.to_string())

# La fecha vacía de la fila 22 obtuvo un valor NaT (No es una hora); es decir, un valor vacío. 
# Una forma de solucionar los valores vacíos es simplemente eliminar toda la fila.
df = df.dropna(subset=['Date'])
print(df.to_string())


# --- DATOS ERRÓNEOS ---

# Estrategia 1: Reemplazar por otro valor, cuando son pocos los datos erróneos
# En el ejemplo seguro fue un error tipográfico y el valor debería ser "45" en lugar de "450"
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
df.loc[7, 'Duration'] = 45               
print(df.to_string())

# Estrategia 2: Reemplazar por otro valor mediante reglas, cuando son muchos los datos erróneos
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
for i in df.index:
    if df.loc[i, 'Duration'] > 120:
        df.loc[i, 'Duration'] = 120
 
# Estrategia 3: Eliminar filas que contienen datos erróneos
df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
for i in df.index:
  if df.loc[i, "Duration"] > 120:
    df = df.drop(i)

# --- DUPLICADOS ---

df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos2.csv')
print(df.duplicated())  # devuelve un bool para cada fila (True para cada fila que sea un duplicado)
df = df.drop_duplicates()
print(df.duplicated())




