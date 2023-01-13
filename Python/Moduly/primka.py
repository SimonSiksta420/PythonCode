from math import sqrt, pi, acos

class Primka:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"Obecna rovnice primky je: {self.a}x + {self.b}y + {self.c} = 0"
        
    def odchylka(self, druha_primka):
        abd = abs(self.a * druha_primka.a + self.b * druha_primka.b)
        abc = sqrt(self.a**2 + self.b**2)*sqrt(druha_primka.a**2 + druha_primka.b**2)
        vysledek = abd/abc
        cosinus = acos(vysledek)
        return print(cosinus*180/pi)
        
        

primka_a = Primka(1, 0, 0)
primka_b = Primka(0, 1, 0)
print(primka_a)
primka_a.odchylka(primka_b)

input("Press Enter to exit...")