# Sintaxis básica Python

![Sintaxis Python](img/python.jpg)

## Comentarios

* Documentación dentro del código

  ```py
  # Esto es un comentario
  ```

## Sangria

* Indica bloque de código

  ```py
  if 5 > 2:
      print('5 es mayor que 2')
  ```

## Variables

* Almacenan valores y se crean cuando se les asigna un valor. Se infiere tipo de dato segun valor
* Nombre: (L|\_)(L|D|\_)* son case sensitive

  ```py
  i = 4      # int
  f = 3.14   # float
  b = True   # bool
  s1 = 'Hi'  # str
  s2 = "Hi"  # también str 
  n  = None  # No definido 

  print(type(b)) # obtiene el tipo
  ```

## Conversiones de tipos

  ```py
  w = str(3)    # w será '3'
  x = int(3)    # x será 3
  y = float(3)  # y será 3.0
  z = bool(0)   # z será False
  ```

## Cadenas

```py
b = "Hola mundo"
b[0]                   # "H"   
b[2:5]                 # "la "
b[:5]                  # "Hola "
b[2:]                  # "la mundo"

len(b)                 # 10
b.upper()              # "HOLA MUNDO"
b.lower()              # "hola mundo"
b.capitalize()         # "Hola mundo"
b.title()              # "Hola Mundo"
b = " Hola mundo "
b.strip()              # "Hola mundo"
b.replace("H", "h")    # "hola mundo"
b.split("a")           # ["hol", " mundo"]

"Hola" + " " + "mundo" # "Hola mundo"
"Hola" * 3             # HolaHolaHola

"mun" in b             # True  

f"Msg: {b}!"           # "Msg: Hola mundo"
```

## Operadores

* aritméticos = {+, -, *, /, //, %, **}
* asignación = {=, +=, -=, *=, /=, %=}
* relacionales = {==, !=, >, >=, <, <=}
* lógicos = {and, or, not}
* identidad = {is, is not}
* pertenencia = {in, not in}

## Estructuras de control

* **if**

  ```py
  i = 0
  if i == 0:
      print("Es 0")
  else:
      print("No es 0")
  ```

* **while**

  ```py
  while i < 3:
      print(i)
      i += 1
  ```

* **for**

  ```py
  palabra = 'python'
  for letra in palabra:
      print(letra)
  ```

## Colecciones

  ```py
  lista = [1, 3, 5, 2, 4]
  tupla = (1, 3, 5, 2, 4)     # inmutable
  rango = range(6)            
  mapa  = {'a' : 4, 'o' : 3}  # clave-valor
  conj  = {1, 3, 5, 2, 4}     # sin duplicados
  ```

## Listas

  ```py
  lista_vacia = []                 
  lista       = [1, 3, 2, 4]
  lista_multi = [1, [3, 2], 4]

  len(lista)             # 4
  
  lista.append(5)        # [1, 3, 2, 4, 5]
  lista.insert(1, 8)     # [1, 8, 3, 2, 4, 5]

  lista[2]               # 3
  lista[1:3]             # [8, 3]
  lista[1:]              # [8, 3, 2, 4, 5]
  lista[:2]              # [1, 8]

  lista.remove(8)        # [1, 3, 2, 4, 5]
  lista.sort()           # [1, 2, 3, 4, 5]
  lista.clear()          # []
  ```

## Números Aleatorios

  ```py
  import random
  print(random.randrange(1, 10))
  ```

## Entrada por terminal

  ```py
  edad = input('Cual es tu edad? ')  # devuelve str
  ```

## Salida por terminal

  ```py
  print('Tu edad es', edad)
  print('Tu edad es', edad, sep='->')
  print('Tu edad es', edad, end='!\n')
  ```

## Funciones

  ```py
  # pueden tener parámetros/argumentos
  # el pasaje es siempre por referencia
  def sumar(a, b=3):      # declaración con argumento por defecto
      return a + b        # cuerpo

  print(sumar(1, 2))      # argumentos posicionales
  print(sumar(b=2, a=1))  # argumentos nominales
  print(sumar(1))
  ```

## Excepciones

  ```py
  # Creo la excepción
  class SinNaftaException(Exception):
    pass

  class Auto:

    def arrancar(self):
      if self.nafta < 0.1:
        raise SinNaftaException()   # lanzo la excepción

  # función que maneja excepción
  def divide(n1, n2):
    try:
      return n1 / n2
    except ZeroDivisionError:
      print('No se puede dividir por cero')
      return 'operación errónea'
  ```

## Archivos

  ```py
  from io import open

  # Si el archivo no existe, el método open lo crea
  # 'w': escritura -> reemplaza
  # 'a': append    -> agrega
  fw = open('archivo.txt', 'a')    
  fw.write('Hola mundo \n cruel')
  fw.close()

  # 'r': lectura
  fr = open('archivo.txt', 'r')
  lista = fr.readlines()      # devuelve lista de lineas
  fr.seek(0)                  # se cambia posición del puntero al caracter en posición 0
  texto = fr.read()           # devuelve todo el contenido del archivo
  print(texto)
  print(lista)
  fr.seek(0)                  
  print(fr.read(11))          # lee hasta el caracter en posición 11
  fr.close()
  ```
