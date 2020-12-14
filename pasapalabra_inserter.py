import requests
import json
from rae_api import create_arguments

URL = 'http://localhost:3000/api/v1/words'

def insert_into_api(word):
    result, arguments = create_arguments(word)
    if result:
      print(arguments)
      r = requests.post(URL, json=arguments)
      status_code = r.status_code          
      if status_code == 422 or status_code == 500:
          error = r.json()['exception']
          return result, status_code, error
      return result, status_code, ''  

    return False, None, None

if __name__ == '__main__':
    print(insert_into_api('kilométrico'))
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