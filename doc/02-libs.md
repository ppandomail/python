# Librerias

## No necesitan instalarse

* **sys**: funciones y parámetros específicos del SO

  ```py
  import sys

  print(sys.argv)        # argumentos de ejecución por línea de comandos
  for elem in sys.argv:
      print(elem)
  ```

* **os**: interfaz con el SO

  ```py
  import os

  print(os.environ)        # Lista de variables de entorno
  print(os.getenv('PATH')) # Valor de variable de entorno
  print(os.sep)            # Separador. Ejemplo: /
  print(os.getcwd())       # Directorio de trabajo

  os.remove('main.py')     # Elimina archivo
  ```

* **io**: funciones para manejo de flujo de datos y archivos
  
* **datetime**: funciones para fechas y tiempos
  
  ```py
  from datetime import datetime
  import pytz

  print(datetime.now())                              # Fecha de hoy
  print(datetime.now().strftime("%Y%m%d_%H%M%S"))    # Formatea fecha
  print(datetime.now(pytz.timezone("America/Buenos_Aires")))
  ```

* **time**: funciones de tiempo y conversiones

  ```py
  import time

  print("Hola")
  time.sleep(2)            # cantidad de segundos 
  print("Mundo")
  print(time.gmtime(0))    # epoch: punto donde comienza el tiempo 1/1/1970 00:00:00
  print(time.localtime())
  ```

* **calendar**: funciones de calendario

* **math**: funciones y constantes estadísticas. Representaciones, funciones trigonométricas, hiperbólicas

  ```py
  import math

  math.sqrt(64)   # 8
  math.ceil(1.4)  # 2
  math.floor(1.4) # 1
  math.pi         # 3.14...
  ```

* **unittest**: generación de tests unitarios

  ```py
  import unittest

  class MiTestCase(unittest.TestCase):
      
      @classmethod
      def setUpClass(cls):
          print('En setUpClass')

      def setUp(self):
          print('En setUp')
      
      def test_ok(self):
          self.assertEqual(2, 2)
          
      def test_fail(self):
          self.assertEqual(2, 3)
          
      def tearDown(self):
          print('En tearDown')

      @classmethod
      def tearDownClass(cls):
          print('En tearDownClass')

  unittest.main()
  ```

* **re**: expresiones regulares (secuencia de caracteres que forman un patrón de búsqueda, ejemplo email)
  * '^Sandra' -> que empiece con ...
  * 'Martin$' -> que termine con ...
  * '[ñ]' -> si se encuentra en cualquier lugar el caracter ñ
  * 'niñ[oa]'
  * '^[O-T]' -> empiece con un caracter en el rango de O a T
  * 'Ma[0-3]' -> en el rango de 0 a 3
  * 'Ma[^0-3]' -> no en el rango de 0 a 3
  * '.a' -> cualquier caracter

  ```py
  import re

  cadena = 'Vamos a aprender expresiones regulares'
  re.search('aprender', cadena)                     # devuelve un objeto si está o None caso contrario
  re.findall('aprender', cadena)                    # devuelve una lista. En este caso ['aprender']
  re.match('Sandra', 'Sandra Lopez')                # devuelve True. Busca al comienzo de 'Sandra Lopez' el patrón de búsqueda
  re.match('sandra', 'Sandra Lopez', re.IGNORECASE) # devuelve True
  ```

## Necesitan instalarse (repo: https://pypi.org/)

```sh
pip install <nom-lib>
```

* **requests**: facilita el trabajo con peticiones HTTP (acceso a internet)

  ```py
  import requests

  response = requests.get("https://jsonplaceholder.typicode.com/todos/", verify=False)
  print(response.text)
  print(response.status_code)
  print(response.encoding)
  print(response.headers)

  param = {'postId': 1}
  response = requests.get('https://jsonplaceholder.typicode.com/comments', params=param, verify=False)
  print(response.text)

  data = {'title': 'foo', 'body': 'bar', 'userId': 1}
  response = requests.post('https://jsonplaceholder.typicode.com/posts', params=data, verify=False)
  print(response.status_code)

  data = {'title': 'foo', 'body': 'bar', 'userId': 1}
  response = requests.put('https://jsonplaceholder.typicode.com/posts/1', params=data, verify=False)
  print(response.status_code)

  response = requests.delete('https://jsonplaceholder.typicode.com/posts/1', verify=False)
  print(response.status_code)
  ```

* **django**: crear aplicaciones web

* **flask**: crear aplicaciones web en forma rápida

  ```py
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')  # le dice a Flask qué URL debe ejecutar 
  def index():
      return '<h1>Hola mundo!<h1>'

  # Ejecución del server
  # > export FLASK_APP=hello.py
  # > flask run
  # Entrar al browser: localhost:5000/
  ```

* **Facker**: generador de datos falsos

  ```py
  # https://faker.readthedocs.io/en/master/
  from faker import Faker
  fake = Faker()

  print(fake.name())
  print(fake.address())
  print(fake.text())

  for _ in range(10):
    print(fake.name())
    
  fake = Faker('it_IT')
  for _ in range(10):
      print(fake.name()) 
  ```

* **pytest**: testing
* **pytest-bdd**: comportamiento
* **allure-pytest**: reporting
* **scipy**: funciones matemáticas y estadísticas para aplicaciones científicas
* **scikit-learn**: algoritmos de ML
* **tensorflow**: algoritmos de ML y aprendizaje profundo
* **keras**: entrenar redes neuronales
* **nltk**: funciones para PNL
* **pandas**: funciones para análisis de datos
* **numpy**: funciones matemáticas avanzadas
* **matplotlib**: análisis y representación básica de gráfica de datos
* **plotly**: graficación interactiva
