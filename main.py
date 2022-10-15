
# Solicitar a la API una quote cada 30 segs

import requests
import json
import time
import csv

URL = "https://thesimpsonsquoteapi.glitch.me/quotes"

while True :
    respuesta = requests.request("GET", URL)
    datos =respuesta.json()
    #get the data and append them to List1
    
    frase = datos[0]['quote']
    personaje = datos[0]['character']


    info_general = [personaje, frase]

    if personaje == 'Hommer Simpson':

      info_hommer = [personaje, frase]
      
    elif personaje == 'Lisa Simpson':

      info_lisa = [personaje, frase] 

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

    time.sleep(5)

    

