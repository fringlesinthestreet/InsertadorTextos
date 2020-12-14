import json
import os.path


PATH = './WORDS_LIST.json'

def load_words():
    if not os.path.isfile(PATH):
        return set()

    with open(PATH) as json_file:
        data = json.load(json_file)
    
    return set(data)

def save_words(words_list):
    with open(PATH, 'w') as outfile:
        json.dump(words_list, outfile)