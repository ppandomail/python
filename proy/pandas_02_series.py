"""
Serie: es un array unidimensional (como una columna de una tabla) que contiene datos de cualquier tipo
"""

import pandas as pd

a = [1, 7, 2]

# Serie a partir de una lista con etiquetas por default mediante número de índice

myvar = pd.Series(a)

print(myvar)         

print(myvar[0])      # 1

# Serie a partir de una lista con etiquetas definidas

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar['y']) # 7


# Serie a partir de un diccionario (las claves del diccionario se convierten en las etiquetas)

calorias = {'dia1': 420, 'dia2': 380, 'dia3': 390}

myvar = pd.Series(calorias)

print(myvar)

print(myvar['dia2'])

# Serie a partir de un diccionario especificando claves

myvar = pd.Series(calorias, index = ['dia1', 'dia2'])

print(myvar)