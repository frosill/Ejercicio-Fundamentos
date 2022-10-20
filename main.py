
# Solicitar a la API una quote cada 30 seg

import requests
import json
import time
import csv
import os
import errno
import string

URL = "https://thesimpsonsquoteapi.glitch.me/quotes"
contador_palabras = {} # Inicializamos el diccionario que cuenta las palabras

while True :
    respuesta = requests.request("GET", URL)
    datos =respuesta.json()
    
# Cogemos la quote y el personaje del JSON recibido y la guardamos en info_general
    frase = datos[0]['quote']
    personaje = datos[0]['character']
    info_general = [personaje, frase]

#Pasamos las quote a lista de palabras y le quitamos los signos de puntuación
    words_wp = frase.split()  #Separamos str en lista de palabras con puntuación
    words = []                #Inicialización lista de palabras sin signos de puntuación

    for word_wp in words_wp:
      words.append(''.join([i for i in word_wp if i not in string.punctuation]))

    print(words)

#Vamos añadiendo las palabras que hemos encontrado al diccionario por medio del bucle
    for word in words:
      value = 0

      if word not in contador_palabras:
        contador_palabras[word] = value

      value = words.count(word)
      contador_palabras[word] += value

# Creamos fichero de texto donde vamos almacenando la cuenta de palabras
    with open ('CuentaPalabras.txt', 'w') as cuentapalabras:
      for clave, valor in contador_palabras.items():
        cuentapalabras.write(f"\n{clave}: {valor}")
       

#Descargamos la imagen y la guardamos en el directorio General del proyecto
    URL_imagen = datos[0]['image']
    imagen = requests.get(URL_imagen).content

    imagen_local = f"General/{personaje}.png"  #Especificamos la ruta donde se descarga la imagen

    with open(imagen_local, 'wb') as handler:
      handler.write(imagen)

#Con un try vamos creando las carpetas de cada personaje, para que si trata de crear la carpeta de un personaje que ya existe, no salte error
    try:
      os.mkdir(f'{personaje}')
      imagen_local = f'{personaje}/{personaje}.png'

#Generamos los CSVs en la carpeta que corresponde 

      my_dict1 = {'frase': frase, 'personaje': personaje}

      with open ('General/general.csv','a') as f:
        a= csv.DictWriter(f, my_dict1.keys())
        a.writerow(my_dict1)

      my_dict2 = {'frase': frase, 'personaje': personaje}

      if personaje == 'Homer Simpson':
        with open (f'{personaje}/{personaje}.csv','a') as f:
          a= csv.DictWriter(f, my_dict2.keys())
          a.writerow(my_dict2)

      my_dict3 = {'frase': frase, 'personaje': personaje}

      if personaje == 'Lisa Simpson':
        with open (f'{personaje}/{personaje}.csv','a') as f:
          a= csv.DictWriter(f, my_dict3.keys())
          a.writerow(my_dict3)

      with open(imagen_local, 'wb') as handler:
        handler.write(imagen)

    except OSError as e:
      if e.errno != errno.EEXIST:
        raise

    time.sleep(0)

    

