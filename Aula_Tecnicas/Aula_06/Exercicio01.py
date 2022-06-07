#Exercício 1 - Faça um algoritmo que imprima a metade de cada número de 10 a 20.
#Fazendo com for e While
def imprimir_metade():
    for n in range(10, 21):
        metade = n / 2
        print(metade)

imprimir_metade()

print("comecando while")

numeros = 10
cont = 0
    
while cont <= 10:
    metade1 = numeros / 2
    numeros = numeros + 1
    cont += 1
    print(metade1)


