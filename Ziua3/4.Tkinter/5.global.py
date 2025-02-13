#variabila globala
variabila = 10

print("variabila =", variabila)

def o_functie():
    #variabila locala
    variabila = 1000
    print("Variabila in functie =", variabila)

o_functie()
print("variabila =", variabila)

def alta_functie():
    global variabila
    variabila = 1000
    print("Variabila in alta functie =", variabila)

alta_functie()
print("variabila =", variabila)