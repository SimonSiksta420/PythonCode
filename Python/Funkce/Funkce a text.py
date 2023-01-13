number = int(input("Zadej číslo: "))
text = input("Zadej text: ")

def number_text(number:int, text:str) -> str:
    """Funkce pro vytvoření textu s číslem"""
    return text * str(number)

input("Text s číslem: " + number_text(number, text))