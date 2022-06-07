def polegadas(lista: list):
        lista2 = {}
        for i in lista:
            lista_valor = lista[i] * 2.54
            lista2.append(lista_valor)
        return lista2

lista = {}
for i in range(0, 5): 
    altura = int(input("insira as alturas em cm: "))
    altura = altura * 2.54
    lista.append(altura)


#print("A lista de polegadas eh: ", lista2)
polegadas()
    

