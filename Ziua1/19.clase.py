# Clasa / sablon / template
class Operatii:
    def adunare (self, a, b): #"self" este o referinta catre obiectul curent
        return a + b

# Obiect
obiect = Operatii()
obiect.adunare

print(obiect.adunare (10, 5))