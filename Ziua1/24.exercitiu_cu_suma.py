def functia_smechera(string):
    suma = 0
    my_list = string.split(",")
    my_list_unice = []

    for i in my_list:
        count = 0
        for j in my_list:
            if i == j:
                count += 1
        if count == 1:
            suma += int(i)
            my_list_unice.append(i)
    
    print("Lista este:", my_list)
    print("Lista de elemente unice este:", my_list_unice)
    print("Suma este:", suma)

functia_smechera("1,2,3,2")
functia_smechera("1,1,1,1,1")
functia_smechera("1,2,3,4,5")
functia_smechera("11, 22, 33, 44, 22, 33")