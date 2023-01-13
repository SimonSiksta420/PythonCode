''' def test(fce_vstup:int=7) -> bool:
    """Funkce pro testování funkce"""
    if fce_vstup == * 5: '''
    
number = int(input("Zadej číslo: "))

def prime_number(number:int) -> bool:
    """Funkce pro zjištění, zda je číslo prvočíslem"""
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

input("Je číslo prvočíslem? " + str(prime_number(number)))