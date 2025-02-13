import random

def functia_a():
    pass

def functia_b() -> int: # functia returneaza un int
    return random.randint(1, 20)

# Type hints
def functia_c(param1:int, param2:int) -> float: # functia are 2 parametri cu type hint int (ar vrea int, dar nu e neaparat) si returneaza un float
    return param1 / param2

print(functia_a())
print(functia_b())
print(functia_c(100,2))
print(functia_c(100.25,2))

