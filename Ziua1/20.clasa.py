
# nume, prenume -> proprietati (ARE)
nume = "Tiriac"
prenume = "Ion"

# scrie, invata -> functii / metode (FACE)

# %%
class Student:
    # Magic method / functie magica
    def __init__(self, nume, prenume) -> None:
        self.nume = nume
        self.prenume = prenume

    def scrie (self):
        print("Studentul",self.nume,"scrie")
    
    def invata (self):
        print("Studentul invata")


# %%
student1 = Student("Tiriac", "Ion")
student2 = Student("Halep", "Simona")

# print(student1)
student1.scrie()

print(student1.nume)

student1.nume = "Andrei"
print(student1.nume)

student2.scrie()