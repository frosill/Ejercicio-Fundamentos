
# Solicitar a la API una quote cada 30 seg

import requests
import json
import time
import csv
import os
import errno
import string

URL = "https://thesimpsonsquoteapi.glitch.me/quotes"
contador_palabras = {} # Inicializa el diccionario que cuenta las palabras

while True :
    respuesta = requests.request("GET", URL)
    datos =respuesta.json()
    
# Coge la quote y el personaje del JSON recibido y la guarda en info_general
    frase = datos[0]['quote']
    personaje = datos[0]['character']
    info_general = [personaje, frase]

#Pasa las quote a lista de palabras y le quita los signos de puntuación
    words_wp = frase.split()  #Separa str en lista de palabras con signos de puntuación
    words = []                #Inicializa lista de palabras sin signos de puntuación

    for word_wp in words_wp:
      words.append(''.join([i for i in word_wp if i not in string.punctuation]))

    print(words)

#Va añadiendo las palabras que ha encontrado al diccionario por medio del bucle
    for word in words:

      contador_palabras[word] = 0 # Iniciala todos los valores de las palabras a 0

      if word not in contador_palabras:
        contador_palabras[word] = words.count(word) # Si no esta la añade y le asigna la cantidad de veces que se repite en la quote
      else:
        contador_palabras[word] += words.count(word) # Si ya existe le añade las veces oprtunas
      

# Crea fichero de texto donde va almacenando la cuenta de palabras
    with open ('CuentaPalabras.txt', 'w') as cuentapalabras:
      for clave, valor in contador_palabras.items():
        cuentapalabras.write(f"\n{clave}: {valor}")
       

#Descarga la imagen y la guarda en el directorio General del proyecto
    URL_imagen = datos[0]['image']
    imagen = requests.get(URL_imagen).content

    imagen_local = f"General/{personaje}.png"  #Especifica la ruta donde se descarga la imagen

    with open(imagen_local, 'wb') as handler:
      handler.write(imagen)

#Con un try va creando las carpetas de cada personaje, para que si trata de crear la carpeta de un personaje que ya existe, no salte error
    try:
      os.mkdir(f'Personajes/{personaje}')
      imagen_local = f'Personajes/{personaje}/{personaje}.png'

#Genera los CSVs en la carpeta que corresponde 
    #Genera CSV General
      my_dict1 = {'frase': frase, 'personaje': personaje}

      with open ('General/general.csv','a') as f:
        a= csv.DictWriter(f, my_dict1.keys())
        a.writerow(my_dict1)

    #Genera CSV Homer
      my_dict2 = {'frase': frase, 'personaje': personaje}

      if personaje == 'Homer Simpson':
        with open (f'Personajes/{personaje}/{personaje}.csv','a') as f:
          a= csv.DictWriter(f, my_dict2.keys())
          a.writerow(my_dict2)

    #Genera CSV Lisa
      my_dict3 = {'frase': frase, 'personaje': personaje}

      if personaje == 'Lisa Simpson':
        with open (f'Personajes/{personaje}/{personaje}.csv','a') as f:
          a= csv.DictWriter(f, my_dict3.keys())
          a.writerow(my_dict3)

      with open(imagen_local, 'wb') as handler:
        handler.write(imagen)

    except OSError as e:
      if e.errno != errno.EEXIST:
        raise

    time.sleep(0)

    

