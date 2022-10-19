
# Solicitar a la API una quote cada 30 segs

import requests
import json
import time
import csv
import os

URL = "https://thesimpsonsquoteapi.glitch.me/quotes"
contador_palabras = {} # Inicializamos el diccionario que cuenta las palabras

while True :
    respuesta = requests.request("GET", URL)
    datos =respuesta.json()
    
# Cogemos la quote y el personaje del JSON recibido y la guardamos en info_general
    frase = datos[0]['quote']
    personaje = datos[0]['character']

    words = frase.split() #Sparamos str en lista

#Vamos añadiendo las palabras que hemos encontrado al diccionario por medio del bucle
    for word in words:
      value = 0

      if word not in contador_palabras:
        contador_palabras[word] = value
        

      value = words.count(word)
      contador_palabras[word] += value

    info_general = [personaje, frase]

# Creamos fichero de texto donde vamos almacenando la cuenta de palabras
    with open ('CuentaPalabras.txt', 'w') as cuentapalabras:
      for clave, valor in contador_palabras.items():
        cuentapalabras.write(f"\n{clave}: {valor}")
      

#Descargamos la imagen y la guardamos en el directorio raiz del proyecto
    URL_imagen = datos[0]['image']
    imagen = requests.get(URL_imagen).content

    imagen_local = f"General/{personaje}.png"  #Especificamos la ruta donde se descarga la imagen

    with open(imagen_local, 'wb') as handler:
      handler.write(imagen)

# Evaluamos el personaje para ver en qué carpeta meterlo
    if personaje == 'Homer Simpson':

      info_hommer = [personaje, frase]
      imagen_local = f"Homer/{personaje}.png"

      with open(imagen_local, 'wb') as handler2:
        handler2.write(imagen)

    elif personaje == 'Lisa Simpson':

      info_lisa = [personaje, frase]
      imagen_local = f"Lisa/{personaje}.png"

      with open(imagen_local, 'wb') as handler3:
        handler3.write(imagen)

#Generamos los CSVs en la carpeta que corresponde 

    my_dict1 = {'frase': frase, 'personaje': personaje}

    with open ('General/general.csv','a') as f:
      a= csv.DictWriter(f, my_dict1.keys())
      a.writerow(my_dict1)

    my_dict2 = {'frase': frase, 'personaje': personaje}

    if personaje == 'Homer Simpson':
      with open ('Homer/homer.csv','a') as f:
        a= csv.DictWriter(f, my_dict2.keys())
        a.writerow(my_dict2)

    my_dict3 = {'frase': frase, 'personaje': personaje}

    if personaje == 'Lisa Simpson':
      with open ('Lisa/lisa.csv','a') as f:
        a= csv.DictWriter(f, my_dict3.keys())
        a.writerow(my_dict3)

    print(contador_palabras)

    time.sleep(0)

    

