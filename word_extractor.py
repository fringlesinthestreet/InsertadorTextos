ACCEPTED_ORDS = [
  241, # ñ
  32,  # ' ' 
  225, # á 
  233, # é 
  237, # í 
  243, # ó 
  250, # ú
]

ARTICULOS = [
  'el',
  'la',
  'lo',
  'las',
  'los',
  'un',
  'una',
  'uno',
  'unas',
  'unos',
  'yo',
  'tu',
  'ellos',
  'nosotros',
  'aquellos',
  'vosotros',
  'vos',
  'el',
  'ellos',
  'vuestro',
]

PREPOSICIONES = [
  'a',
  'antes',
  'de',
  'dentro',
  'desde',
  'hace',
  'después',
  'despues',
  'durante',
  'en',
  'hasta',
  'por',
  'sobre',
  'tras',
  'al',
  'contra',
  'por',
  'con',
  'para',
  'según',
  'segun',
  'sin',
  'ni',
  'si',
  'no',
  'ni',
  'sí',
  'del',
  'al'
]


def eliminar_articulos(words_set):
    for articulo in ARTICULOS:
        if articulo in words_set:
            words_set.remove(articulo)
    return words_set

def eliminar_preposiciones(words_set):
    for preposicion in PREPOSICIONES:
        if preposicion in words_set:
            words_set.remove(preposicion)
    return words_set

def clean_text(text):
    lower_case = text.lower()
    filtered_text = "".join(filter(letter_in_range, lower_case))
    words = set(filtered_text.split(" "))
    words = eliminar_articulos(words)
    words = eliminar_preposiciones(words)
    return words

def letter_in_range(letter):
    ord_number = ord(letter)
    if ord_number in ACCEPTED_ORDS:
        return True
    return (ord_number >= 97 and ord_number <= 122)

if __name__ == '__main__':
    print(clean_text("asdas! sada, sada sad sadasSADAS Á ´É ññáÍ Ó Ú"))