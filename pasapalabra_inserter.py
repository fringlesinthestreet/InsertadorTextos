import requests
import json
from rae_api import create_arguments

URL = 'http://localhost:3000/api/v1/words'

def insert_into_api(word):
    result, arguments = create_arguments(word)
    if result:
      # print(arguments)
      r = requests.post(URL, json=arguments)
      status_code = r.status_code          
      if status_code == 422 or status_code == 500:
          error = r.json()['exception']
          return result, status_code, error
      return result, status_code, ''  

    return False, None, None

if __name__ == '__main__':
    print(insert_into_api('zorro'))
    print(insert_into_api('zarpar'))
    print(insert_into_api('zancudo'))
    print(insert_into_api('zángano'))
    print(insert_into_api('zócalo'))
    print(insert_into_api('zueco'))
    print(insert_into_api('zapato'))
    print(insert_into_api('zapatilla'))
    print(insert_into_api('zapallo'))
    print(insert_into_api('zanco'))
    print(insert_into_api('zarpado'))
    print(insert_into_api('zafarla'))
    print(insert_into_api('zarigüeya'))
    """
    print(insert_into_api('xilófono'))
    print(insert_into_api('kilogramo'))
    print(insert_into_api('kilómetro'))
    print(insert_into_api('kilowatt'))
    print(insert_into_api('kilo'))
    print(insert_into_api('xilofón'))
    print(insert_into_api('xenofobia'))
    print(insert_into_api('kétchup'))
    print(insert_into_api('ketchup'))
    print(insert_into_api('kremlin'))
    print(insert_into_api('kungfu'))
    print(insert_into_api('washingtoniano'))
    print(insert_into_api('watt'))
    print(insert_into_api('waterpolo'))
    print(insert_into_api('windsurf'))
    print(insert_into_api('walkie-talkie'))

    print(insert_into_api('usar'))
    print(insert_into_api('útil'))
    print(insert_into_api('universo'))
    print(insert_into_api('unisex'))
    print(insert_into_api('unipersonal'))
    print(insert_into_api('unido'))
    print(insert_into_api('unión'))
    print(insert_into_api('usado'))
    print(insert_into_api('usanza'))
    print(insert_into_api('utopía'))
    print(insert_into_api('usufructo'))
    """
    '''
    r = requests.post(URL, json={
        "word": {
            "name": "celular",
            "definitions_arguments": [{'definition': 'adjetivo . Perteneciente o relativo a las células', '_destroy': False}, {'definition': 'adjetivo . Derecho . Dicho de un establecimiento carcelario Donde los reclusos están sistemáticamente incomunicados en celdas independientes', '_destroy': False}, {'definition': 'nombre masculino . Usado más en América . Número que se asigna a cada teléfono', '_destroy': False}]
        }
    })
    print(r.status_code)
    print(r.json()['exception'])
    '''