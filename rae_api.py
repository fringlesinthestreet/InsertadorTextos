import requests
from bs4 import BeautifulSoup
import json

URL = 'https://dle.rae.es/'
PARSEADOR = 'lxml'
CONTAINER_CLASS = 'article'
ROW_CLASS = 'p'
DEFINITION_CLASS = 'mark'
ABBREVIATION_CLASS = 'abbr'

def get_definition(word):
    r = requests.get(URL + word)
    soup = BeautifulSoup(r.text, PARSEADOR)
    if soup.find(CONTAINER_CLASS) is None:
        return False, None
    rows = soup.find(CONTAINER_CLASS).find_all(ROW_CLASS, recursive=False)
    if rows is None:
        return False, None
    definitions = []
    for row in rows:
        # print(row)
        words = row.find_all(DEFINITION_CLASS, recursive=False)
        abbreviations = row.find_all(ABBREVIATION_CLASS, recursive=False)
        if not words:
            continue
        
        # print(words)
        # print(abbreviations)
        abbr_definitions = " . ".join(map(lambda element: element.get('title').split(',')[0], abbreviations))

        definition = " ".join(map(lambda element: element.contents[0], words))
        definition_argument = {
            "definition": abbr_definitions + ' . ' + definition,
            "_destroy": False
        }
        definitions.append(definition_argument)
    return True, definitions

def create_arguments(word):
    status, definitions = get_definition(word)

    return status, {
        "word": {
            "name": word,
            "definitions_attributes": definitions
        }
    }

if __name__ == '__main__':
    print(create_arguments('celular'))
    
    # articulos = a.find_all('article')
    # print(articulos)
    # filas = a.find('article').find_all("p", recursive=False)
    # print(filas)
    