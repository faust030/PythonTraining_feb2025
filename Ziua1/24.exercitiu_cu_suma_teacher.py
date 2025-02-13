string = "11, 22, 33, 44, 22, 33"
numbers = string.split(",")
print(numbers)

unice = [int(i) for i in numbers if numbers.count(i) == 1]
print(unice)

suma = sum(unice)
print(suma)