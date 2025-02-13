
## Version 1
file_reader = open("numere.txt", "r")

continut = file_reader.read()
print(continut)
print(type(continut))

file_reader.close # Trebuie inchis fisierul la final


## Version 2 - inchide automat fisierul cant termina cu el
with open("numere.txt", "r") as file_reader:
    continut = file_reader.read()
    print(continut)
