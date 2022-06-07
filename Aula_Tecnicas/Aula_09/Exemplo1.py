def somar_val(lista: list, valor: int) -> None:
    for i in range(0, len(lista)):
        lista[i] = lista[i] + valor

lista = [1, 2, 3, 4, 5]
somar_val(lista, 5)
print(lista)