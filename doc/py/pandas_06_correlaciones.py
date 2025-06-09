"""
corr(): muestra la relación entre las columnas, ignorando las columnas "no numéricas"
Es una tabla con muchos números que representan qué tan buena es la relación entre dos columnas
El número varía de -1 a 1
   1 : correlación perfecta (cada vez que un valor aumenta, el otro también)
 0.9 : buena relación    (si aumenta un valor, el otro probablemente también aumentará)
-0.9 : buena relación    (si aumenta un valor, el otro probablement disminuirá)
 0.2 : NO buena relación (si aumenta un valor, no significa que el otro lo hará)

"""

import pandas as pd

df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos.csv')
print(df.corr())

# Análisis
# Duration y Duration: Perfecta, cada columna siempre tiene una relación perfecta consigo misma
# Duration y Calories: Muy Buena, podemos predecir que cuanto mas entrenes, mas calorias quemarás
# Duration y Pulse: Muy Mala, no podemos predecir el pulso máximo simplemente mirando la duración del entrenamiento
  