#Faça um algoritmo que leia 5 números inteiros e escreva a soma dos que forem ímpares.

soma = 0
for numero in range(1, 6):
    num = int(input(f'insira o {numero} numero: '))
    if(num % 2 == 1):
        soma = soma + num
print(f'a soma dos numeros impares eh: {soma}')

print("fazendo em while....")

soma1 = 0
cont = 1
while cont <= 5:
    num1 = int(input(f'insira o {cont} numero: '))
    if(num1 % 2 == 1):
        soma1 = soma1 + num1
    cont += 1
print(f'a soma dos numeros impares eh: {soma1}')

