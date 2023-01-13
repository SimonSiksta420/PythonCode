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
input ("Numbers before prime number: " + str([i for i in range(1, number) if prime_number(i)]))