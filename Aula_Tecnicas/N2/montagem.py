lista = []
lista2 = []
for i in range(0, 5): 
    altura = int(input("insira as alturas: "))
    lista.append(altura)

    polegada: float
    polegada = altura * 2.54
    print(polegada)

    lista2.append(polegada)


print(lista)
print(lista2)