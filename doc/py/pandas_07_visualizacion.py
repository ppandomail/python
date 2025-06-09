import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/ppando/Materias/python/proy/pandas_datos.csv')

df.plot()                                                   # Linea por defecto
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')   # Dispersión, se visualiza muy buena correlación entre ambas variables
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')   # Dispersión, se visualiza muy mala correlación entre ambas variables
plt.show()

df['Duration'].plot(kind = 'hist')                          # Histograma, hubo más de 100 entrenamientos que duraron entre 50 y 60 minutos      
plt.show()

