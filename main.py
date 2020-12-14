from time import sleep
import random
from word_extractor import clean_text
from pasapalabra_inserter import insert_into_api

def insert_words(text):
    cleaned_text_set = clean_text(text)
    for word in cleaned_text_set:
        print("inserting the word: {}".format(word))

        time_to_sleep = random.random()
        sleep(time_to_sleep)

        result, status_code, error_text = insert_into_api(word)
        if result:
            print("found, status_code: {}, error: {}".format(status_code, error_text))
        else:
            print("nor found")

if __name__ == '__main__':
    text = """
    Había una hoja de papel sobre una mesa, junto a otras hojas iguales a ella, cuando una pluma, bañada en negrísima tinta, la manchó completa y la llenó de palabras.

    – “¿No podrías haberme ahorrado esta humillación?”, dijo enojada la hoja de papel a la tinta. “Tu negro infernal me ha arruinado para siempre”.

    – “No te he ensuciado”, repuso la tinta. “Te he vestido de palabras. Desde ahora ya no eres una hoja de papel sino un mensaje. Custodias el pensamiento del hombre. Te has convertido en algo precioso”.

    En ese momento, alguien que estaba ordenando el despacho, vio aquellas hojas esparcidas y las juntó para arrojarlas al fuego. Sin embargo, reparó en la hoja “sucia” de tinta y la devolvió a su lugar porque llevaba, bien visible, el mensaje de la palabra. Luego, arrojó el resto al fuego.
    """
    insert_words(text)