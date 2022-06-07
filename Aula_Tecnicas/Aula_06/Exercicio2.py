#Faça um algoritmo que imprima a tabuada do 5.

def tabuada():
    for n in range(0, 11):
        calculo = n * 5
        print(calculo)

tabuada()


print("agora while....")

cont = 0
num = 5

while cont <= 10:
    calculo1 = num * cont
    cont += 1
    print(calculo1)

print("modelo professor")

def tabuada(tabuada: int):
    for numero in range(0, 11):
        resultado = tabuada * numero
        print(f'{tabuada} x {numero} = {resultado}')

tabuada(5)
    









