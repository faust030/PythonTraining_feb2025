
colectie = [100, 200, 300]

def scade_5(x):
    return x-5

print(list(map(scade_5, colectie)))
# aplica functia pt fiecare element din colectie

# %%
colectie = ["100", "200", "300"]

print(colectie)
print(list(map(int, colectie)))

def putere(x):
    return x**2

print(list(map(putere, list(map(int, colectie)))))