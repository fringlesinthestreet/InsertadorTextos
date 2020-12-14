from time import sleep
import random
from word_extractor import clean_text
from pasapalabra_inserter import insert_into_api
from word_saver import load_words, save_words

def insert_words(cleaned_text_set):
    for word in cleaned_text_set:
        print("inserting the word: {}".format(word))

        time_to_sleep = random.random()
        sleep(time_to_sleep)

        result, status_code, error_text = insert_into_api(word)
        if result:
            print("found, status_code: {}, error: {}".format(status_code, error_text))
        else:
            print("not found")

if __name__ == '__main__':
    text = """8. La aventura del agua
Un día que el agua se encontraba en el soberbio mar sintió el caprichoso deseo de subir al cielo. Entonces se dirigió al fuego y le dijo:

– “¿Podrías ayudarme a subir más alto?”.

El fuego aceptó y con su calor, la volvió más ligera que el aire, transformándola en un sutil vapor. El vapor subió más y más en el cielo, voló muy alto, hasta los estratos más ligeros y fríos del aire, donde ya el fuego no podía seguirlo. Entonces las partículas de vapor, ateridas de frío, se vieron obligadas a juntarse, se volvieron más pesadas que el aire y cayeron en forma de lluvia. Habían subido al cielo invadidas de soberbia y recibieron su merecido. La tierra sedienta absorbió la lluvia y, de esta forma, el agua estuvo durante mucho tiempo prisionera en el suelo, purgando su pecado con una larga penitencia.

9. La gratitud de la fiera
Androcles, un pobre esclavo de la antigua Roma, en un descuido de su amo, escapó al bosque. Buscando refugio seguro, encontró una cueva y al entrar, a la débil luz que llegaba del exterior, el joven descubrió un soberbio león. Se lamía la pata derecha y rugía de vez en cuando. Androcles, sin sentir temor, se dijo:

– “Este pobre animal debe estar herido. Parece como si el destino me hubiera guiado hasta aquí para que pueda ayudarle. Vamos, amigo, no temas, te ayudaré”.

Así, hablándole con suavidad, Androcles venció el recelo de la fiera y tanteó su herida hasta encontrar una flecha clavada profundamente. Se la extrajo y luego le lavó la herida con agua fresca.

Durante varios días, el león y el hombre compartieron la cueva hasta que Androcles, creyendo que ya no le buscarían se decidió a salir. Varios centuriones romanos armados con sus lanzas cayeron sobre él y le llevaron prisionero al circo. Pasados unos días, fue sacado de su pestilente mazmorra. El recinto estaba lleno a rebosar de gentes ansiosas de contemplar la lucha. Androcles se aprestó a luchar con el león que se dirigía hacia él. De pronto, con un espantoso rugido, la fiera se detuvo en seco y comenzó a restregar cariñosamente su cabezota contra el cuerpo del esclavo.

– “¡Sublime! ¡Es sublime! ¡César, perdona al esclavo, pues ha sometido a la fiera!”, gritaban los espectadores.

El emperador ordenó que el esclavo fuera puesto en libertad. Sin embargo, lo que todos ignoraron era que Androcles no poseía ningún poder especial y que lo que había ocurrido no era sino la demostración de la gratitud del animal.

10. Secreto a voces
Gretel, la hija del Alcalde, era muy curiosa. Quería saberlo todo, pero no sabía guardar un secreto.

– “¿Qué hablabas con el Gobernador?”, le preguntó a su padre, después de intentar escuchar una larga conversación entre los dos hombres.

– “Estábamos hablando sobre el gran reloj que mañana, a las doce, vamos a colocar en el Ayuntamiento. Pero es un secreto y no debes divulgarlo”.

Gretel prometió callar, pero a las doce del día siguiente estaba en la plaza con todas sus compañeras de la escuela para ver cómo colocaban el reloj en el ayuntamiento. Sin embargo, grande fue su sorpresa al ver que tal reloj no existía. El Alcalde quiso dar una lección a su hija y en verdad fue dura, pues las niñas del pueblo estuvieron mofándose de ella durante varios años. Eso sí, le sirvió para saber callar a tiempo."""

    # Cargamos las ya guardadas, para no repetir
    saved_words = load_words()

    # Parseamos las nuevas
    cleaned_text_set = clean_text(text)

    # Juntamos ambos conjuntos en uno nuevo que se guardará
    all_words = cleaned_text_set.union(saved_words)

    # Dejamos solo las palabras nuevas para ser insertadas en el sistema
    new_words = cleaned_text_set.difference(saved_words)

    # insertamos en el sistema
    insert_words(new_words)

    # guardamos el conjunto completo de palabras
    save_words(list(all_words))