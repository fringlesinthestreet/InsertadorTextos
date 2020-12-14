ACCEPTED_ORDS = [
  241, # ñ
  32,  # ' ' 
  225, # á 
  233, # é 
  237, # í 
  243, # ó 
  250, # ú
]

def clean_text(text):
    lower_case = text.lower()
    filtered_text = "".join(filter(letter_in_range, accent_free_text))
    words = set(filtered_text.split(" "))
    return words

def letter_in_range(letter):
    ord_number = ord(letter)
    if ord_number in ACCEPTED_ORDS:
        return True
    return (ord_number >= 97 and ord_number <= 122)

if __name__ == '__main__':
    print(clean_text("asdas! sada, sada sad sadasSADAS Á ´É ññáÍ Ó Ú"))