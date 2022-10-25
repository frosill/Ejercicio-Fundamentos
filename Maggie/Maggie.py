# Solicitar a la API una quote cada 30 seg

import requests
import json
import time
import csv

URL = "https://thesimpsonsquoteapi.glitch.me/quotes"

while True :
    respuesta = requests.request("GET", URL)
    datos =respuesta.json()
    
# Coge la quote y el personaje del JSON recibido y la guarda en info_general
    frase = datos[0]['quote']
    personaje = datos[0]['character']
    info_general = [personaje, frase]      

#Con un try va creando las carpetas de cada personaje, para que si trata de crear la carpeta de un personaje que ya existe, no salte error

#Genera los CSVs en la carpeta que corresponde y escribe en ellos
    #Genera CSV General
    my_dict1 = {'frase': frase, 'personaje': personaje}

    with open ('General/general.csv','a') as f:
        a= csv.DictWriter(f, my_dict1.keys())
        a.writerow(my_dict1)

    #Genera CSV Homer
    my_dict2 = {'frase': frase, 'personaje': personaje}

    if personaje == 'Homer Simpson':
        with open (f'Homer/{personaje}.csv','a') as f:
            a= csv.DictWriter(f, my_dict2.keys())
            a.writerow(my_dict2)

    #Genera CSV Lisa
    my_dict3 = {'frase': frase, 'personaje': personaje}

    if personaje == 'Lisa Simpson':
        with open (f'Lisa/{personaje}.csv','a') as f:
            a= csv.DictWriter(f, my_dict3.keys())
            a.writerow(my_dict3)

    time.sleep(30)